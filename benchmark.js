
const vsmMap = {"Hoàn chỉnh 1": "VSM 1", "Hoàn chỉnh 2": "VSM 2", "May 1": "VSM 1", "May 2": "VSM 1", "May 3": "VSM 1", "May 4": "VSM 1", "May 5": "VSM 2", "May 6": "VSM 2", "Dập 1": "VSM 1", "Dập 2": "VSM 2", "In lụa": "VSM 1", "Bế hình": "VSM 1", "Cán dán": "VSM 1", "Cắt trục": "VSM 1", "Ép dấu chân": "VSM 2", "Chuẩn bị đế": "VSM 2", "Bọc đế": "VSM 2", "Bán thành phẩm": "VSM 2", "Cắt nhiệt": "VSM 1", "Phát sinh": "Phát sinh"};

function generateData(count) {
    const data = [];
    const now = new Date();
    for (let i = 0; i < count; i++) {
        data.push({
            chuyen: "May 1",
            ten_bao_tri: "Tech 1",
            gio_hu: new Date(now.getTime() - Math.random() * 1000000000).toISOString(),
            gio_chay_lai: new Date(now.getTime() - Math.random() * 100000000).toISOString(),
            gio_xong: new Date(now.getTime() - Math.random() * 100000000).toISOString(),
        });
    }
    return data;
}

const raw = generateData(10000);
const sIn = "2023-01-01";
const eIn = "2025-12-31";
const vsmV = "all";
const lineV = "all";

function original() {
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
    return { tot, mttrC };
}

function optimized() {
    let tot=0, mttrS=0, mttrC=0, lS={}, tS={};

    // Optimization 1: Parse dates outside the loop
    const s = sIn ? new Date(sIn) : null;
    const e = eIn ? new Date(eIn) : null;
    if (e) e.setHours(23, 59, 59, 999);

    for (let i of raw) {
        // Optimization 3: Parse gio_hu once
        const dStr = i.gio_hu;
        const d = dStr ? new Date(dStr) : new Date();

        // Optimization 2: Combine filter and processing
        if (s && e) {
            if (d < s || d > e) continue;
        }
        if (vsmV !== 'all' && (vsmMap[i.chuyen] || "Khác") !== vsmV) continue;
        if (lineV !== 'all' && i.chuyen !== lineV) continue;

        const l = i.chuyen || "Khác";
        const t = i.ten_bao_tri || "Chưa gán";

        if (!lS[l]) lS[l] = { tk: 0, dt: 0 };
        if (!tS[t]) tS[t] = { tk: 0, dt: 0 };

        lS[l].tk++;
        if (i.ten_bao_tri) tS[t].tk++;

        const dateHu = d.getTime(); // Use the already parsed date time

        if (dStr && i.gio_chay_lai) {
            const dateChayLai = new Date(i.gio_chay_lai).getTime();
            const dt = (dateChayLai - dateHu) / 36e5;
            if (dt > 0) {
                tot += dt;
                lS[l].dt += dt;
            }
        }

        if (dStr && i.gio_xong) {
            const dateXong = new Date(i.gio_xong).getTime();
            const rep = (dateXong - dateHu) / 60000;
            if (rep > 0 && i.ten_bao_tri) {
                tS[t].dt += rep;
                mttrS += rep;
                mttrC++;
            }
        }
    }
    return { tot, mttrC };
}

console.time('Original');
const r1 = original();
console.timeEnd('Original');

console.time('Optimized');
const r2 = optimized();
console.timeEnd('Optimized');

// Verification
console.log('Results match:', Math.abs(r1.tot - r2.tot) < 0.001 && r1.mttrC === r2.mttrC);
