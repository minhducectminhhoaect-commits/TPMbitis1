
const assert = require('assert');
const { performance } = require('perf_hooks');

// Mocks
const vsmMap = {"Hoàn chỉnh 1": "VSM 1", "Hoàn chỉnh 2": "VSM 2", "May 1": "VSM 1", "May 2": "VSM 1", "May 3": "VSM 1", "May 4": "VSM 1", "May 5": "VSM 2", "May 6": "VSM 2", "Dập 1": "VSM 1", "Dập 2": "VSM 2", "In lụa": "VSM 1", "Bế hình": "VSM 1", "Cán dán": "VSM 1", "Cắt trục": "VSM 1", "Ép dấu chân": "VSM 2", "Chuẩn bị đế": "VSM 2", "Bọc đế": "VSM 2", "Bán thành phẩm": "VSM 2", "Cắt nhiệt": "VSM 1", "Phát sinh": "Phát sinh"};

// Original function (extracted)
function loadDashboardDataOriginal(raw, sIn, eIn, vsmV, lineV) {
    const filtered = raw.filter(i => {
        if (sIn && eIn) { const d=i.gio_hu?new Date(i.gio_hu):new Date(), s=new Date(sIn), e=new Date(eIn); e.setHours(23,59,59); if(d<s||d>e) return false; }
        if(vsmV!=='all' && (vsmMap[i.chuyen]||"Khác")!==vsmV) return false;
        if(lineV!=='all' && i.chuyen!==lineV) return false;
        return true;
    });
    let tot=0, mttrS=0, mttrC=0, lS={}, tS={};
    filtered.forEach(i=>{
        const l=i.chuyen||"Khác", t=i.ten_bao_tri||"Chưa gán";
        if(!lS[l])lS[l]={tk:0,dt:0}; if(!tS[t])tS[t]={tk:0,dt:0};
        lS[l].tk++; if(i.ten_bao_tri) tS[t].tk++;
        // Downtime Chuyền: Giờ chạy lại (I) - Giờ hư (F)
        if(i.gio_hu && i.gio_chay_lai){ const dt=(new Date(i.gio_chay_lai)-new Date(i.gio_hu))/36e5; if(dt>0){ tot+=dt; lS[l].dt+=dt; } }
        // MTTR Máy: Giờ sửa xong (L) - Giờ hư (F)
        if(i.gio_hu && i.gio_xong){ const rep=(new Date(i.gio_xong)-new Date(i.gio_hu))/60000; if(rep>0 && i.ten_bao_tri){ tS[t].dt+=rep; mttrS+=rep; mttrC++; } }
    });
    return {tot, mttrC, lS, tS, count: filtered.length};
}

// Optimized function
function loadDashboardDataOptimized(raw, sIn, eIn, vsmV, lineV) {
    let sTime, eTime;
    if (sIn && eIn) {
        const s = new Date(sIn);
        const e = new Date(eIn);
        e.setHours(23, 59, 59);
        sTime = s.getTime();
        eTime = e.getTime();
    }

    const filtered = [];
    // Single loop for filter
    for(let i = 0; i < raw.length; i++) {
        const item = raw[i];
        if (sTime !== undefined) {
             const d = item.gio_hu ? new Date(item.gio_hu).getTime() : Date.now();
             if (d < sTime || d > eTime) continue;
        }
        if(vsmV !== 'all' && (vsmMap[item.chuyen] || "Khác") !== vsmV) continue;
        if(lineV !== 'all' && item.chuyen !== lineV) continue;
        filtered.push(item);
    }

    let tot=0, mttrS=0, mttrC=0, lS={}, tS={};

    // Process aggregated data
    for(let i = 0; i < filtered.length; i++) {
        const item = filtered[i];
        const l=item.chuyen||"Khác", t=item.ten_bao_tri||"Chưa gán";
        if(!lS[l])lS[l]={tk:0,dt:0}; if(!tS[t])tS[t]={tk:0,dt:0};

        lS[l].tk++;
        if(item.ten_bao_tri) tS[t].tk++;

        // Cache parsed gio_hu to avoid double parsing
        let huTime = 0;
        if (item.gio_hu) huTime = new Date(item.gio_hu).getTime();

        // Downtime Chuyền: Giờ chạy lại (I) - Giờ hư (F)
        if(huTime && item.gio_chay_lai){
            const chayLaiTime = new Date(item.gio_chay_lai).getTime();
            const dt=(chayLaiTime - huTime)/36e5;
            if(dt>0){ tot+=dt; lS[l].dt+=dt; }
        }
        // MTTR Máy: Giờ sửa xong (L) - Giờ hư (F)
        if(huTime && item.gio_xong){
            const xongTime = new Date(item.gio_xong).getTime();
            const rep=(xongTime - huTime)/60000;
            if(rep>0 && item.ten_bao_tri){ tS[t].dt+=rep; mttrS+=rep; mttrC++; }
        }
    }
    return {tot, mttrC, lS, tS, count: filtered.length};
}

// Generate data
const rawData = [];
const start = new Date('2023-01-01');
for (let i = 0; i < 10000; i++) {
    const hu = new Date(start.getTime() + i * 3600000).toISOString();
    const xong = new Date(new Date(hu).getTime() + Math.random() * 7200000).toISOString();
    const chay = new Date(new Date(xong).getTime() + Math.random() * 1800000).toISOString();
    rawData.push({
        id: i,
        chuyen: `May ${i % 6 + 1}`,
        ten_bao_tri: `Tho ${i % 5}`,
        gio_hu: hu,
        gio_xong: xong,
        gio_chay_lai: chay
    });
}

// Benchmarking
const sIn = '2023-01-01';
const eIn = '2023-12-31';
const vsmV = 'all';
const lineV = 'all';

console.log('Running benchmark...');

const t1 = performance.now();
for(let i=0; i<100; i++) loadDashboardDataOriginal(rawData, sIn, eIn, vsmV, lineV);
const t2 = performance.now();
console.log(`Original: ${(t2-t1).toFixed(2)}ms`);

const t3 = performance.now();
for(let i=0; i<100; i++) loadDashboardDataOptimized(rawData, sIn, eIn, vsmV, lineV);
const t4 = performance.now();
console.log(`Optimized: ${(t4-t3).toFixed(2)}ms`);

// Verification
const res1 = loadDashboardDataOriginal(rawData, sIn, eIn, vsmV, lineV);
const res2 = loadDashboardDataOptimized(rawData, sIn, eIn, vsmV, lineV);

try {
    assert.strictEqual(res1.count, res2.count);
    assert.strictEqual(res1.tot.toFixed(5), res2.tot.toFixed(5));
    assert.strictEqual(res1.mttrC, res2.mttrC);
    console.log('Verification PASSED');
} catch (e) {
    console.error('Verification FAILED', e);
}
