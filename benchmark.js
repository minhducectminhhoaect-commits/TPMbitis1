
const { performance } = require('perf_hooks');

// Mock data generation
const count = 10000;
const raw = [];
const vsmMap = {"Hoàn chỉnh 1": "VSM 1", "May 1": "VSM 1"};
const users = ["User A", "User B", "User C"];
const lines = ["Hoàn chỉnh 1", "May 1", "May 2"];

for (let i = 0; i < count; i++) {
    raw.push({
        gio_hu: new Date(Date.now() - Math.random() * 10000000).toISOString(),
        gio_chay_lai: new Date(Date.now()).toISOString(),
        gio_xong: new Date(Date.now() - Math.random() * 500000).toISOString(),
        chuyen: lines[i % lines.length],
        ten_bao_tri: users[i % users.length]
    });
}

const sIn = new Date(Date.now() - 20000000).toISOString().slice(0, 10);
const eIn = new Date(Date.now() + 20000000).toISOString().slice(0, 10);
const vsmV = 'all';
const lineV = 'all';

// Original Logic
function original() {
    const start = performance.now();
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
    return performance.now() - start;
}

// Optimized Logic
function optimized() {
    const start = performance.now();

    // Hoist Date creation
    let sTime = 0, eTime = 0;
    if (sIn && eIn) {
        const s = new Date(sIn);
        const e = new Date(eIn);
        e.setHours(23,59,59);
        sTime = s.getTime();
        eTime = e.getTime();
    }

    const filtered = raw.filter(i => {
        if (sIn && eIn) {
            // Use getTime() for comparison if possible, or just date object but avoid recreating s and e
            const dTime = i.gio_hu ? new Date(i.gio_hu).getTime() : Date.now();
            if(dTime < sTime || dTime > eTime) return false;
        }
        if(vsmV!=='all' && (vsmMap[i.chuyen]||"Khác")!==vsmV) return false;
        if(lineV!=='all' && i.chuyen!==lineV) return false;
        return true;
    });

    let tot=0, mttrS=0, mttrC=0, lS={}, tS={};
    filtered.forEach(i=>{
        const l=i.chuyen||"Khác", t=i.ten_bao_tri||"Chưa gán";
        if(!lS[l])lS[l]={tk:0,dt:0}; if(!tS[t])tS[t]={tk:0,dt:0};
        lS[l].tk++; if(i.ten_bao_tri) tS[t].tk++;

        // Cache parsed dates
        const dHu = i.gio_hu ? new Date(i.gio_hu) : null;
        const tHu = dHu ? dHu.getTime() : 0;

        // Downtime Chuyền
        if(dHu && i.gio_chay_lai){
            const dt=(new Date(i.gio_chay_lai).getTime() - tHu)/36e5;
            if(dt>0){ tot+=dt; lS[l].dt+=dt; }
        }
        // MTTR Máy
        if(dHu && i.gio_xong){
            const rep=(new Date(i.gio_xong).getTime() - tHu)/60000;
            if(rep>0 && i.ten_bao_tri){ tS[t].dt+=rep; mttrS+=rep; mttrC++; }
        }
    });
    return performance.now() - start;
}

console.log("Original:", original().toFixed(2), "ms");
console.log("Optimized:", optimized().toFixed(2), "ms");
