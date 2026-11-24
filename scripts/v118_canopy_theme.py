#!/usr/bin/env python3
"""v118: ธีมที่ 3 "Canopy" — หน้าตาแบบตัวอย่าง TikTok @settigation (CRM dashboard V10) เฉพาะ desktop ≥1024px
ตามคำสั่งเจ้าของร้าน: ข้อ 1 ทำครบทุกหน้า / ข้อ 2 ไม่ทำโควต้า / ข้อ 3 ธีมที่ 3 กดสลับได้ / ข้อ 4 ทำครั้งเดียวจบทั้งชุด
+ backup ก่อนเสมอ (git tag pre-v118-canopy + backups/fixpro_v117_pre_canopy/) + อย่ากระทบส่วนอื่น
+ ห้ามยุ่งโมบายเด็ดขาด (ทุกกฎ canopy ครอบ @media ≥1024px) + font เดิม Kanit (ไม่แตะ font-family)
— bump v118 3 จุด"""
import re
base = '/home/z/my-project/fixpro/'

html = open(base + 'index.html', encoding='utf-8').read()
assert "APP_VERSION = 'v117'" in html and 'manifest.webmanifest?v=117' in html
assert 'v118: ธีมที่ 3 "Canopy"' in html
assert "html[data-theme=\"canopy\"] .screen.active" in html
assert 'id="canopy-dash"' in html and 'function renderCanopyDashboard' in html
assert 'function setThemeIcon' in html and "order = ['light', 'dark', 'canopy']" in html
assert "renderCanopyDashboard(); // v118: หน้าแรกโหมด Canopy" in html
# กันพลาด: ทุกกฎ canopy ต้องอยู่ในบล็อก @media (min-width: 1024px) — นับ html[data-theme="canopy"] ต้องมีครอบ
_zone = html[html.find('v118: ธีมที่ 3 "Canopy"'):html.find('v118: ธีมที่ 3 "Canopy"') + 11000]
_pat = re.compile(r'font-family\s*:\s*[^;}]+|font-family=\\"[^\\"]+\\"|font-family="[^"]+"')
_bad_fonts = [f for f in _pat.findall(_zone) if 'Kanit' not in f]
assert not _bad_fonts, 'ห้ามใช้ฟอนต์อื่นในโซน v118 (font เดิม Kanit ตามสั่ง): %s' % _bad_fonts[:3]
html = html.replace("APP_VERSION = 'v117'", "APP_VERSION = 'v118'")
html = html.replace('manifest.webmanifest?v=117', 'manifest.webmanifest?v=118')
open(base + 'index.html', 'w', encoding='utf-8').write(html)

sw = open(base + 'sw.js', encoding='utf-8').read()
assert "var CACHE = 'fixpro-v117';" in sw and "'./manifest.webmanifest?v=117'," in sw
sw = sw.replace("var CACHE = 'fixpro-v117';", "var CACHE = 'fixpro-v118';")
sw = sw.replace("'./manifest.webmanifest?v=117',", "'./manifest.webmanifest?v=118',")
import re
m = re.search(r'\(v117: bump ตามรอบแคช[^)]*\)', sw)
assert m, 'หาคอมเมนต์ v117 ใน sw.js ไม่เจอ'
sw = sw.replace(m.group(0), "(v118: bump ตามรอบแคช — ธีมที่ 3 \"Canopy\" หน้าตาแบบตัวอย่าง TikTok @settigation เฉพาะ desktop ≥1024px (พื้นเขียวเข้ม+กรอบแอปลอยมุมโค้ง+เมนูซ้าย active แคปซูลขาว+การ์ดแก้วขาวโปร่ง+accent emerald+หน้าแรกชุดใหม่ KPI sparkline/insight/กราฟรายได้+โดนัทประเภทงาน จากข้อมูลจริง ไม่มีโควต้า) + สลับ 3 ธีม สว่าง→มืด→canopy + font Kanit เดิม ตามคำสั่งเจ้าของร้าน \"ทำให้ครบทุกหน้า/ไม่จำเป็นต้องมีโควต้า/ทำเป็นทีมที่ 3 สามารถกดสลับได้/ทำครั้งเดียวจบทั้งชุด...desktop version ห้ามยุ่งโมบายเวอร์ชั่นเด็ดขาด...font ใช้ font เดิมของเรา\")")
open(base + 'sw.js', 'w', encoding='utf-8').write(sw)

h2 = open(base + 'index.html', encoding='utf-8').read()
s2 = open(base + 'sw.js', encoding='utf-8').read()
print('index: v118 =', "APP_VERSION = 'v118'" in h2, '| ?v=118 =', '?v=118' in h2)
print('sw.js: fixpro-v118 =', 'fixpro-v118' in s2, '| ?v=118 =', '?v=118' in s2, '| comment v118 =', 'v118: bump ตามรอบแคช' in s2)
