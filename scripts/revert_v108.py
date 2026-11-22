#!/usr/bin/env python3
"""v108: ยกเลิก UI กระจกทั้งหมด ตามคำสั่งเจ้าของร้าน 'รูปแบบกระจกไม่เป็นที่น่าพอใจ ยกเลิกแก้กลับทั้งหมด อย่าให้กระทบส่วนอื่นๆ'
คืน index.html + sw.js จาก tag backup-v104-glass-ui (สถานะก่อนทำกระจก v105 เป๊ะ ตามขั้นตอน backup ที่ทำไว้ก่อนแก้จริง)
แล้ว bump เวอร์ชันเป็น v108 (ไม่กลับไปใช้ fixpro-v104 เพราะกฎข้อ 4: ชื่อแคชต้องเดินหน้า กันชนกับแคชเก่าของเครื่องที่เคยใช้ v104)
ไฟล์อื่นทุกไฟล์ไม่แตะ — ฟีเจอร์/ข้อมูล/มือถือ = สถานะ v104 ที่เจ้าของร้านใช้อยู่ก่อนเริ่มกระจก"""
import subprocess, re

base = '/home/z/my-project/fixpro/'
TAG = 'backup-v104-glass-ui'

def show(path):
    return subprocess.run(['git', 'show', f'{TAG}:{path}'], capture_output=True, text=True, cwd=base).stdout

# --- index.html: v104 → เปลี่ยนเฉพาะเลขเวอร์ชันเป็น v108 (2 จุด) ---
html = show('index.html')
assert "APP_VERSION = 'v104'" in html and 'manifest.webmanifest?v=104' in html
assert 'glass-style' not in html  # ยืนยันว่าไฟล์ v104 ไม่มีบล็อกกระจก
html = html.replace("APP_VERSION = 'v104'", "APP_VERSION = 'v108'")
html = html.replace('manifest.webmanifest?v=104', 'manifest.webmanifest?v=108')
open(base + 'index.html', 'w', encoding='utf-8').write(html)

# --- sw.js: v104 → CACHE + manifest?v= เป็น v108 + บันทึกเหตุผลใน comment ---
sw = show('sw.js')
assert "var CACHE = 'fixpro-v104';" in sw and "'./manifest.webmanifest?v=104'," in sw
sw = sw.replace("var CACHE = 'fixpro-v104';", "var CACHE = 'fixpro-v108';")
sw = sw.replace("'./manifest.webmanifest?v=104',", "'./manifest.webmanifest?v=108',")
sw = re.sub(r'\(v104: bump ตามรอบแคช[^\)]*\)',
            '(v108: bump ตามรอบแคช — ยกเลิก UI กระจกทั้งหมดคืนหน้าตา v104 ตามคำสั่งเจ้าของร้าน "รูปแบบกระจกไม่เป็นที่น่าพอใจ ยกเลิกแก้กลับทั้งหมด อย่าให้กระทบส่วนอื่นๆ" — เลขเดินหน้ากันชนแคชเก่า)', sw)
open(base + 'sw.js', 'w', encoding='utf-8').write(sw)

# --- ตรวจผล ---
html2 = open(base + 'index.html', encoding='utf-8').read()
sw2 = open(base + 'sw.js', encoding='utf-8').read()
print('index.html: glass-style =', html2.count('glass-style'), '(ต้องเป็น 0)')
print('index.html: v108 markers =', "APP_VERSION = 'v108'" in html2, '?v=108' in html2)
print('sw.js: CACHE v108 =', "fixpro-v108" in sw2, '| manifest v108 =', '?v=108' in sw2)
# ไฟล์ที่คืนต้องต่างจาก tag เฉพาะเลขเวอร์ชันเท่านั้น
diff_html = subprocess.run(['git', 'diff', TAG, '--', 'index.html'], capture_output=True, text=True, cwd=base).stdout
lines = [l for l in diff_html.splitlines() if (l.startswith('+') or l.startswith('-')) and not l.startswith(('+++', '---'))]
print('index.html diff vs tag (บรรทัดที่เปลี่ยน):')
for l in lines: print('  ', l[:120])
diff_sw = subprocess.run(['git', 'diff', TAG, '--', 'sw.js'], capture_output=True, text=True, cwd=base).stdout
lines_sw = [l for l in diff_sw.splitlines() if (l.startswith('+') or l.startswith('-')) and not l.startswith(('+++', '---'))]
print('sw.js diff vs tag (บรรทัดที่เปลี่ยน):', len(lines_sw), 'บรรทัด — ควรเป็นแค่เลขเวอร์ชัน + comment')
