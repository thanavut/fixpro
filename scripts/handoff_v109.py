#!/usr/bin/env python3
"""handoff v109: บันทึกการเลิกการ์ดสรุป dark 3D (ปิดงานชุดกระจกทั้งหมด)"""
p = '/home/z/my-project/fixpro/HANDOFF_FIXPRO.md'
t = open(p, encoding='utf-8').read()

# 1) หัวเอกสาร + สถานะ 0.1
t = t.replace('production: **v108**', 'production: **v109**')
t = t.replace('- **งานถึง v108 เสร็จหมดแล้ว ไม่มีงานค้าง** — เวอร์ชันถัดไปที่ต้อง bump คือ **v109**',
              '- **งานถึง v109 เสร็จหมดแล้ว ไม่มีงานค้าง** — เวอร์ชันถัดไปที่ต้อง bump คือ **v110**')

# 2) สรุปรอบล่าสุด: แทรก v109 และเปลี่ยนหัว v108 เป็น "รอบก่อนหน้า"
old_head = '- สรุปรอบล่าสุด: **v108 = ยกเลิก UI กระจกทั้งหมด**'
assert t.count(old_head) == 1
new_head = ('- สรุปรอบล่าสุด: **v109 = เลิกการ์ดสรุป dark 3D (v103/v104) กลับสไตล์ขาว base ก่อน v103 ทุกจอ** '
    'ตามคำสั่งเจ้าของร้าน "จัดการการ์ดสรุปด้วยยังสีดำอยู่" (แนบภาพหน้าจอ desktop มา) — ลบบล็อก CSS v103/v104 '
    'ทั้งก้อน (การ์ดดำ #1C1E22/glow/hover เอียง 3D/จุดสถานะ ::after บนชิป) + ลบป้าย "เปิดดู" (stat-go) 4 จุดใน '
    'renderDashboard HTML — การ์ดกลับเป็น: ขาว + ชิปไอคอน gradient 44px (desktop)/22px (mobile) + เลขเข้ม '
    '24px/15px + ลวดลายมุมสีจางเดิม (::before ของ base) — หน้างาน/แจ้งเตือน/รายงานใช้ .stat-card ต้นฉบับ '
    '(ไม่โดน scope #dash-stats) จึงไม่กระทบ + มือถือคงเดิมเป๊ะ — bump v109 3 จุด — ทดสอบ: node --check PASS + '
    'desktop 1280 computed = การ์ด rgb(255,255,255) ขอบ rgb(232,234,240) เลข rgb(26,29,35) 24px ชิป 44px '
    'transform none + mobile 390 เดิม + ภาพจริง + 0 error — prod ยืนยัน (curl v109/fixpro-v109/โค้ดการ์ดดำ '
    'นับได้ 0 + computed desktop/mobile + ภาพจริง) — รอบก่อนหน้า: **v108 = ยกเลิก UI กระจกทั้งหมด**')
t = t.replace(old_head, new_head)

# 3) บรรทัดยืนยัน production (0.1 ท้าย) → v109
lines = t.split('\n')
hits = [i for i, l in enumerate(lines) if l.startswith('- ยืนยันบน production แล้ว (อ่านอย่างเดียว):')]
assert len(hits) == 1
lines[hits[0]] = ('- ยืนยันบน production แล้ว (อ่านอย่างเดียว): sw.js = fixpro-v109 + APP_VERSION v109 + '
    'โค้ดการ์ดดำ/glass-style นับได้ 0 + desktop = ธีมขาว v104 และการ์ดสรุปขาว base (พื้น rgb(255,255,255) '
    'เลขเข้ม rgb(26,29,35) 24px ชิป gradient 44px ไม่มีป้าย/จุด/hover 3D — ค่าจริง 1/0/7/4,540) + mobile '
    'การ์ดขาวเลขดำเดิม (computed style ยืนยัน) + CSP ใหม่ v102 คงอยู่ + ข้อมูลจริงครบ (8 ลูกค้า 12 งาน), '
    'ไฟล์นี้เปิดได้ที่ https://fixpro-7b397.web.app/HANDOFF_FIXPRO.md')
t = '\n'.join(lines)

