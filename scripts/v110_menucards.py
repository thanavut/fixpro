#!/usr/bin/env python3
"""v110: เมนูซ้าย desktop ทำเป็นการ์ดตามคำขอเจ้าของร้าน 'เมนูตรงนี้ทำเป็นการ์ดได้ไหม' (แนบภาพ sidebar)
แก้เฉพาะกฎในบล็อก @media desktop — มือถือ (แถบล่าง) ใช้กฎ base เดิมไม่กระทบ — bump v110 3 จุด"""
base = '/home/z/my-project/fixpro/'

html = open(base + 'index.html', encoding='utf-8').read()
assert "APP_VERSION = 'v109'" in html and 'manifest.webmanifest?v=109' in html
assert 'v110: รายการเมนู = การ์ดขาว' in html, 'กฎการ์ดเมนูยังไม่เข้าไฟล์'
html = html.replace("APP_VERSION = 'v109'", "APP_VERSION = 'v110'")
html = html.replace('manifest.webmanifest?v=109', 'manifest.webmanifest?v=110')
open(base + 'index.html', 'w', encoding='utf-8').write(html)

sw = open(base + 'sw.js', encoding='utf-8').read()
assert "var CACHE = 'fixpro-v109';" in sw and "'./manifest.webmanifest?v=109'," in sw
sw = sw.replace("var CACHE = 'fixpro-v109';", "var CACHE = 'fixpro-v110';")
sw = sw.replace("'./manifest.webmanifest?v=109',", "'./manifest.webmanifest?v=110',")
sw = sw.replace('(v109: bump ตามรอบแคช — การ์ดสรุป dark 3D (v103/v104) ถูกยกเลิกกลับสไตล์ขาว base ทุกจอ ตามคำสั่งเจ้าของร้าน "จัดการการ์ดสรุปด้วยยังสีดำอยู่")',
                '(v110: bump ตามรอบแคช — เมนูซ้าย desktop ทำเป็นการ์ดขาวแบบเดียวกับการ์ดอื่นในแอป ตามคำขอเจ้าของร้าน "เมนูตรงนี้ทำเป็นการ์ดได้ไหม" — แก้เฉพาะบล็อก desktop มือถือเดิมเป๊ะ)')
open(base + 'sw.js', 'w', encoding='utf-8').write(sw)

h2 = open(base + 'index.html', encoding='utf-8').read()
s2 = open(base + 'sw.js', encoding='utf-8').read()
print('index: v110 =', "APP_VERSION = 'v110'" in h2, '| ?v=110 =', '?v=110' in h2, '| การ์ดเมนู =', 'v110: รายการเมนู = การ์ดขาว' in h2)
print('sw.js: fixpro-v110 =', 'fixpro-v110' in s2, '| ?v=110 =', '?v=110' in s2, '| comment v110 =', 'v110: bump ตามรอบแคช' in s2)
