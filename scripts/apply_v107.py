#!/usr/bin/env python3
"""v107: แทนบล็อก <style id="glass-style"> ด้วยพาเลตที่วัดจากคลิปตัวอย่างจริง
+ bump v107 ครบ 3 จุด (APP_VERSION / manifest?v= / sw.js CACHE + comment)"""
import re

base = '/home/z/my-project/fixpro/'
html = open(base + 'index.html', encoding='utf-8').read()
css = open('/home/z/my-project/scripts/glass_v107.css', encoding='utf-8').read()

start = html.index('<style id="glass-style">') + len('<style id="glass-style">')
end = html.index('</style>', start)
old_block = html[start:end]
html = html[:start] + '\n' + css + html[end:]

# bump v106 -> v107 (3 จุดใน index.html + 2 จุดใน sw.js)
assert "APP_VERSION = 'v106'" in html
html = html.replace("APP_VERSION = 'v106'", "APP_VERSION = 'v107'")
assert 'manifest.webmanifest?v=106' in html
html = html.replace('manifest.webmanifest?v=106', 'manifest.webmanifest?v=107')

open(base + 'index.html', 'w', encoding='utf-8').write(html)

sw = open(base + 'sw.js', encoding='utf-8').read()
assert "fixpro-v106" in sw
sw = sw.replace("var CACHE = 'fixpro-v106';", "var CACHE = 'fixpro-v107';")
sw = sw.replace("'./manifest.webmanifest?v=106',", "'./manifest.webmanifest?v=107',")
# อัปเดตความหมาย comment แถว manifest (บันทึกสั้นๆ ว่า v107 คืออะไร)
sw = re.sub(r'\(v106: bump ตามรอบแคช[^\)]*\)', '(v107: bump ตามรอบแคช — เขียนพาเลต glass ใหม่จากสีที่วัดจากพิกเซลคลิปตัวอย่างจริง: พื้น navy-teal + การ์ด/เนื้อหาแก้วขาวเทาตัวหนังสือเข้ม + เมนูข้าง navy + active pill teal + การ์ดสรุปเลิกดำ)', sw)
open(base + 'sw.js', 'w', encoding='utf-8').write(sw)

# ตรวจผลลัพธ์
html2 = open(base + 'index.html', encoding='utf-8').read()
print('glass block len:', len(css), '(เดิม', len(old_block), ')')
print('v107 markers:', "APP_VERSION = 'v107'" in html2, '?v=107' in html2, 'color-scheme: light' in html2)
print('sw CACHE:', 'fixpro-v107' in open(base + 'sw.js', encoding='utf-8').read())
print('เขียวเก่าหลงเหลือ:', '#0B2014' in html2 or 'rgba(8,22,15' in html2)
