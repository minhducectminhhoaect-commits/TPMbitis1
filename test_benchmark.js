
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

const raw = generateData(10000); // 10k items
const sIn = new Date().toISOString().slice(0, 10);
const eIn = new Date().toISOString().slice(0, 10);

// Current implementation
function currentImpl(raw, sIn, eIn) {
    const start = performance.now();
    const filtered = raw.filter(i => {
        if (sIn && eIn) {
            const d = i.gio_hu ? new Date(i.gio_hu) : new Date();
            const s = new Date(sIn);
            const e = new Date(eIn);
            e.setHours(23, 59, 59);
            if (d < s || d > e) return false;
        }
        return true;
    });

    let tot = 0;
    filtered.forEach(i => {
        if (i.gio_hu && i.gio_chay_lai) {
            const dt = (new Date(i.gio_chay_lai) - new Date(i.gio_hu)) / 36e5;
            if (dt > 0) tot += dt;
        }
        if (i.gio_hu && i.gio_xong) {
             const rep = (new Date(i.gio_xong) - new Date(i.gio_hu)) / 60000;
        }
    });
    const end = performance.now();
    return end - start;
}

// Optimized implementation
function optimizedImpl(raw, sIn, eIn) {
    const start = performance.now();

    // Hoist date parsing
    let sTime, eTime;
    if (sIn && eIn) {
        const s = new Date(sIn);
        const e = new Date(eIn);
        e.setHours(23, 59, 59);
        sTime = s.getTime();
        eTime = e.getTime();
    }

    const filtered = [];
    // Single loop for filtering and preparing data could be faster, but let's stick to structure
    // Actually, let's keep filter separate to match logic structure but optimize the predicate

    for (let i = 0; i < raw.length; i++) {
        const item = raw[i];
        if (sIn && eIn) {
            const dTime = item.gio_hu ? new Date(item.gio_hu).getTime() : Date.now();
            if (dTime < sTime || dTime > eTime) continue;
            // Optimization: Store parsed time if we're going to use it later?
            // In a real app we might not want to mutate 'item' if it's shared, but here it's fresh from API.
            // Let's assume we can attach it or just parse it.
            // For now, just hoisting s and e is the big win.
        }
        filtered.push(item);
    }

    let tot = 0;
    for (let i = 0; i < filtered.length; i++) {
        const item = filtered[i];
        // Parse once
        const tHu = item.gio_hu ? new Date(item.gio_hu).getTime() : 0;

        if (tHu && item.gio_chay_lai) {
            const tChay = new Date(item.gio_chay_lai).getTime();
            const dt = (tChay - tHu) / 36e5;
            if (dt > 0) tot += dt;
        }
        if (tHu && item.gio_xong) {
             const tXong = new Date(item.gio_xong).getTime();
             const rep = (tXong - tHu) / 60000;
        }
    }

    const end = performance.now();
    return end - start;
}

// Warmup
currentImpl(raw.slice(0, 100), sIn, eIn);
optimizedImpl(raw.slice(0, 100), sIn, eIn);

// Run benchmark
let currentTotal = 0;
let optimizedTotal = 0;
const iterations = 50;

for(let i=0; i<iterations; i++) {
    currentTotal += currentImpl(raw, sIn, eIn);
    optimizedTotal += optimizedImpl(raw, sIn, eIn);
}

console.log(`Current Avg: ${(currentTotal/iterations).toFixed(2)}ms`);
console.log(`Optimized Avg: ${(optimizedTotal/iterations).toFixed(2)}ms`);
console.log(`Speedup: ${(currentTotal/optimizedTotal).toFixed(2)}x`);
