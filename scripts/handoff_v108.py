#!/usr/bin/env python3
"""handoff v108: บันทึกการยกเลิก UI กระจก + ย่อประวัติ v105-107 (ถูกยกเลิก) + กฎเหล็กห้ามทำกระจกซ้ำ
ใช้ anchor-based slicing (บรรทัดยาว ห้ามจับ old_string ทั้งก้อน)"""
import re

p = '/home/z/my-project/fixpro/HANDOFF_FIXPRO.md'
t = open(p, encoding='utf-8').read()

def replace_line(t, startswith, new_line):
    """แทนบรรทัดที่ขึ้นต้นด้วย startswith ทั้งบรรทัด"""
    lines = t.split('\n')
    hits = [i for i, l in enumerate(lines) if l.startswith(startswith)]
    assert len(hits) == 1, f'{startswith!r} → เจอ {len(hits)} บรรทัด'
    lines[hits[0]] = new_line
    return '\n'.join(lines)

# 1) หัวข้อ 0.1: งานถึง v108 เสร็จ
t = t.replace(
    '- **งานถึง v107 เสร็จหมดแล้ว ไม่มีงานค้าง** — เวอร์ชันถัดไปที่ต้อง bump คือ **v108**',
    '- **งานถึง v108 เสร็จหมดแล้ว ไม่มีงานค้าง** — เวอร์ชันถัดไปที่ต้อง bump คือ **v109**')

# 2) สรุปรอบล่าสุด L14: แทนทุกอย่างก่อนหน้า marker v104 ด้วย bullet v108 + ประวัติกระจกที่ถูกยกเลิก
marker = '— รอบก่อนหน้า: **v104 = การ์ด glass 3D แบบคลิป TikTok เหลือเฉพาะ Desktop'
assert t.count(marker) == 1
i = t.index(marker)
tail = t[i:]  # จาก marker ถึงจบบรรทัด (รวม v104/v103/v102/v100/v101 เดิมครบ)
new_prefix = (
    '- สรุปรอบล่าสุด: **v108 = ยกเลิก UI กระจกทั้งหมด** ตามคำสั่งเจ้าของร้าน "รูปแบบกระจกไม่เป็นที่น่าพอใจ '
    'ยกเลิกแก้กลับทั้งหมด อย่าให้กระทบส่วนอื่นๆ" — คืน index.html + sw.js จาก tag `backup-v104-glass-ui` '
    '(สถานะก่อนเริ่มทำกระจก v105 เป๊ะ — tag นี้ push ไว้บน GitHub ตั้งแต่ก่อนเริ่มกระจก ตามขั้นตอน backup ที่สั่งไว้ '
    '+ สำเนา /home/z/my-project/backup-v104/) แล้ว bump เป็น v108 (APP_VERSION + manifest?v=108 + CACHE fixpro-v108 '
    '— เลขเดินหน้ากันชนแคชเก่าของเครื่องที่เคยใช้ v104 ห้ามใช้ fixpro-v104 ซ้ำ) — ตรวจด้วย scripts/revert_v108.py '
    '(ใน repo): diff ไฟล์คืน vs tag = ต่างเฉพาะเลขเวอร์ชัน + บล็อก glass-style ถูกลบหมด (นับได้ 0) — ไฟล์/ฟีเจอร์/'
    'ข้อมูลอื่นทุกอย่าง = สถานะ v104 ก่อนเริ่มกระจก ไม่แตะ (desktop การ์ดสรุปกลับ dark 3D v103/v104, mobile = ขาวเดิม) '
    '— ทดสอบ: node --check PASS + desktop 1280px computed = พื้น #F5F6FA ทึบ/การ์ดขาว/หัวขาว frosted/การ์ดสรุป dark 3D เลขขาว '
    '+ mobile 390px เดิมเป๊ะ (พื้น #F5F6FA การ์ดขาว เลข #1A1D23 หัวขาว) + ภาพจริง desktop ตรง v104 + 0 error '
    '— prod ยืนยัน (curl v108/fixpro-v108/glass-style=0 + computed desktop/mobile + ภาพจริง) '
    '— รอบก่อนหน้า (v105-107 = ชุดทดลองกระจก ถูกยกเลิกทั้งหมดด้วย v108 เหลือไว้เพื่อบันทึก รายละเอียดเต็มในข้อ 8 + git log): '
    '**v107** = พาเลตกระจกเขียนใหม่จากสีที่วัดจากพิกเซลคลิปจริง (scripts/sample_ref_colors.py วัด 29 จุดจาก 19 เฟรม + '
    'ต้นฉบับ CSS scripts/glass_v107.css ใน repo) → เจ้าของร้านไม่พอใจรูปแบบกระจก; '
    '**v106** = ตรวจซ้ำกระจกแก้ไอคอนปฏิทิน/placeholder; '
    '**v105** = เริ่มทำ UI กระจกทุกหน้า desktop ตามคลิป "Admin Dashboard V2" (@paulcodes4) + ทำ backup tag ก่อนแก้ '
    '(ตามคำสั่ง "พิจารณาทำแอปทุกหน้าเป็น UI กระจกแบบนี้ได้ไหม Desktop เท่านั้นก่อนทำ backup ก่อนเสมอ") '
)
t = t[:i - len('— รอบก่อนหน้า: ')] if False else t
# ตัดข้อความเดิมทั้งหมดก่อน marker (รวม prefix เก่า) แล้วต่อด้วย new_prefix + tail
j = t.index('- สรุปรอบล่าสุด: **v107')
t = t[:j] + new_prefix + tail

