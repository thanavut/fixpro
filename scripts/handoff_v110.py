#!/usr/bin/env python3
"""handoff v110: บันทึกการทำเมนูซ้าย desktop เป็นการ์ด"""
p = '/home/z/my-project/fixpro/HANDOFF_FIXPRO.md'
t = open(p, encoding='utf-8').read()

# 1) หัวเอกสาร + สถานะ 0.1
t = t.replace('production: **v109**', 'production: **v110**')
t = t.replace('- **งานถึง v109 เสร็จหมดแล้ว ไม่มีงานค้าง** — เวอร์ชันถัดไปที่ต้อง bump คือ **v110**',
              '- **งานถึง v110 เสร็จหมดแล้ว ไม่มีงานค้าง** — เวอร์ชันถัดไปที่ต้อง bump คือ **v111**')

# 2) สรุปรอบล่าสุด: แทรก v110 และเปลี่ยนหัว v109 เป็น "รอบก่อนหน้า"
old_head = '- สรุปรอบล่าสุด: **v109 = เลิกการ์ดสรุป dark 3D'
assert t.count(old_head) == 1
new_head = ('- สรุปรอบล่าสุด: **v110 = เมนูซ้าย desktop ทำเป็นการ์ดขาว** ตามคำขอเจ้าของร้าน "เมนูตรงนี้ทำเป็นการ์ดได้ไหม" '
    '(แนบภาพ sidebar มา) — รายการเมนู 6 รายการ = การ์ดขาว (พื้น var(--surface) ขอบ var(--border) เงา var(--shadow-sm) '
    'มุมมน 10px ห่างกัน 6px) + hover ขอบเขียวยกนิด + active = พื้นเขียวอ่อน var(--primary-bg) ขอบเขียว เงาเขียวนุ่ม '
    '(แทนแคปซูลไล่สี+แถบตั้งข้างเดิมกฎ "6) เมนูซ้ายเดสก์ท็อป") — จุดสำคัญ: กฎ active เดิมอยู่นอก @media (global) '
    'และมาทีหลังบล็อก desktop L706 จึงต้องวางบล็อกการ์ด @media(min-width:1024px) ใหม่ "หลัง" กฎเดิม (หลังกฎ 6) '
    'เพื่อชนะ cascade — รอบแรกวางในบล็อก L706 แล้วโดนทับ (เจอจาก computed: พื้นโปร่ง/เงา inset เขียวค้าง) — กันชื่อเมนู '
    'ตก 2 บรรทัด: white-space nowrap ที่ span + padding 8px 10px (แจ้งเตือนมีป้ายตัวเลข) — โหมดย่อเมนู (v85 '
    'sidebar-collapsed) = การ์ดไอคอนสี่เหลี่ยม 37x34 ในขอบ sidebar — มือถือไม่กระทบ (เทียบ computed กับ prod v109: '
    'transparent/none/none เหมือนเดิมทุกค่า — กฎ active เดิมไม่เคย render บนมือถืออยู่แล้ว) — bump v110 3 จุด '
    '— ทดสอบ: node --check PASS + desktop 1280 computed (การ์ดขาว rgb(255,255,255) ขอบ rgb(232,234,240) active '
    'rgb(232,245,233) ขอบเขียว gradient none) + label 1 line + ภาพจริง + collapsed ครบ + 0 error — prod ยืนยัน '
    '(curl v110/fixpro-v110/กฎการ์ด=1 + computed desktop/mobile + ภาพจริง) — รอบก่อนหน้า: **v109 = เลิกการ์ดสรุป dark 3D')
t = t.replace(old_head, new_head)

# 3) บรรทัดยืนยัน production (0.1 ท้าย) → v110
lines = t.split('\n')
hits = [i for i, l in enumerate(lines) if l.startswith('- ยืนยันบน production แล้ว (อ่านอย่างเดียว):')]
assert len(hits) == 1
lines[hits[0]] = ('- ยืนยันบน production แล้ว (อ่านอย่างเดียว): sw.js = fixpro-v110 + APP_VERSION v110 + เมนูซ้าย '
    'desktop เป็นการ์ดขาว (computed: การ์ด rgb(255,255,255) ขอบ rgb(232,234,240) ห่าง 6px, active rgb(232,245,233) '
    'ขอบเขียว ไม่มี gradient) + การ์ดสรุปขาว + ธีมขาว v104/v109 คงอยู่ + mobile เดิมเป๊ะ (transparent/no border/radius 0) '
    '+ CSP ใหม่ v102 คงอยู่ + ข้อมูลจริงครบ (8 ลูกค้า 12 งาน), ไฟล์นี้เปิดได้ที่ https://fixpro-7b397.web.app/HANDOFF_FIXPRO.md')
t = '\n'.join(lines)

# 4) ข้อ 8 ประวัติ: แทรก v110 บนสุด
anchor = '- v109: **เลิกการ์ดสรุป dark 3D'
assert t.count(anchor) == 1
v110 = ('- v110: **เมนูซ้าย desktop ทำเป็นการ์ดขาว** ตามคำขอเจ้าของร้าน "เมนูตรงนี้ทำเป็นการ์ดได้ไหม" (แนบภาพ) — '
    'การ์ดขาว 6 รายการ + active เขียวอ่อนขอบเขียว (แทนแคปซูลไล่สี) + บล็อกใหม่วางหลังกฎ active เดิมเพื่อชนะ cascade + '
    'nowrap กันชื่อตก 2 บรรทัด + collapsed = การ์ดไอคอน 37x34 + bump v110 3 จุด — ทดสอบ: node --check PASS + '
    'desktop/mobile computed + ภาพจริง + 0 error — **ยืนยัน production 2026-11-21 (อ่านอย่างเดียว): curl v110 ครบ + '
    'computed desktop การ์ดครบ/mobile เดิม + ภาพจริง** — สคริปต์ bump = scripts/v110_menucards.py\n')
t = t.replace(anchor, v110 + anchor)

open(p, 'w', encoding='utf-8').write(t)
t2 = open(p, encoding='utf-8').read()
checks = {
    'งานถึง v110': '- **งานถึง v110 เสร็จหมดแล้ว' in t2,
    'สรุป v110': '- สรุปรอบล่าสุด: **v110 = เมนูซ้าย desktop ทำเป็นการ์ดขาว**' in t2,
    'รอบก่อนหน้า v109': 'รอบก่อนหน้า: **v109 = เลิกการ์ดสรุป dark 3D' in t2,
    'prod v110': 'production: **v110**' in t2,
    'ประวัติ v109 คงอยู่': '- v109: **เลิกการ์ดสรุป dark 3D' in t2,
}
print(checks)
assert all(checks.values())
print('handoff v110 อัปเดตสำเร็จ')
