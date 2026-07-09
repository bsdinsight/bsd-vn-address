# bsd_vn_address — Địa giới hành chính VN (2025), dùng chung BSD

Module Odoo 19 Community **nền dùng chung** cho mọi sản phẩm BSD (Sapiones, Agrione,
Realty Pro, Parkone…). Cung cấp:

- Model **`frm.vn.ward`** — Phường/Xã (cải cách 2025: 34 tỉnh, 2 cấp, bỏ huyện).
  Core: `name`, `code`, `state_id` (→ `res.country.state`, domain VN), `active`.
- Nạp sẵn **~3321 phường/xã** khi cài (post_init, khớp 34 tỉnh của Odoo base, NFC + mã).
- Trường **`res.partner.vn_ward_id`** (địa chỉ cấp xã) — sản phẩm KHÔNG khai lại.

## Vì sao tên model là `frm.vn.ward`
Giữ theo Agrione — nơi model này đã cắm sâu ~15 model nghiệp vụ. Để làm nền dùng chung
mà không phải refactor Agrione, ta tách phần CORE ra đây; Agrione `frm_vn_address`
chỉ cần `depends: ['bsd_vn_address']` rồi `_inherit = 'frm.vn.ward'` thêm field nông học.

## Sản phẩm khác dùng thế nào
```python
# __manifest__.py
'depends': ['bsd_vn_address'],
# model
ward_id = fields.Many2one('frm.vn.ward', ...)
```
Sapiones: `l10n_vn_hr` trỏ `private_vn_ward_id → frm.vn.ward`; `l10n_vn_address` tan vào module này.

## Cài
`-i bsd_vn_address` (post_init tự nạp 3321 xã). Idempotent.
