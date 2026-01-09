
const vsmMap = {"Hoàn chỉnh 1": "VSM 1", "Hoàn chỉnh 2": "VSM 2", "May 1": "VSM 1", "May 2": "VSM 1", "May 3": "VSM 1", "May 4": "VSM 1", "May 5": "VSM 2", "May 6": "VSM 2", "Dập 1": "VSM 1", "Dập 2": "VSM 2", "In lụa": "VSM 1", "Bế hình": "VSM 1", "Cán dán": "VSM 1", "Cắt trục": "VSM 1", "Ép dấu chân": "VSM 2", "Chuẩn bị đế": "VSM 2", "Bọc đế": "VSM 2", "Bán thành phẩm": "VSM 2", "Cắt nhiệt": "VSM 1", "Phát sinh": "Phát sinh"};

// Generate 100k items
const raw = [];
const lines = Object.keys(vsmMap);
const now = Date.now();
for (let i = 0; i < 100000; i++) {
    raw.push({
        id: i,
        chuyen: lines[i % lines.length],
        gio_hu: new Date(now - Math.floor(Math.random() * 10000000000)).toISOString(),
        ten_bao_tri: i % 2 === 0 ? "Tech A" : "Tech B"
    });
}

const sIn = "2023-01-01";
const eIn = "2023-12-31";
const vsmV = "all";
const lineV = "all";

console.log(`Benchmarking with ${raw.length} items...`);

// Test Current
console.time("Current");
for(let k=0; k<10; k++) {
    raw.filter(i => {
        if (sIn && eIn) { const d=i.gio_hu?new Date(i.gio_hu):new Date(), s=new Date(sIn), e=new Date(eIn); e.setHours(23,59,59); if(d<s||d>e) return false; }
        if(vsmV!=='all' && (vsmMap[i.chuyen]||"Khác")!==vsmV) return false;
        if(lineV!=='all' && i.chuyen!==lineV) return false;
        return true;
    });
}
console.timeEnd("Current");

// Test Optimized
console.time("Optimized");
for(let k=0; k<10; k++) {
    let s, e;
    if (sIn && eIn) {
        s = new Date(sIn);
        e = new Date(eIn);
        e.setHours(23, 59, 59);
    }
    raw.filter(i => {
        if (s && e) {
             const d=i.gio_hu?new Date(i.gio_hu):new Date();
             if(d<s||d>e) return false;
        }
        if(vsmV!=='all' && (vsmMap[i.chuyen]||"Khác")!==vsmV) return false;
        if(lineV!=='all' && i.chuyen!==lineV) return false;
        return true;
    });
}
console.timeEnd("Optimized");
