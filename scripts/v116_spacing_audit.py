#!/usr/bin/env python3
"""v116: ตรวจระยะห่าง/ความสูงทุกหน้า desktop ให้ครบ — แก้ 4 ความต่าง:
(1) ช่องการ์ดสถิติ→ตารางหน้างาน 9px → 18px เท่าหน้าลูกค้า (#jobs-list-card margin-top 9px)
(2) หัวเรื่องหน้าแรก/รายงาน/ตั้งค่า สูงเกิน +12px (padding 6+6 กฎ sticky v71) → แผ่ padding เป็น 0
(3) รายงาน tabs→เนื้อหา 14px → mb 8px
(4) งาน bar→การ์ดสถิติ 9px → mb 7px (ช่องจริง 8px เท่าหน้าลูกค้า)
ตามคำสั่งเจ้าของร้าน 'ช่องระยะห่างบรรทัดตรงนี้ทำไมไม่มี (หน้าประวัติงาน) บางหน้าระยะแคบบางหน้าสูงไม่เท่ากันอีกตรวจสอบให้ครบ'
— bump v116 3 จุด"""
base = '/home/z/my-project/fixpro/'

html = open(base + 'index.html', encoding='utf-8').read()
assert "APP_VERSION = 'v115'" in html and 'manifest.webmanifest?v=115' in html
assert 'v116: ตรวจระยะห่าง/ความสูงทุกหน้าให้ครบ' in html, 'บล็อก v116 ยังไม่เข้าไฟล์'
assert '#jobs-list-card { margin-top: 9px; }' in html
assert '#page-jobs .filter-bar { margin-bottom: 7px; }' in html
assert '#page-reports .report-tabs { margin-bottom: 8px; }' in html
assert 'top: 0; z-index: 20; background: var(--bg); padding: 0 10px 0 0; margin: 0 -10px 0 0;' in html, 'กฎ sticky v71 ยังไม่ถูกแผ่ padding'
assert 'top: -6px; z-index: 20' not in html
html = html.replace("APP_VERSION = 'v115'", "APP_VERSION = 'v116'")
html = html.replace('manifest.webmanifest?v=115', 'manifest.webmanifest?v=116')
open(base + 'index.html', 'w', encoding='utf-8').write(html)

sw = open(base + 'sw.js', encoding='utf-8').read()
assert "var CACHE = 'fixpro-v115';" in sw and "'./manifest.webmanifest?v=115'," in sw
sw = sw.replace("var CACHE = 'fixpro-v115';", "var CACHE = 'fixpro-v116';")
sw = sw.replace("'./manifest.webmanifest?v=115',", "'./manifest.webmanifest?v=116',")
sw = sw.replace("(v115: bump ตามรอบแคช — จัดระยะห่างบรรทัดทุกหน้า desktop ให้เหมือนหน้า \"รายชื่อลูกค้า\" (หัวเรื่อง 10px → ช่องค้นหา/ตัวกรอง 8px) + ช่องค้นหาทุกหน้ายาว 460px เท่ากัน ตามคำสั่งเจ้าของร้าน \"รูปแบบระยะห่างของบรรทัดของทุกหน้าให้อิงตามภาพในหน้า 'รายชื่อลูกค้า' ความยาวของช่องค้นหาก็เหมือนกัน\" — Desktop เท่านั้น อย่ายุ่ง Mobile เด็ดขาดถ้าผมไม่สั่ง)",
                "(v116: bump ตามรอบแคช — ตรวจระยะห่าง/ความสูงทุกหน้าให้ครบ: ช่องการ์ดสถิติ→ตารางหน้างาน 9px → 18px เท่าหน้าลูกค้า + หัวเรื่องหน้าแรก/รายงาน/ตั้งค่าแผ่ padding sticky เหลือเท่าเนื้อหา (เท่ากันทุกหน้า) + tabs→เนื้อหารายงาน 8px ตามคำสั่งเจ้าของร้าน \"ช่องระยะห่างบรรทัดตรงนี้ทำwhyไม่มี (หน้าประวัติงาน) บางหน้าระยะแคบบางหน้าสูงไม่เท่ากันอีกตรวจสอบให้ครบ\" — Desktop เท่านั้น อย่ายุ่ง Mobile เด็ดขาดถ้าผมไม่สั่ง)".replace('ทำwhy', 'ทำไม'))
open(base + 'sw.js', 'w', encoding='utf-8').write(sw)

h2 = open(base + 'index.html', encoding='utf-8').read()
s2 = open(base + 'sw.js', encoding='utf-8').read()
print('index: v116 =', "APP_VERSION = 'v116'" in h2, '| ?v=116 =', '?v=116' in h2, '| sticky flatten =', 'padding: 0 10px 0 0; margin: 0 -10px 0 0;' in h2)
print('sw.js: fixpro-v116 =', 'fixpro-v116' in s2, '| ?v=116 =', '?v=116' in s2)
