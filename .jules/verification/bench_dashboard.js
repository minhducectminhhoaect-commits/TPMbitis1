
const { performance } = require('perf_hooks');

// Mock data generation
const items = [];
const startDate = new Date('2023-01-01').getTime();
const endDate = new Date('2023-12-31').getTime();
const lines = ["Hoàn chỉnh 1", "Hoàn chỉnh 2", "May 1", "May 2", "Dập 1"];
const vsmMap = {"Hoàn chỉnh 1": "VSM 1", "Hoàn chỉnh 2": "VSM 2", "May 1": "VSM 1", "May 2": "VSM 1", "Dập 1": "VSM 1"};

for (let i = 0; i < 100000; i++) {
    items.push({
        gio_hu: new Date(startDate + Math.random() * (endDate - startDate)).toISOString(),
        chuyen: lines[Math.floor(Math.random() * lines.length)],
        ten_bao_tri: "Tech " + Math.floor(Math.random() * 5),
        gio_xong: new Date(startDate + Math.random() * (endDate - startDate)).toISOString(),
        gio_chay_lai: new Date(startDate + Math.random() * (endDate - startDate)).toISOString()
    });
}

const sIn = '2023-03-01';
const eIn = '2023-08-01';
const vsmV = 'all';
const lineV = 'all';

function runOriginal() {
    const raw = items;
    const start = performance.now();

    // Original Logic
    const filtered = raw.filter(i => {
        if (sIn && eIn) {
            const d=i.gio_hu?new Date(i.gio_hu):new Date(), s=new Date(sIn), e=new Date(eIn);
            e.setHours(23,59,59);
            if(d<s||d>e) return false;
        }
        if(vsmV!=='all' && (vsmMap[i.chuyen]||"Khác")!==vsmV) return false;
        if(lineV!=='all' && i.chuyen!==lineV) return false;
        return true;
    });

    return performance.now() - start;
}

function runOptimized() {
    const raw = items;
    const start = performance.now();

    // Optimized Logic
    let sDate, eDate;
    if (sIn && eIn) {
        sDate = new Date(sIn);
        eDate = new Date(eIn);
        eDate.setHours(23, 59, 59);
    }
    const filtered = raw.filter(i => {
        if (sDate && eDate) {
            const d = i.gio_hu ? new Date(i.gio_hu) : new Date();
            if (d < sDate || d > eDate) return false;
        }
        if (vsmV !== 'all' && (vsmMap[i.chuyen] || "Khác") !== vsmV) return false;
        if (lineV !== 'all' && i.chuyen !== lineV) return false;
        return true;
    });

    return performance.now() - start;
}

// Warmup
runOriginal();
runOptimized();

const originalTimes = [];
const optimizedTimes = [];

for(let i=0; i<50; i++) {
    originalTimes.push(runOriginal());
    optimizedTimes.push(runOptimized());
}

const avgOriginal = originalTimes.reduce((a,b)=>a+b,0) / originalTimes.length;
const avgOptimized = optimizedTimes.reduce((a,b)=>a+b,0) / optimizedTimes.length;

console.log(`Original Avg: ${avgOriginal.toFixed(3)}ms`);
console.log(`Optimized Avg: ${avgOptimized.toFixed(3)}ms`);
console.log(`Improvement: ${((avgOriginal - avgOptimized) / avgOriginal * 100).toFixed(2)}%`);

if (avgOptimized < avgOriginal) {
    console.log("PASS: Optimization verified.");
} else {
    console.log("FAIL: Optimization did not improve performance.");
}