# 3) บรรทัดยืนยัน production (0.1 ท้าย) → v108
t = replace_line(t, '- ยืนยันบน production แล้ว (อ่านอย่างเดียว):',
    '- ยืนยันบน production แล้ว (อ่านอย่างเดียว): sw.js = fixpro-v108 + APP_VERSION v108 + ไม่มีบล็อก glass-style '
    '(curl นับได้ 0) + desktop = ธีมขาว v104 (พื้น #F5F6FA ทึบ การ์ดขาว หัวขาว frosted การ์ดสรุป dark 3D เลขขาว '
    'ค่าจริง 1/0/7/4,540 — 21 พ.ย.) + mobile การ์ดขาวเลขดำเดิม (computed style ยืนยัน) + CSP ใหม่ v102 คงอยู่ + '
    'ข้อมูลจริงครบ (8 ลูกค้า 12 งาน), ไฟล์นี้เปิดได้ที่ https://fixpro-7b397.web.app/HANDOFF_FIXPRO.md')

# 4) กฎเหล็ก UI กระจก (ข้อ 5) → กฎยกเลิกกระจก v108
t = replace_line(t, '- **กฎ UI กระจกทุกหน้า (v105)',
    '- **กฎ UI กระจก (ยกเลิกแล้ว v108 — ห้ามทำซ้ำ)**: เจ้าของร้านปฏิเสธรูปแบบกระจก 2 รอบติด (v107 สั่งแก้โทน '
    '"ไม่เอากระจกสีเขียว...ทำให้ตรงกับตัวอย่าง" แล้วสั่ง "ยกเลิกแก้กลับทั้งหมด" ใน v108) — **ห้ามเสนอ/ทำ UI กระจก '
    '(glass morphism) กับแอปนี้อีกทุกรูปแบบ เว้นแต่เจ้าของร้านขอเองชัดๆ ในข้อความใหม่** — index.html ปัจจุบัน = '
    'สถานะ v104 ไม่มีบล็อก glass-style (ตรวจได้: grep glass-style index.html ต้องได้ 0) — จุด inline สีพาสเทล '
    '(การ์ดรอเก็บเงิน JS / กล่องแจ้งเตือนทุกปี / badge-*) ห้ามแก้ inline ต้นฉบับเพราะกระทบมือถือ — ถ้าจำเป็นต้อง '
    'ทับด้วย CSS เฉพาะจอ ให้ทำแบบ v103/v104 (บล็อก @media ที่ scope เฉพาะ element) ไม่ใช่ทับตัวแปร :root ทั้งธีม '
    '— เครื่องมือเก่าเก็บไว้ใน repo เป็นบันทึก: scripts/glass_v107.css + scripts/sample_ref_colors.py + '
    'scripts/apply_v107.py + scripts/revert_v108.py')

