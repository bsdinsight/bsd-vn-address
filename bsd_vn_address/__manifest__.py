# -*- coding: utf-8 -*-
{
    'name': 'BSD - Đơn vị hành chính VN (2025)',
    'version': '19.0.1.0.0',
    'category': 'Localization',
    'summary': 'Model dùng chung frm.vn.ward (Tỉnh/TP → Phường/Xã VN 2025) + nạp 3321 xã',
    'description': """
Địa giới hành chính Việt Nam 2025 — module NỀN dùng chung BSD
=============================================================

Cung cấp model **``frm.vn.ward``** (Phường/Xã, cải cách 2025: 34 tỉnh, 2 cấp, bỏ huyện)
làm nguồn địa giới DÙNG CHUNG cho mọi sản phẩm Odoo của BSD (Sapiones, Agrione,
Realty Pro, Parkone...). Tự nạp ~3321 phường/xã (NFC + mã) khi cài, khớp vào 34 tỉnh
có sẵn trong ``res.country.state``.

Cũng bổ sung trường **``res.partner.vn_ward_id``** (địa chỉ cấp xã) — các module sản phẩm
KHÔNG khai lại trường này, chỉ tham chiếu ``frm.vn.ward``.

Tên model ``frm.vn.ward`` giữ theo Agrione (đã cắm sâu 15 model) để không phải refactor;
các sản phẩm khác chỉ cần ``depends: ['bsd_vn_address']`` và trỏ Many2one tới ``frm.vn.ward``.

Phát triển bởi BSD — https://bsdinsight.com
""",
    'author': 'BSD',
    'website': 'https://bsdinsight.com',
    'license': 'LGPL-3',
    'images': ['static/description/cover.png'],
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/vn_ward_views.xml',
        'views/res_partner_views.xml',
    ],
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': False,
}
