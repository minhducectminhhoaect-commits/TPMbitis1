
const { performance } = require('perf_hooks');

const vsmMap = {"Hoàn chỉnh 1": "VSM 1", "Hoàn chỉnh 2": "VSM 2", "May 1": "VSM 1", "May 2": "VSM 1", "May 3": "VSM 1", "May 4": "VSM 1", "May 5": "VSM 2", "May 6": "VSM 2", "Dập 1": "VSM 1", "Dập 2": "VSM 2", "In lụa": "VSM 1", "Bế hình": "VSM 1", "Cán dán": "VSM 1", "Cắt trục": "VSM 1", "Ép dấu chân": "VSM 2", "Chuẩn bị đế": "VSM 2", "Bọc đế": "VSM 2", "Bán thành phẩm": "VSM 2", "Cắt nhiệt": "VSM 1", "Phát sinh": "Phát sinh"};

const sIn = "2023-01-01";
const eIn = "2023-12-31";
const vsmV = "all";
const lineV = "all";

// Generate mock data
const raw = [];
const size = 100000;
for (let i = 0; i < size; i++) {
    raw.push({
        gio_hu: new Date(2023, Math.floor(Math.random() * 12), Math.floor(Math.random() * 28)).toISOString(),
        chuyen: Object.keys(vsmMap)[Math.floor(Math.random() * Object.keys(vsmMap).length)]
    });
}

function runOriginal() {
    const start = performance.now();
    const filtered = raw.filter(i => {
        if (sIn && eIn) {
            const d = i.gio_hu ? new Date(i.gio_hu) : new Date();
            const s = new Date(sIn);
            const e = new Date(eIn);
            e.setHours(23,59,59);
            if(d<s||d>e) return false;
        }
        if(vsmV!=='all' && (vsmMap[i.chuyen]||"Khác")!==vsmV) return false;
        if(lineV!=='all' && i.chuyen!==lineV) return false;
        return true;
    });
    const end = performance.now();
    return end - start;
}

function runOptimized() {
    const start = performance.now();

    // Optimization: Hoist Date parsing
    let s, e;
    if (sIn && eIn) {
        s = new Date(sIn);
        e = new Date(eIn);
        e.setHours(23,59,59);
    }

    const filtered = raw.filter(i => {
        if (sIn && eIn) {
            const d = i.gio_hu ? new Date(i.gio_hu) : new Date();
            // Using hoisted s and e
            if(d<s||d>e) return false;
        }
        if(vsmV!=='all' && (vsmMap[i.chuyen]||"Khác")!==vsmV) return false;
        if(lineV!=='all' && i.chuyen!==lineV) return false;
        return true;
    });
    const end = performance.now();
    return end - start;
}

console.log("Warming up...");
runOriginal();
runOptimized();

console.log("Running benchmark...");
const tOriginal = runOriginal();
const tOptimized = runOptimized();

console.log(`Original: ${tOriginal.toFixed(2)}ms`);
console.log(`Optimized: ${tOptimized.toFixed(2)}ms`);
console.log(`Improvement: ${((tOriginal - tOptimized) / tOriginal * 100).toFixed(2)}%`);
