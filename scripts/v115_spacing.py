#!/usr/bin/env python3
"""v115: จัดระยะห่างบรรทัดทุกหน้า desktop ให้เหมือนหน้า 'รายชื่อลูกค้า' (หัวเรื่อง 10px → ช่องค้นหา/ตัวกรอง 8px → เนื้อหา)
+ ช่องค้นหาทุกหน้ายาว 460px เท่ากัน — ตามคำสั่งเจ้าของร้าน 'รูปแบบระยะห่างของบรรทัดของทุกหน้าให้อิงตามภาพในหน้า
"รายชื่อลูกค้า" ความยาวของช่องค้นหาก็เหมือนกัน' — scope desktop ≥1024 เท่านั้น — bump v115 3 จุด"""
base = '/home/z/my-project/fixpro/'

html = open(base + 'index.html', encoding='utf-8').read()
assert "APP_VERSION = 'v114'" in html and 'manifest.webmanifest?v=114' in html
assert 'v115: จัดระยะห่างของบรรทัดทุกหน้า desktop' in html, 'บล็อก v115 ยังไม่เข้าไฟล์'
for rule in ['#page-jobs .filter-bar { margin-bottom: 8px; }',
             '#page-jobs .filter-bar .search-input { max-width: 460px; }',
             '#page-reminders > div:nth-child(2) { margin-bottom: 8px !important; }',
             '#page-reports .rpt-periods { margin-bottom: 8px; }',
             '#page-dashboard > div:first-child { margin-bottom: 10px !important; }']:
    assert rule in html, rule
html = html.replace("APP_VERSION = 'v114'", "APP_VERSION = 'v115'")
html = html.replace('manifest.webmanifest?v=114', 'manifest.webmanifest?v=115')
open(base + 'index.html', 'w', encoding='utf-8').write(html)

sw = open(base + 'sw.js', encoding='utf-8').read()
assert "var CACHE = 'fixpro-v114';" in sw and "'./manifest.webmanifest?v=114'," in sw
sw = sw.replace("var CACHE = 'fixpro-v114';", "var CACHE = 'fixpro-v115';")
sw = sw.replace("'./manifest.webmanifest?v=114',", "'./manifest.webmanifest?v=115',")
sw = sw.replace('(v114: bump ตามรอบแคช — ลบเส้นแบ่งบน desktop (เส้นใต้แถบบน+เงา+เส้นขอบเมนูซ้าย = transparent) + พื้นเข้มขึ้นอีกขั้น #ECEFF5 → #E1E5EE ให้การ์ดเด่น ตามคำสั่งเจ้าของร้าน "ลบเส้นออก (ตามภาพ) แล้วทำพื้นหลังเข้มกว่านี้ให้การ์ดเด่น" — scope html:not([data-theme=dark]) ธีมมืดไม่พัง — Desktop เท่านั้น อย่ายุ่ง Mobile เด็ดขาดถ้าผมไม่สั่ง)',
                '(v115: bump ตามรอบแคช — จัดระยะห่างบรรทัดทุกหน้า desktop ให้เหมือนหน้า "รายชื่อลูกค้า" (หัวเรื่อง 10px → ช่องค้นหา/ตัวกรอง 8px) + ช่องค้นหาทุกหน้ายาว 460px เท่ากัน ตามคำสั่งเจ้าของร้าน "รูปแบบระยะห่างของบรรทัดของทุกหน้าให้อิงตามภาพในหน้า \'รายชื่อลูกค้า\' ความยาวของช่องค้นหาก็เหมือนกัน" — Desktop เท่านั้น อย่ายุ่ง Mobile เด็ดขาดถ้าผมไม่สั่ง)')
open(base + 'sw.js', 'w', encoding='utf-8').write(sw)

h2 = open(base + 'index.html', encoding='utf-8').read()
s2 = open(base + 'sw.js', encoding='utf-8').read()
print('index: v115 =', "APP_VERSION = 'v115'" in h2, '| ?v=115 =', '?v=115' in h2, '| กฎครบ 5 =', all(r in h2 for r in ['#page-jobs .filter-bar { margin-bottom: 8px; }', '#page-jobs .filter-bar .search-input { max-width: 460px; }', '#page-reports .rpt-periods { margin-bottom: 8px; }']))
print('sw.js: fixpro-v115 =', 'fixpro-v115' in s2, '| ?v=115 =', '?v=115' in s2, '| comment v115 =', 'v115: bump ตามรอบแคช' in s2)
