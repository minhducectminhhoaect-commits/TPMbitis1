const iter = 50000;
const date = new Date();

console.log('Running benchmark...');

console.time('toLocaleString');
for(let i=0; i<iter; i++) {
    // Exact format used in index.html formatDate
    date.toLocaleString('vi-VN', {hour:'2-digit', minute:'2-digit', day:'2-digit', month:'2-digit'});
}
console.timeEnd('toLocaleString');

// Hoisted formatter
const fmt = new Intl.DateTimeFormat('vi-VN', {hour:'2-digit', minute:'2-digit', day:'2-digit', month:'2-digit'});
console.time('Intl.DateTimeFormat');
for(let i=0; i<iter; i++) {
    fmt.format(date);
}
console.timeEnd('Intl.DateTimeFormat');
