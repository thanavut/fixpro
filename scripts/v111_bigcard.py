#!/usr/bin/env python3
"""v111: เมนูซ้าย desktop = การ์ดใหญ่ใบเดียวครอบเมนูทั้งหมด (ชี้แจงเจ้าของร้าน 'หมายถึงให้ทำเป็นการ์ดใหญ่แล้วมีเมนูอยู่ด้ายใน
ไม่ใช่แยกการ์ดแต่ละเมนู') — ปรับบล็อก v110: container เป็นการ์ด / รายการข้างในเป็นแถวธรรมดา / active กลับไปใช้กฎ 6 เดิม — bump v111 3 จุด"""
base = '/home/z/my-project/fixpro/'

html = open(base + 'index.html', encoding='utf-8').read()
assert "APP_VERSION = 'v110'" in html and 'manifest.webmanifest?v=110' in html
assert 'v111: เมนูซ้าย desktop = การ์ดใหญ่ใบเดียว' in html, 'บล็อก v111 ยังไม่เข้าไฟล์'
assert 'v110: เมนูซ้าย desktop' not in html, 'คอมเมนต์ v110 เก่ายังตกค้าง'
html = html.replace("APP_VERSION = 'v110'", "APP_VERSION = 'v111'")
html = html.replace('manifest.webmanifest?v=110', 'manifest.webmanifest?v=111')
open(base + 'index.html', 'w', encoding='utf-8').write(html)

sw = open(base + 'sw.js', encoding='utf-8').read()
assert "var CACHE = 'fixpro-v110';" in sw and "'./manifest.webmanifest?v=110'," in sw
sw = sw.replace("var CACHE = 'fixpro-v110';", "var CACHE = 'fixpro-v111';")
sw = sw.replace("'./manifest.webmanifest?v=110',", "'./manifest.webmanifest?v=111',")
sw = sw.replace('(v110: bump ตามรอบแคช — เมนูซ้าย desktop ทำเป็นการ์ดขาวแบบเดียวกับการ์ดอื่นในแอป ตามคำขอเจ้าของร้าน "เมนูตรงนี้ทำเป็นการ์ดได้ไหม" — แก้เฉพาะบล็อก desktop มือถือเดิมเป๊ะ)',
                '(v111: bump ตามรอบแคช — เมนูซ้าย desktop = การ์ดใหญ่ใบเดียวครอบเมนูทั้งหมด รายการข้างในเป็นแถวธรรมดา ตามคำชี้แจงเจ้าของร้าน "หมายถึงให้ทำเป็นการ์ดใหญ่แล้วมีเมนูอยู่ด้ายใน ไม่ใช่แยกการ์ดแต่ละเมนู")')
open(base + 'sw.js', 'w', encoding='utf-8').write(sw)

h2 = open(base + 'index.html', encoding='utf-8').read()
s2 = open(base + 'sw.js', encoding='utf-8').read()
print('index: v111 =', "APP_VERSION = 'v111'" in h2, '| ?v=111 =', '?v=111' in h2, '| การ์ดใหญ่ =', 'v111: เมนูซ้าย desktop = การ์ดใหญ่ใบเดียว' in h2)
print('sw.js: fixpro-v111 =', 'fixpro-v111' in s2, '| ?v=111 =', '?v=111' in s2, '| comment v111 =', 'v111: bump ตามรอบแคช' in s2)
