
const ITERATIONS = 100000;
const raw = [];
// Generate mock data
for (let i = 0; i < ITERATIONS; i++) {
    raw.push({
        gio_hu: new Date(Date.now() - Math.floor(Math.random() * 1000000000)).toISOString(),
        chuyen: "May " + (i % 6 + 1)
    });
}

const sIn = new Date(Date.now() - 500000000).toISOString().slice(0, 10);
const eIn = new Date(Date.now()).toISOString().slice(0, 10);

function slowFilter() {
    return raw.filter(i => {
        if (sIn && eIn) {
            const d=i.gio_hu?new Date(i.gio_hu):new Date();
            // THIS IS THE BOTTLENECK: creating new Date(sIn) and new Date(eIn) inside every iteration
            const s=new Date(sIn), e=new Date(eIn);
            e.setHours(23,59,59);
            if(d<s||d>e) return false;
        }
        return true;
    });
}

function fastFilter() {
    // HOISTED
    let s, e;
    if (sIn && eIn) {
        s = new Date(sIn);
        e = new Date(eIn);
        e.setHours(23, 59, 59);
    }

    return raw.filter(i => {
        if (sIn && eIn) {
            const d=i.gio_hu?new Date(i.gio_hu):new Date();
            // Using pre-calculated s and e
            if(d<s||d>e) return false;
        }
        return true;
    });
}

console.time("Slow Filter");
slowFilter();
console.timeEnd("Slow Filter");

console.time("Fast Filter");
fastFilter();
console.timeEnd("Fast Filter");
