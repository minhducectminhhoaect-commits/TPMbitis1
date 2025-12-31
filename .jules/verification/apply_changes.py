
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add formatters
search_1 = """        let currentUser = null, refreshInterval = null, lastAlertCount = 0, lastMyJobCount = 0;
        const ticketCache = {};
        function cacheTicket(t) { ticketCache[t.id] = t; return t.id; }
        const beepSound = new Audio("data:audio/wav;base64,UklGRl9vT19XQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YU");
        const vsmMap = {"Hoàn chỉnh 1": "VSM 1", "Hoàn chỉnh 2": "VSM 2", "May 1": "VSM 1", "May 2": "VSM 1", "May 3": "VSM 1", "May 4": "VSM 1", "May 5": "VSM 2", "May 6": "VSM 2", "Dập 1": "VSM 1", "Dập 2": "VSM 2", "In lụa": "VSM 1", "Bế hình": "VSM 1", "Cán dán": "VSM 1", "Cắt trục": "VSM 1", "Ép dấu chân": "VSM 2", "Chuẩn bị đế": "VSM 2", "Bọc đế": "VSM 2", "Bán thành phẩm": "VSM 2", "Cắt nhiệt": "VSM 1", "Phát sinh": "Phát sinh"};"""

replace_1 = """        let currentUser = null, refreshInterval = null, lastAlertCount = 0, lastMyJobCount = 0;
        const ticketCache = {};
        function cacheTicket(t) { ticketCache[t.id] = t; return t.id; }
        const beepSound = new Audio("data:audio/wav;base64,UklGRl9vT19XQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YU");
        const vsmMap = {"Hoàn chỉnh 1": "VSM 1", "Hoàn chỉnh 2": "VSM 2", "May 1": "VSM 1", "May 2": "VSM 1", "May 3": "VSM 1", "May 4": "VSM 1", "May 5": "VSM 2", "May 6": "VSM 2", "Dập 1": "VSM 1", "Dập 2": "VSM 2", "In lụa": "VSM 1", "Bế hình": "VSM 1", "Cán dán": "VSM 1", "Cắt trục": "VSM 1", "Ép dấu chân": "VSM 2", "Chuẩn bị đế": "VSM 2", "Bọc đế": "VSM 2", "Bán thành phẩm": "VSM 2", "Cắt nhiệt": "VSM 1", "Phát sinh": "Phát sinh"};

        // Performance Optimization: Hoist DateTimeFormat to avoid recreating it in loops
        const dateTimeFmt = new Intl.DateTimeFormat('vi-VN', {hour:'2-digit', minute:'2-digit', day:'2-digit', month:'2-digit'});
        const dateTimeFullFmt = new Intl.DateTimeFormat('vi-VN'); // Default style
        const timeFmt = new Intl.DateTimeFormat('vi-VN', {hour:'2-digit', minute:'2-digit', second:'2-digit'});"""

# 2. Update loadLeaderOpen
search_2 = "new Date(i.gio_hu).toLocaleString()"
replace_2 = "dateTimeFullFmt.format(new Date(i.gio_hu))"

# 3. Update loadLeaderActionable
search_3 = "new Date(i.gio_xong).toLocaleString()"
replace_3 = "dateTimeFullFmt.format(new Date(i.gio_xong))"

search_4 = "new Date(i.gio_xong).toLocaleTimeString()"
replace_4 = "timeFmt.format(new Date(i.gio_xong))"

# 4. Update viewDetail
search_5 = "const fmt = (d) => d ? new Date(d).toLocaleString() : '---';"
replace_5 = "const fmt = (d) => d ? dateTimeFullFmt.format(new Date(d)) : '---';"

# 5. Update formatDate
search_6 = "function formatDate(s) { return s ? new Date(s).toLocaleString('vi-VN', {hour:'2-digit', minute:'2-digit', day:'2-digit', month:'2-digit'}) : ''; }"
replace_6 = "function formatDate(s) { return s ? dateTimeFmt.format(new Date(s)) : ''; }"

if search_1 in content:
    content = content.replace(search_1, replace_1)
else:
    print("Block 1 not found")

if search_2 in content:
    content = content.replace(search_2, replace_2)
else:
    print("Block 2 not found")

if search_3 in content:
    content = content.replace(search_3, replace_3)
else:
    print("Block 3 not found")

if search_4 in content:
    content = content.replace(search_4, replace_4)
else:
    print("Block 4 not found")

if search_5 in content:
    content = content.replace(search_5, replace_5)
else:
    print("Block 5 not found")

if search_6 in content:
    content = content.replace(search_6, replace_6)
else:
    print("Block 6 not found")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updates applied.")
