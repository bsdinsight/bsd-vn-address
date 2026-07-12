# BSD – Đơn vị hành chính Việt Nam 2025 (`bsd_vn_address`)

Module nền **dùng chung** cho địa giới hành chính Việt Nam sau cải cách **2025**
(34 tỉnh/thành, 2 cấp Tỉnh → Phường/Xã, bỏ cấp huyện) trên **Odoo 19.0**.

[![License: LGPL-3](https://img.shields.io/badge/license-LGPL--3-blue.svg)](LICENSE)
![Odoo 19.0](https://img.shields.io/badge/Odoo-19.0-714B67.svg)

## Tính năng

- **`frm.vn.ward`** — danh mục Phường/Xã gắn với `res.country.state` (34 tỉnh sẵn có của Odoo), có tên + mã.
- **Tự nạp ~3.321 phường/xã** khi cài (`post_init_hook`), khớp tỉnh theo tên đã chuẩn hoá (NFC, bỏ tiền tố *Tỉnh/Thành phố*, xử lý bí danh *Huế ↔ Thừa Thiên - Huế*).
- **Idempotent** theo `(state_id, name)` — cài lại/nâng cấp không tạo trùng; **không** sửa `res.country.state`.
- **`res.partner.vn_ward_id`** — chọn Phường/Xã ngay trên form liên hệ.

## Cài đặt

```bash
# đặt thư mục module vào addons_path, rồi:
odoo -i bsd_vn_address -d <database>
```

Không cần module ngoài — **chỉ phụ thuộc `base`**.

## Dùng làm lớp nền cho module khác

```python
# __manifest__.py
'depends': ['bsd_vn_address'],

# models
ward_id = fields.Many2one('frm.vn.ward', string='Phường/Xã')
```

## Kỹ thuật

| | |
|---|---|
| Phiên bản Odoo | 19.0 (Community & Enterprise) |
| Phụ thuộc | `base` |
| Giấy phép | LGPL-3 |
| Model chính | `frm.vn.ward`, mở rộng `res.partner` |
| Dữ liệu | ~3.321 phường/xã (cập nhật 2025) |

## Giấy phép

LGPL-3 — xem [LICENSE](LICENSE).

---

Phát triển bởi **BSD** · [bsdinsight.com](https://bsdinsight.com)
