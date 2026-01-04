
const { performance } = require('perf_hooks');

// Mock data generation
const count = 10000;
const raw = [];
const now = new Date();
for (let i = 0; i < count; i++) {
    const d = new Date(now);
    d.setDate(d.getDate() - Math.floor(Math.random() * 30));
    raw.push({
        gio_hu: d.toISOString(),
        chuyen: `May ${Math.floor(Math.random() * 6) + 1}`,
        ma_so: `MSTS-${i}`
    });
}

const sIn = new Date(now);
sIn.setDate(sIn.getDate() - 20);
const sInStr = sIn.toISOString().slice(0, 10);

const eIn = new Date(now);
eIn.setDate(eIn.getDate() - 5);
const eInStr = eIn.toISOString().slice(0, 10);

const vsmV = 'all'; // Simplified for this test
const lineV = 'all'; // Simplified for this test
const vsmMap = {}; // Not needed for the date bottleneck test

// ORIGINAL FUNCTION (Simulated)
function originalFilter() {
    return raw.filter(i => {
        // The bottleneck:
        if (sInStr && eInStr) {
            const d=i.gio_hu?new Date(i.gio_hu):new Date(), s=new Date(sInStr), e=new Date(eInStr);
            e.setHours(23,59,59);
            if(d<s||d>e) return false;
        }
        return true;
    });
}

// OPTIMIZED FUNCTION
function optimizedFilter() {
    // Hoisting invariants
    let sTime = 0, eTime = 0;
    if (sInStr && eInStr) {
        const s = new Date(sInStr);
        const e = new Date(eInStr);
        e.setHours(23, 59, 59, 999); // Be precise
        sTime = s.getTime();
        eTime = e.getTime();
    }

    return raw.filter(i => {
        if (sTime && eTime) {
            const dTime = i.gio_hu ? new Date(i.gio_hu).getTime() : Date.now();
            if (dTime < sTime || dTime > eTime) return false;
        }
        return true;
    });
}

console.log(`Benchmarking with ${count} items...`);

// Warmup
originalFilter();
optimizedFilter();

const t1 = performance.now();
for(let i=0; i<100; i++) originalFilter();
const t2 = performance.now();

const t3 = performance.now();
for(let i=0; i<100; i++) optimizedFilter();
const t4 = performance.now();

console.log(`Original: ${(t2 - t1).toFixed(2)}ms`);
console.log(`Optimized: ${(t4 - t3).toFixed(2)}ms`);
console.log(`Speedup: ${((t2 - t1) / (t4 - t3)).toFixed(2)}x`);