# 4) กฎเหล็ก (ข้อ 5): ครอบคลุมการ์ดดำ 3D ด้วย
lines = t.split('\n')
hits = [i for i, l in enumerate(lines) if l.startswith('- **กฎ UI กระจก (ยกเลิกแล้ว v108')]
assert len(hits) == 1
lines[hits[0]] = ('- **กฎ UI กระจก + การ์ดสรุป dark 3D (ยกเลิกแล้ว v109 — ห้ามทำซ้ำ)**: เจ้าของร้านปฏิเสธชุดทดลอง '
    'ตามคลิป 3 รอบติด — การ์ดสรุป dark 3D/Glassmorphism (v103/v104) ถูกยกเลิกด้วย v109 ("จัดการการ์ดสรุปด้วย'
    'ยังสีดำอยู่"), UI กระจกทุกหน้า (v105-107) ถูกยกเลิกด้วย v108 ("รูปแบบกระจกไม่เป็นที่น่าพอใจ ยกเลิกแก้กลับ'
    'ทั้งหมด อย่าให้กระทบส่วนอื่นๆ") — **ห้ามเสนอ/ทำ glass morphism หรือการ์ดสรุปพื้นเข้ม 3D กับแอปนี้อีกทุกรูปแบบ '
    'เว้นแต่เจ้าของร้านขอเองชัดๆ ในข้อความใหม่** — index.html ปัจจุบัน = สไตล์ base v47/v102 ล้วน (grep '
    'glass-style/1C1E22/stat-go ต้องได้ 0) — จุด inline สีพาสเทล (การ์ดรอเก็บเงิน JS / กล่องแจ้งเตือนทุกปี / '
    'badge-*) ห้ามแก้ inline ต้นฉบับเพราะกระทบมือถือ — ถ้าจำเป็นต้องทับด้วย CSS เฉพาะจอ ให้ scope เฉพาะ '
    'element (แบบ v103 ครั้งแรก) ไม่ใช่ทับตัวแปร :root ทั้งธีม — เครื่องมือเก่าเก็บไว้ใน repo เป็นบันทึก: '
    'scripts/glass_v107.css + scripts/sample_ref_colors.py + scripts/apply_v107.py + scripts/revert_v108.py + '
    'scripts/v109_statcards.py')
t = '\n'.join(lines)

# 5) ข้อ 8 ประวัติ: แทรก v109 บนสุด
anchor = '- v108: **ยกเลิก UI กระจกทั้งหมด**'
assert t.count(anchor) == 1
v109 = ('- v109: **เลิกการ์ดสรุป dark 3D กลับสไตล์ขาว base ก่อน v103 ทุกจอ** ตามคำสั่งเจ้าของร้าน "จัดการการ์ดสรุป'
    'ด้วยยังสีดำอยู่" (แนบภาพ desktop) — ลบบล็อก CSS v103/v104 ทั้งก้อน + ป้าย stat-go 4 จุดใน HTML + bump v109 '
    '3 จุด — ทดสอบ: node --check PASS + desktop/mobile computed + ภาพจริง + 0 error — **ยืนยัน production '
    '2026-11-21 (อ่านอย่างเดียว): curl v109 ครบ + โค้ดการ์ดดำนับได้ 0 + computed desktop (การ์ดขาว เลขเข้ม '
    '24px ชิป 44px)/mobile (15px/22px) + ภาพจริง** — สคริปต์ bump = scripts/v109_statcards.py\n')
t = t.replace(anchor, v109 + anchor)

open(p, 'w', encoding='utf-8').write(t)
t2 = open(p, encoding='utf-8').read()
checks = {
    'งานถึง v109': '- **งานถึง v109 เสร็จหมดแล้ว' in t2,
    'สรุป v109': '- สรุปรอบล่าสุด: **v109 = เลิกการ์ดสรุป dark 3D' in t2,
    'รอบก่อนหน้า v108': 'รอบก่อนหน้า: **v108 = ยกเลิก UI กระจกทั้งหมด**' in t2,
    'กฎครบการ์ดดำ': 'ห้ามเสนอ/ทำ glass morphism หรือการ์ดสรุปพื้นเข้ม 3D' in t2,
    'prod v109': 'production: **v109**' in t2,
    'ประวัติ v108 คงอยู่': '- v108: **ยกเลิก UI กระจกทั้งหมด**' in t2,
}
print(checks)
assert all(checks.values())
print('handoff v109 อัปเดตสำเร็จ')
