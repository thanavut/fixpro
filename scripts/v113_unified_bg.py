#!/usr/bin/env python3
"""v113: พื้นหลังสีเดียวกันทั้งหมดบน desktop (header+sidebar = สีเดียวกับเนื้อหา) + เพิ่มความเข้ม --bg #F5F6FA → #ECEFF5
ตามคำสั่งเจ้าของร้าน 'เปลี่ยนสีพื้นหลังให้เหมือนกันทั้งหมด (เหมือนภาพที่ 3) และ เพิ่มความเข้มอีกเล็กน้อย' — scope html:not([data-theme=dark])
กันทับตัวแปร dark บน <html> — bump v113 3 จุด"""
base = '/home/z/my-project/fixpro/'

html = open(base + 'index.html', encoding='utf-8').read()
assert "APP_VERSION = 'v112'" in html and 'manifest.webmanifest?v=112' in html
assert 'v113: พื้นหลังสีเดียวกันทั้งหมดบน desktop' in html, 'บล็อก v113 ยังไม่เข้าไฟล์'
assert 'html:not([data-theme="dark"]) body { --bg: #ECEFF5; }' in html
html = html.replace("APP_VERSION = 'v112'", "APP_VERSION = 'v113'")
html = html.replace('manifest.webmanifest?v=112', 'manifest.webmanifest?v=113')
open(base + 'index.html', 'w', encoding='utf-8').write(html)

sw = open(base + 'sw.js', encoding='utf-8').read()
assert "var CACHE = 'fixpro-v112';" in sw and "'./manifest.webmanifest?v=112'," in sw
sw = sw.replace("var CACHE = 'fixpro-v112';", "var CACHE = 'fixpro-v113';")
sw = sw.replace("'./manifest.webmanifest?v=112',", "'./manifest.webmanifest?v=113',")
sw = sw.replace('(v112: bump ตามรอบแคช — การ์ดเมนูซ้าย desktop ยาวถึงด้านล่างเต็มความสูง พื้นสีเดียวกัน ตามคำสั่งเจ้าของร้าน "แล้วด้านล่างเหลือไว้ทำไม ทำเป็นการ์ดยาวถึงด้านล่างไปเลย แล้วพื้นหลังเป็นสีเดียวกัน" — Desktop เท่านั้น อย่ายุ่ง Mobile เด็ดขาดถ้าผมไม่สั่ง)',
                '(v113: bump ตามรอบแคช — พื้นหลังสีเดียวกันทั้งหมดบน desktop (แถบบน+เมนูซ้าย = สีเดียวกับพื้นเนื้อหา) + เพิ่มความเข้ม #F5F6FA → #ECEFF5 ตามคำสั่งเจ้าของร้าน "เปลี่ยนสีพื้นหลังให้เหมือนกันทั้งหมด (เหมือนภาพที่ 3) และ เพิ่มความเข้มอีกเล็กน้อย" — scope html:not([data-theme=dark]) ธีมมืดไม่พัง — Desktop เท่านั้น อย่ายุ่ง Mobile เด็ดขาดถ้าผมไม่สั่ง)')
open(base + 'sw.js', 'w', encoding='utf-8').write(sw)

h2 = open(base + 'index.html', encoding='utf-8').read()
s2 = open(base + 'sw.js', encoding='utf-8').read()
print('index: v113 =', "APP_VERSION = 'v113'" in h2, '| ?v=113 =', '?v=113' in h2, '| scope dark =', 'html:not([data-theme="dark"]) body' in h2)
print('sw.js: fixpro-v113 =', 'fixpro-v113' in s2, '| ?v=113 =', '?v=113' in s2, '| comment v113 =', 'v113: bump ตามรอบแคช' in s2)
