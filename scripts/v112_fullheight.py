#!/usr/bin/env python3
"""v112: การ์ดเมนูซ้าย desktop ยาวถึงด้านล่าง (คำสั่งเจ้าของร้าน 'แล้วด้านล่างเหลือไว้ทำไม ทำเป็นการ์ดยาวถึงด้านล่างไปเลย
แล้วพื้นหลังเป็นสีเดียวกัน') — sidebar flex column การ์ดยืดเต็มความสูง พื้นสีเดียวกัน — Desktop เท่านั้น อย่ายุ่ง Mobile เด็ดขาด — bump v112 3 จุด"""
base = '/home/z/my-project/fixpro/'

html = open(base + 'index.html', encoding='utf-8').read()
assert "APP_VERSION = 'v111'" in html and 'manifest.webmanifest?v=111' in html
assert 'v112: การ์ดยาวถึงล่าง' in html, 'กฎ v112 ยังไม่เข้าไฟล์'
assert '.mobile-nav { display: flex; flex-direction: column; }' in html
html = html.replace("APP_VERSION = 'v111'", "APP_VERSION = 'v112'")
html = html.replace('manifest.webmanifest?v=111', 'manifest.webmanifest?v=112')
open(base + 'index.html', 'w', encoding='utf-8').write(html)

sw = open(base + 'sw.js', encoding='utf-8').read()
assert "var CACHE = 'fixpro-v111';" in sw and "'./manifest.webmanifest?v=111'," in sw
sw = sw.replace("var CACHE = 'fixpro-v111';", "var CACHE = 'fixpro-v112';")
sw = sw.replace("'./manifest.webmanifest?v=111',", "'./manifest.webmanifest?v=112',")
sw = sw.replace('(v111: bump ตามรอบแคช — เมนูซ้าย desktop = การ์ดใหญ่ใบเดียวครอบเมนูทั้งหมด รายการข้างในเป็นแถวธรรมดา ตามคำชี้แจงเจ้าของร้าน "หมายถึงให้ทำเป็นการ์ดใหญ่แล้วมีเมนูอยู่ด้ายใน ไม่ใช่แยกการ์ดแต่ละเมนู")',
                '(v112: bump ตามรอบแคช — การ์ดเมนูซ้าย desktop ยาวถึงด้านล่างเต็มความสูง พื้นสีเดียวกัน ตามคำสั่งเจ้าของร้าน "แล้วด้านล่างเหลือไว้ทำไม ทำเป็นการ์ดยาวถึงด้านล่างไปเลย แล้วพื้นหลังเป็นสีเดียวกัน" — Desktop เท่านั้น อย่ายุ่ง Mobile เด็ดขาดถ้าผมไม่สั่ง)')
open(base + 'sw.js', 'w', encoding='utf-8').write(sw)

h2 = open(base + 'index.html', encoding='utf-8').read()
s2 = open(base + 'sw.js', encoding='utf-8').read()
print('index: v112 =', "APP_VERSION = 'v112'" in h2, '| ?v=112 =', '?v=112' in h2, '| flex sidebar =', '.mobile-nav { display: flex; flex-direction: column; }' in h2)
print('sw.js: fixpro-v112 =', 'fixpro-v112' in s2, '| ?v=112 =', '?v=112' in s2, '| comment v112 =', 'v112: bump ตามรอบแคช' in s2)
