
const assert = require('assert');

// Mock data generation
const generateData = (count) => {
    const data = [];
    const now = new Date();
    for (let i = 0; i < count; i++) {
        data.push({
            chuyen: `Line ${i % 10}`,
            gio_hu: new Date(now.getTime() - Math.random() * 1000000000).toISOString(),
            gio_chay_lai: new Date(now.getTime() - Math.random() * 500000000).toISOString(),
            gio_xong: new Date(now.getTime() - Math.random() * 500000000).toISOString(),
            ten_bao_tri: `Tech ${i % 5}`
        });
    }
    return data;
};

const raw = generateData(1000);
const sIn = new Date(Date.now() - 500000000).toISOString().slice(0, 10);
const eIn = new Date().toISOString().slice(0, 10);
const vsmMap = {};

// Helper for logic
function logic(raw, sIn, eIn, vsmV, lineV) {
    // Original Logic simulation
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
    return { count: filtered.length, tot, mttrC, mttrS };
}

function optimizedLogic(raw, sIn, eIn, vsmV, lineV) {
    // Optimized Logic
    let sDate, eDate;
    if (sIn && eIn) { sDate = new Date(sIn); eDate = new Date(eIn); eDate.setHours(23,59,59); }

    const filtered = raw.filter(i => {
        if (sDate && eDate) { const d=i.gio_hu?new Date(i.gio_hu):new Date(); if(d<sDate||d>eDate) return false; }
        if(vsmV!=='all' && (vsmMap[i.chuyen]||"Khác")!==vsmV) return false;
        if(lineV!=='all' && i.chuyen!==lineV) return false;
        return true;
    });
    let tot=0, mttrS=0, mttrC=0, lS={}, tS={};
    filtered.forEach(i=>{
        const l=i.chuyen||"Khác", t=i.ten_bao_tri||"Chưa gán";
        if(!lS[l])lS[l]={tk:0,dt:0}; if(!tS[t])tS[t]={tk:0,dt:0};
        lS[l].tk++; if(i.ten_bao_tri) tS[t].tk++;

        const dHu = i.gio_hu ? new Date(i.gio_hu) : null;

        if(dHu && i.gio_chay_lai){ const dt=(new Date(i.gio_chay_lai)-dHu)/36e5; if(dt>0){ tot+=dt; lS[l].dt+=dt; } }
        if(dHu && i.gio_xong){ const rep=(new Date(i.gio_xong)-dHu)/60000; if(rep>0 && i.ten_bao_tri){ tS[t].dt+=rep; mttrS+=rep; mttrC++; } }
    });
    return { count: filtered.length, tot, mttrC, mttrS };
}

// Check correctness
const res1 = logic(raw, sIn, eIn, 'all', 'all');
const res2 = optimizedLogic(raw, sIn, eIn, 'all', 'all');

console.log('Original:', res1);
console.log('Optimized:', res2);

assert.strictEqual(res1.count, res2.count, 'Count mismatch');
// Floating point comparison
assert.ok(Math.abs(res1.tot - res2.tot) < 0.00001, 'Total Downtime mismatch');
assert.ok(Math.abs(res1.mttrS - res2.mttrS) < 0.00001, 'MTTR Sum mismatch');
assert.strictEqual(res1.mttrC, res2.mttrC, 'MTTR Count mismatch');

console.log('Verification Passed!');
