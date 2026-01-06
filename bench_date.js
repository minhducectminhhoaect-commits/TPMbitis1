
const ITERATIONS = 100000;
const sIn = "2023-01-01";
const eIn = "2023-12-31";

const data = [];
for (let i = 0; i < ITERATIONS; i++) {
    data.push({
        gio_hu: "2023-06-15T10:00:00.000Z",
        chuyen: "May 1",
        ten_bao_tri: "Tech A",
        gio_chay_lai: "2023-06-15T12:00:00.000Z",
        gio_xong: "2023-06-15T11:00:00.000Z"
    });
}

console.log(`Running benchmark with ${ITERATIONS} items...`);

// Original approach
console.time("Original");
const filtered1 = data.filter(i => {
    if (sIn && eIn) {
        const d = i.gio_hu ? new Date(i.gio_hu) : new Date();
        const s = new Date(sIn);
        const e = new Date(eIn);
        e.setHours(23, 59, 59);
        if (d < s || d > e) return false;
    }
    return true;
});
console.timeEnd("Original");

// Optimized approach
console.time("Optimized");
let s, e;
if (sIn && eIn) {
    s = new Date(sIn);
    e = new Date(eIn);
    e.setHours(23, 59, 59);
}

const filtered2 = data.filter(i => {
    if (sIn && eIn) {
        const d = i.gio_hu ? new Date(i.gio_hu) : new Date();
        // s and e are already created
        if (d < s || d > e) return false;
    }
    return true;
});
console.timeEnd("Optimized");

// Loop optimization
console.time("Loop Original");
let tot1 = 0;
filtered1.forEach(i => {
    if(i.gio_hu && i.gio_chay_lai){ const dt=(new Date(i.gio_chay_lai)-new Date(i.gio_hu))/36e5; if(dt>0){ tot1+=dt; } }
    if(i.gio_hu && i.gio_xong){ const rep=(new Date(i.gio_xong)-new Date(i.gio_hu))/60000; if(rep>0){ } }
});
console.timeEnd("Loop Original");

console.time("Loop Optimized");
let tot2 = 0;
filtered2.forEach(i => {
    const dHu = i.gio_hu ? new Date(i.gio_hu) : null;
    if(dHu && i.gio_chay_lai){ const dt=(new Date(i.gio_chay_lai)-dHu)/36e5; if(dt>0){ tot2+=dt; } }
    if(dHu && i.gio_xong){ const rep=(new Date(i.gio_xong)-dHu)/60000; if(rep>0){ } }
});
console.timeEnd("Loop Optimized");