# 5) หัวเอกสาร: เวอร์ชันปัจจุบัน
t = t.replace('production: **v107**', 'production: **v108**')

# 6) ข้อ 8 ประวัติ: แทนก้อน v107/v106/v105 ด้วย v108 + ย่อ
i_start = t.index('- v107: **เขียนพาเลต glass ใหม่จากสีที่วัดจากพิกเซลคลิปตัวอย่างจริง**')
i_end = t.index('- v104: **การ์ด glass เหลือเฉพาะ Desktop')
hist = (
    '- v108: **ยกเลิก UI กระจกทั้งหมด** ตามคำสั่งเจ้าของร้าน "รูปแบบกระจกไม่เป็นที่น่าพอใจ ยกเลิกแก้กลับทั้งหมด '
    'อย่าให้กระทบส่วนอื่นๆ" — คืน index.html + sw.js จาก tag backup-v104-glass-ui + bump v108 3 จุด '
    '(diff vs tag = เฉพาะเลขเวอร์ชัน) — ทดสอบ: node --check PASS + desktop 1280px = ธีมขาว v104 ทุกค่า + mobile '
    '390px เดิมเป๊ะ + ภาพจริง + 0 error — **ยืนยัน production 2026-11-21 (อ่านอย่างเดียว): curl v108 ครบ + '
    'glass-style นับได้ 0 + computed desktop/mobile + ภาพจริงหน้าแรกตรง v104** — สคริปต์คืนไฟล์ = scripts/revert_v108.py\n'
    '- v107 (ยกเลิกแล้ว): พาเลตกระจกเขียนใหม่จากสีวัดพิกเซลคลิปจริง (29 จุด/19 เฟรม) — เจ้าของร้านไม่พอใจรูปแบบกระจก '
    'สั่งยกเลิกทาง v108 — เครื่องมือ/ต้นฉบับเก็บไว้: scripts/glass_v107.css, scripts/sample_ref_colors.py\n'
    '- v106 (ยกเลิกแล้ว): ตรวจซ้ำกระจก + แก้ไอคอนปฏิทิน/placeholder — ถูก v108 ลบพร้อมบล็อกกระจก\n'
    '- v105 (ยกเลิกแล้ว): เริ่ม UI กระจกทุกหน้า desktop ตามคลิป Admin Dashboard V2 + ทำ backup tag '
    'backup-v104-glass-ui ก่อนแก้ (ขั้นตอนนี้ทำให้ v108 ย้อนกลับได้ทันที) — ถูก v108 ลบพร้อมบล็อกกระจก\n'
)
t = t[:i_start] + hist + t[i_end:]

open(p, 'w', encoding='utf-8').write(t)

# ตรวจ
t2 = open(p, encoding='utf-8').read()
checks = {
    'งานถึง v108': '- **งานถึง v108 เสร็จหมดแล้ว' in t2,
    'สรุป v108': '- สรุปรอบล่าสุด: **v108 = ยกเลิก UI กระจกทั้งหมด**' in t2,
    'ประวัติ v104 คงอยู่': '- v104: **การ์ด glass เหลือเฉพาะ Desktop' in t2,
    'ประวัติ v102/v101 คงอยู่': '- v102: **แก้ของที่ audit' in t2 and '- v101:' in t2,
    'กฎห้ามกระจก': 'ห้ามเสนอ/ทำ UI กระจก' in t2,
    'prod v108': 'production: **v108**' in t2,
    'ไม่มี v107 สด (คงแค่ย่อ)': '- สรุปรอบล่าสุด: **v107' not in t2,
}
print(checks)
assert all(checks.values())
print('handoff v108 อัปเดตสำเร็จ')
