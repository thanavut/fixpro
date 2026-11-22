#!/usr/bin/env python3
"""v109: ยกเลิกการ์ดสรุป dark 3D (v103/v104) ตามคำสั่งเจ้าของร้าน 'จัดการการ์ดสรุปด้วยยังสีดำอยู่'
- index.html: ลบบล็อก CSS v103/v104 ทั้งก้อน (L231-254 เดิม) + ลบป้าย stat-go 4 จุดใน renderDashboard
  → การ์ดสรุปกลับสไตล์ base v47/v102 (ขาว เลขเข้ม ชิปไอคอน 22px) ทุกจอ = เหมือน mobile ที่ใช้อยู่
- bump: APP_VERSION v109 + manifest?v=109 + CACHE fixpro-v109"""
base = '/home/z/my-project/fixpro/'

html = open(base + 'index.html', encoding='utf-8').read()
assert "APP_VERSION = 'v108'" in html and 'manifest.webmanifest?v=108' in html
assert 'stat-go' not in html, 'stat-go ยังตกค้าง!'
assert '1C1E22' not in html and 'เปิดดู<' not in html, 'CSS การ์ดดำ/ป้ายยังตกค้าง!'  # เปิดดูแล้ว (v82 ฟีเจอร์แจ้งเตือน) ไม่เกี่ยว
html = html.replace("APP_VERSION = 'v108'", "APP_VERSION = 'v109'")
html = html.replace('manifest.webmanifest?v=108', 'manifest.webmanifest?v=109')
open(base + 'index.html', 'w', encoding='utf-8').write(html)

sw = open(base + 'sw.js', encoding='utf-8').read()
assert "var CACHE = 'fixpro-v108';" in sw and "'./manifest.webmanifest?v=108'," in sw
sw = sw.replace("var CACHE = 'fixpro-v108';", "var CACHE = 'fixpro-v109';")
sw = sw.replace("'./manifest.webmanifest?v=108',", "'./manifest.webmanifest?v=109',")
sw = sw.replace('(v108: bump ตามรอบแคช — ยกเลิก UI กระจกทั้งหมดคืนหน้าตา v104 ตามคำสั่งเจ้าของร้าน "รูปแบบกระจกไม่เป็นที่น่าพอใจ ยกเลิกแก้กลับทั้งหมด อย่าให้กระทบส่วนอื่นๆ" — เลขเดินหน้ากันชนแคชเก่า)',
                '(v109: bump ตามรอบแคช — การ์ดสรุป dark 3D (v103/v104) ถูกยกเลิกกลับสไตล์ขาว base ทุกจอ ตามคำสั่งเจ้าของร้าน "จัดการการ์ดสรุปด้วยยังสีดำอยู่")')
open(base + 'sw.js', 'w', encoding='utf-8').write(sw)

h2 = open(base + 'index.html', encoding='utf-8').read()
s2 = open(base + 'sw.js', encoding='utf-8').read()
print('index: v109 =', "APP_VERSION = 'v109'" in h2, '| ?v=109 =', '?v=109' in h2,
      '| stat-go/1C1E22/เปิดดู< =', h2.count('stat-go') + h2.count('1C1E22') + h2.count('เปิดดู<'), '(ต้อง 0)')
print('sw.js: fixpro-v109 =', 'fixpro-v109' in s2, '| ?v=109 =', '?v=109' in s2, '| comment v109 =', 'v109: bump ตามรอบแคช' in s2)
