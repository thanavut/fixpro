#!/usr/bin/env python3
"""v117: ช่องระหว่างบรรทัดหน้าประวัติงานบน desktop ยังเป็นสีขาว → เปลี่ยนเป็นสีพื้นเหมือนหน้าอื่น
ต้นเหตุ (ตรวจ computed): #jobs-list-card (.card กรอบรวม) ยังมีพื้นขาว+เส้น+เงาบน desktop
แต่ข้างในมี DIV.cust-table (การ์ดสมบูรณ์: พื้น/ขอบ/มุมมน/เงาตัวเอง) อยู่แล้ว = การ์ดซ้อนกรอบขาว
ช่อง 18px ระหว่างแถวการ์ดสถิติกับตารางจึงโชว์ขาวจากกรอบรวม ขณะที่หน้าลูกค้า .cust-table ลอยบนพื้นโดยตรง
→ ทำกรอบรวมโปร่งใสบน desktop เหมือนกฎมือถือ v91 (L254) เป๊ะ — ตารางยังสวยด้วย chrome ของ .cust-table เอง
ตรวจหน้าอื่นครบแล้ว (วัด computed): ลูกค้า/แจ้งเตือน/รายงาน/ตั้งค่า/หน้าแรก/รายละเอียดลูกค้า = การ์ดแยกใบลอยบนพื้นถูกต้อง
ไม่มี card-in-card ซ้อนกันทุกหน้า (สแกน .card .card = ไม่พบ) — bump v117 3 จุด"""
base = '/home/z/my-project/fixpro/'

html = open(base + 'index.html', encoding='utf-8').read()
assert "APP_VERSION = 'v116'" in html and 'manifest.webmanifest?v=116' in html
assert 'v117: ช่องระหว่างบรรทัดหน้างาน desktop' in html
assert '#jobs-list-card { background: transparent; border-color: transparent; box-shadow: none; margin-bottom: 0; }' in html
html = html.replace("APP_VERSION = 'v116'", "APP_VERSION = 'v117'")
html = html.replace('manifest.webmanifest?v=116', 'manifest.webmanifest?v=117')
open(base + 'index.html', 'w', encoding='utf-8').write(html)

sw = open(base + 'sw.js', encoding='utf-8').read()
assert "var CACHE = 'fixpro-v116';" in sw and "'./manifest.webmanifest?v=116'," in sw
sw = sw.replace("var CACHE = 'fixpro-v116';", "var CACHE = 'fixpro-v117';")
sw = sw.replace("'./manifest.webmanifest?v=116',", "'./manifest.webmanifest?v=117',")
import re
m = re.search(r'\(v116: bump ตามรอบแคช[^)]*\)', sw)
assert m, 'หาคอมเมนต์ v116 ใน sw.js ไม่เจอ'
sw = sw.replace(m.group(0), "(v117: bump ตามรอบแคช — ช่องระหว่างบรรทัดหน้าประวัติงาน desktop เลิกเป็นสีขาว = สีพื้นเหมือนหน้าอื่น (กรอบรวม #jobs-list-card โปร่งใสเหมือนกฎมือถือ v91 เพราะตาราง .cust-table ข้างในมีการ์ดของตัวเองอยู่แล้ว = เลิกการ์ดซ้อนกรอบขาว) ตามคำสั่งเจ้าของร้าน \"หน้า ประวัติงาน ระหว่างบรรทัดยังเป็นสีขาวเปลี่ยนเป็นสีพื้นเหมือนหน้าอื่น ตรวจสอบหน้าอื่นๆให้ละเอียดด้วย\" — ตรวจทุกหน้าแล้วไม่มีการ์ดซ้อนกรอบอื่น — Desktop เท่านั้น อย่ายุ่ง Mobile เด็ดขาดถ้าผมไม่สั่ง)")
open(base + 'sw.js', 'w', encoding='utf-8').write(sw)

h2 = open(base + 'index.html', encoding='utf-8').read()
s2 = open(base + 'sw.js', encoding='utf-8').read()
print('index: v117 =', "APP_VERSION = 'v117'" in h2, '| ?v=117 =', '?v=117' in h2)
print('sw.js: fixpro-v117 =', 'fixpro-v117' in s2, '| ?v=117 =', '?v=117' in s2, '| comment v117 =', 'v117: bump ตามรอบแคช' in s2)
