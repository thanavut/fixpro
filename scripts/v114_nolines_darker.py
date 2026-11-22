#!/usr/bin/env python3
"""v114: ลบเส้นแบ่งบน desktop (border-bottom+เงา header, border-right sidebar = transparent)
+ พื้นเข้มขึ้นอีกขั้น #ECEFF5 → #E1E5EE ให้การ์ดเด่น — ตามคำสั่งเจ้าของร้าน
'ลบเส้นออก (ตามภาพ) แล้วทำพื้นหลังเข้มกว่านี้ให้การ์ดเด่น' — scope desktop+light เท่านั้น — bump v114 3 จุด"""
base = '/home/z/my-project/fixpro/'

html = open(base + 'index.html', encoding='utf-8').read()
assert "APP_VERSION = 'v113'" in html and 'manifest.webmanifest?v=113' in html
assert 'v114: ตามคำสั่งเจ้าของร้าน "ลบเส้นออก' in html, 'กฎ v114 ยังไม่เข้าไฟล์'
assert '--bg: #E1E5EE' in html and 'border-bottom-color: transparent; box-shadow: none' in html and 'border-right-color: transparent' in html
html = html.replace("APP_VERSION = 'v113'", "APP_VERSION = 'v114'")
html = html.replace('manifest.webmanifest?v=113', 'manifest.webmanifest?v=114')
open(base + 'index.html', 'w', encoding='utf-8').write(html)

sw = open(base + 'sw.js', encoding='utf-8').read()
assert "var CACHE = 'fixpro-v113';" in sw and "'./manifest.webmanifest?v=113'," in sw
sw = sw.replace("var CACHE = 'fixpro-v113';", "var CACHE = 'fixpro-v114';")
sw = sw.replace("'./manifest.webmanifest?v=113',", "'./manifest.webmanifest?v=114',")
sw = sw.replace('(v113: bump ตามรอบแคช — พื้นหลังสีเดียวกันทั้งหมดบน desktop (แถบบน+เมนูซ้าย = สีเดียวกับพื้นเนื้อหา) + เพิ่มความเข้ม #F5F6FA → #ECEFF5 ตามคำสั่งเจ้าของร้าน "เปลี่ยนสีพื้นหลังให้เหมือนกันทั้งหมด (เหมือนภาพที่ 3) และ เพิ่มความเข้มอีกเล็กน้อย" — scope html:not([data-theme=dark]) ธีมมืดไม่พัง — Desktop เท่านั้น อย่ายุ่ง Mobile เด็ดขาดถ้าผมไม่สั่ง)',
                '(v114: bump ตามรอบแคช — ลบเส้นแบ่งบน desktop (เส้นใต้แถบบน+เงา+เส้นขอบเมนูซ้าย = transparent) + พื้นเข้มขึ้นอีกขั้น #ECEFF5 → #E1E5EE ให้การ์ดเด่น ตามคำสั่งเจ้าของร้าน "ลบเส้นออก (ตามภาพ) แล้วทำพื้นหลังเข้มกว่านี้ให้การ์ดเด่น" — scope html:not([data-theme=dark]) ธีมมืดไม่พัง — Desktop เท่านั้น อย่ายุ่ง Mobile เด็ดขาดถ้าผมไม่สั่ง)')
open(base + 'sw.js', 'w', encoding='utf-8').write(sw)

h2 = open(base + 'index.html', encoding='utf-8').read()
s2 = open(base + 'sw.js', encoding='utf-8').read()
print('index: v114 =', "APP_VERSION = 'v114'" in h2, '| ?v=114 =', '?v=114' in h2, '| E1E5EE =', '--bg: #E1E5EE' in h2)
print('sw.js: fixpro-v114 =', 'fixpro-v114' in s2, '| ?v=114 =', '?v=114' in s2, '| comment v114 =', 'v114: bump ตามรอบแคช' in s2)
