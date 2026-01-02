
const { performance } = require('perf_hooks');

const dates = [];
for (let i = 0; i < 10000; i++) {
    dates.push(new Date().toISOString());
}

function runOriginal() {
    const start = performance.now();
    for (const d of dates) {
        // Original logic: new Date(s).toLocaleString(...)
        const s = new Date(d).toLocaleString('vi-VN', {hour:'2-digit', minute:'2-digit', day:'2-digit', month:'2-digit'});
    }
    return performance.now() - start;
}

function runOptimized() {
    const start = performance.now();
    const dateFormatter = new Intl.DateTimeFormat('vi-VN', {hour:'2-digit', minute:'2-digit', day:'2-digit', month:'2-digit'});
    for (const d of dates) {
        // Optimized logic: reuse formatter
        const s = dateFormatter.format(new Date(d));
    }
    return performance.now() - start;
}

// Warmup
runOriginal();
runOptimized();

const originalTimes = [];
const optimizedTimes = [];

for(let i=0; i<20; i++) {
    originalTimes.push(runOriginal());
    optimizedTimes.push(runOptimized());
}

const avgOriginal = originalTimes.reduce((a,b)=>a+b,0) / originalTimes.length;
const avgOptimized = optimizedTimes.reduce((a,b)=>a+b,0) / optimizedTimes.length;

console.log(`Original (toLocaleString) Avg: ${avgOriginal.toFixed(3)}ms`);
console.log(`Optimized (Intl.DateTimeFormat) Avg: ${avgOptimized.toFixed(3)}ms`);
console.log(`Improvement: ${((avgOriginal - avgOptimized) / avgOriginal * 100).toFixed(2)}%`);

if (avgOptimized < avgOriginal) {
    console.log("PASS: Optimization verified.");
} else {
    console.log("FAIL: Optimization did not improve performance.");
}
