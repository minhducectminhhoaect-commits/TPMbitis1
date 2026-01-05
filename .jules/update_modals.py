
replacements = [
    (
        '<div id="modal-detail" class="card hidden" style="position:fixed; top:5%; left:5%; right:5%; z-index:200; max-height:90%; overflow-y:auto; border:2px solid #0056b3; box-shadow:0 10px 25px rgba(0,0,0,0.5);"><div class="header" style="border-bottom:1px solid #eee; padding-bottom:10px;"><h3 style="margin:0; color:#0056b3">Chi Tiết Phiếu</h3><button class="secondary" style="width:auto; padding:5px 10px" onclick="document.getElementById(\'modal-detail\').classList.add(\'hidden\')">X</button></div><div id="detail-content"></div><button onclick="document.getElementById(\'modal-detail\').classList.add(\'hidden\')" style="margin-top:15px;">Đóng</button></div>',
        '<div id="modal-detail" class="card hidden" role="dialog" aria-modal="true" aria-labelledby="title-detail" style="position:fixed; top:5%; left:5%; right:5%; z-index:200; max-height:90%; overflow-y:auto; border:2px solid #0056b3; box-shadow:0 10px 25px rgba(0,0,0,0.5);"><div class="header" style="border-bottom:1px solid #eee; padding-bottom:10px;"><h3 id="title-detail" style="margin:0; color:#0056b3">Chi Tiết Phiếu</h3><button class="secondary" aria-label="Đóng" style="width:auto; padding:5px 10px" onclick="document.getElementById(\'modal-detail\').classList.add(\'hidden\')">X</button></div><div id="detail-content"></div><button onclick="document.getElementById(\'modal-detail\').classList.add(\'hidden\')" aria-label="Đóng" style="margin-top:15px;">Đóng</button></div>'
    ),
    (
        '<div id="modal-history" class="card hidden" style="position:fixed; top:20px; left:10px; right:10px; bottom:20px; z-index:100; overflow-y:auto;"><div class="header"><h3>Lịch Sử</h3><button class="secondary" style="width:auto; padding:5px 10px" onclick="document.getElementById(\'modal-history\').classList.add(\'hidden\')">Đóng</button></div><div id="common-history-list">Đang tải...</div></div>',
        '<div id="modal-history" class="card hidden" role="dialog" aria-modal="true" aria-labelledby="title-history" style="position:fixed; top:20px; left:10px; right:10px; bottom:20px; z-index:100; overflow-y:auto;"><div class="header"><h3 id="title-history">Lịch Sử</h3><button class="secondary" aria-label="Đóng" style="width:auto; padding:5px 10px" onclick="document.getElementById(\'modal-history\').classList.add(\'hidden\')">Đóng</button></div><div id="common-history-list">Đang tải...</div></div>'
    ),
    (
        '<div id="modal-assign" class="card hidden" style="position:fixed; top:20px; left:20px; right:20px; z-index:99; border:2px solid #0056b3"><h3>Xác nhận Bảo Trì Đến</h3><input type="hidden" id="a-id"><input type="hidden" id="a-row"><p>Máy: <b id="a-msts"></b></p><label>Nhân Viên:</label><select id="a-tech"><option value="">-- Chọn Tên --</option><option value="Hoàng Đức Thuần">Hoàng Đức Thuần</option><option value="Bùi Thanh Hoàng">Bùi Thanh Hoàng</option><option value="Nguyễn Tuấn Khanh">Nguyễn Tuấn Khanh</option><option value="Nguyễn Văn Khanh">Nguyễn Văn Khanh</option><option value="Nguyễn Nhất Đẳng">Nguyễn Nhất Đẳng</option><option value="Phan Văn Hồ">Phan Văn Hồ</option><option value="Phạm Đắc Thụy">Phạm Đắc Thụy</option></select><label>Thời gian đến:</label><input type="datetime-local" id="a-time"><button onclick="leaderAssignSubmit()">Xác Nhận</button><button class="secondary" onclick="document.getElementById(\'modal-assign\').classList.add(\'hidden\')">Hủy</button></div>',
        '<div id="modal-assign" class="card hidden" role="dialog" aria-modal="true" aria-labelledby="title-assign" style="position:fixed; top:20px; left:20px; right:20px; z-index:99; border:2px solid #0056b3"><h3 id="title-assign">Xác nhận Bảo Trì Đến</h3><input type="hidden" id="a-id"><input type="hidden" id="a-row"><p>Máy: <b id="a-msts"></b></p><label>Nhân Viên:</label><select id="a-tech"><option value="">-- Chọn Tên --</option><option value="Hoàng Đức Thuần">Hoàng Đức Thuần</option><option value="Bùi Thanh Hoàng">Bùi Thanh Hoàng</option><option value="Nguyễn Tuấn Khanh">Nguyễn Tuấn Khanh</option><option value="Nguyễn Văn Khanh">Nguyễn Văn Khanh</option><option value="Nguyễn Nhất Đẳng">Nguyễn Nhất Đẳng</option><option value="Phan Văn Hồ">Phan Văn Hồ</option><option value="Phạm Đắc Thụy">Phạm Đắc Thụy</option></select><label>Thời gian đến:</label><input type="datetime-local" id="a-time"><button onclick="leaderAssignSubmit()">Xác Nhận</button><button class="secondary" aria-label="Đóng" onclick="document.getElementById(\'modal-assign\').classList.add(\'hidden\')">Hủy</button></div>'
    ),
    (
        '<div id="modal-finish" class="card hidden" style="position:fixed; top:20px; left:20px; right:20px; z-index:99; border:2px solid #28a745"><h3>Báo Cáo Sửa Xong</h3><input type="hidden" id="f-id"><input type="hidden" id="f-row"><p>Máy: <b id="f-msts"></b></p><label>Nhóm lỗi (Nhập tay):</label><input type="text" id="f-nhomloi" placeholder="VD: Cơ khí..."><label>Biện pháp:</label><textarea id="f-bienphap" rows="2"></textarea><label>Giờ sửa xong:</label><input type="datetime-local" id="f-time"><button style="background:#28a745" onclick="techFinishSubmit()">Gửi Báo Cáo</button><button class="secondary" onclick="document.getElementById(\'modal-finish\').classList.add(\'hidden\')">Hủy</button></div>',
        '<div id="modal-finish" class="card hidden" role="dialog" aria-modal="true" aria-labelledby="title-finish" style="position:fixed; top:20px; left:20px; right:20px; z-index:99; border:2px solid #28a745"><h3 id="title-finish">Báo Cáo Sửa Xong</h3><input type="hidden" id="f-id"><input type="hidden" id="f-row"><p>Máy: <b id="f-msts"></b></p><label>Nhóm lỗi (Nhập tay):</label><input type="text" id="f-nhomloi" placeholder="VD: Cơ khí..."><label>Biện pháp:</label><textarea id="f-bienphap" rows="2"></textarea><label>Giờ sửa xong:</label><input type="datetime-local" id="f-time"><button style="background:#28a745" onclick="techFinishSubmit()">Gửi Báo Cáo</button><button class="secondary" aria-label="Đóng" onclick="document.getElementById(\'modal-finish\').classList.add(\'hidden\')">Hủy</button></div>'
    ),
    (
        '<div id="modal-action" class="card hidden" style="position:fixed; top:20px; left:20px; right:20px; z-index:99; border:2px solid #17a2b8"><h3>Xử Lý Nghiệm Thu</h3><input type="hidden" id="c-id"><input type="hidden" id="c-row"><input type="hidden" id="c-type"><p>Máy: <b id="c-msts"></b></p><p id="c-status-text"></p><div id="swap-form" class="hidden"><div style="background:#fff3cd; padding:10px; border-radius:6px; margin-bottom:10px;"><label>Mã Máy Thay Thế:</label><input type="text" id="c-new-msts"><label>Giờ Chuyền Chạy Lại:</label><input type="datetime-local" id="c-time-swap"><button style="background:#ffc107; color:black" onclick="leaderSwapSubmit()">Xác Nhận Thay Máy</button></div></div><div id="confirm-form" class="hidden"><label>Giờ Chuyền Chạy Lại:</label><input type="datetime-local" id="c-time-confirm"><p style="font-size:11px;color:#666"><i>(Mặc định lấy giờ sửa xong)</i></p><button style="background:#28a745" onclick="leaderConfirmSubmit()">Nghiệm Thu (Done)</button></div><button class="secondary" onclick="document.getElementById(\'modal-action\').classList.add(\'hidden\')">Hủy</button></div>',
        '<div id="modal-action" class="card hidden" role="dialog" aria-modal="true" aria-labelledby="title-action" style="position:fixed; top:20px; left:20px; right:20px; z-index:99; border:2px solid #17a2b8"><h3 id="title-action">Xử Lý Nghiệm Thu</h3><input type="hidden" id="c-id"><input type="hidden" id="c-row"><input type="hidden" id="c-type"><p>Máy: <b id="c-msts"></b></p><p id="c-status-text"></p><div id="swap-form" class="hidden"><div style="background:#fff3cd; padding:10px; border-radius:6px; margin-bottom:10px;"><label>Mã Máy Thay Thế:</label><input type="text" id="c-new-msts"><label>Giờ Chuyền Chạy Lại:</label><input type="datetime-local" id="c-time-swap"><button style="background:#ffc107; color:black" onclick="leaderSwapSubmit()">Xác Nhận Thay Máy</button></div></div><div id="confirm-form" class="hidden"><label>Giờ Chuyền Chạy Lại:</label><input type="datetime-local" id="c-time-confirm"><p style="font-size:11px;color:#666"><i>(Mặc định lấy giờ sửa xong)</i></p><button style="background:#28a745" onclick="leaderConfirmSubmit()">Nghiệm Thu (Done)</button></div><button class="secondary" aria-label="Đóng" onclick="document.getElementById(\'modal-action\').classList.add(\'hidden\')">Hủy</button></div>'
    )
]

with open('index.html', 'rb') as f:
    content = f.read().decode('utf-8')

original_content = content
for search, replace in replacements:
    # We might need to handle slight whitespace differences if indentation is weird
    # But since we copied from read_file, it should match if indentation is stripped or matches.
    # The search strings above do NOT have indentation, but the file does.
    # So we need to match carefully.

    # Simple strategy: find the substring (ignoring indentation)
    if search in content:
        content = content.replace(search, replace)
    else:
        print(f"Could not find: {search[:50]}...")
        # Fallback: Try to find it with potential indentation?
        # Actually, let's just print what we see around where it should be.

if content == original_content:
    print("No changes made!")
else:
    with open('index.html', 'wb') as f:
        f.write(content.encode('utf-8'))
    print("Changes applied!")
