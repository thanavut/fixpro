#!/usr/bin/env python3
"""handoff v111: บันทึกการแก้เมนูซ้าย desktop เป็นการ์ดใหญ่ใบเดียว (ชี้แจงความเข้าใจ v110)"""
p = '/home/z/my-project/fixpro/HANDOFF_FIXPRO.md'
t = open(p, encoding='utf-8').read()

# 1) หัวเอกสาร + สถานะ 0.1
t = t.replace('production: **v110**', 'production: **v111**')
t = t.replace('- **งานถึง v110 เสร็จหมดแล้ว ไม่มีงานค้าง** — เวอร์ชันถัดไปที่ต้อง bump คือ **v111**',
              '- **งานถึง v111 เสร็จหมดแล้ว ไม่มีงานค้าง** — เวอร์ชันถัดไปที่ต้อง bump คือ **v112**')

# 2) สรุปรอบล่าสุด: แทรก v111 ก่อนหัว v110 และเปลี่ยนหัว v110 เป็น "รอบก่อนหน้า"
old_head = '- สรุปรอบล่าสุด: **v110 = เมนูซ้าย desktop ทำเป็นการ์ดขาว**'
assert t.count(old_head) == 1
new_head = ('- สรุปรอบล่าสุด: **v111 = เมนูซ้าย desktop เป็นการ์ดใหญ่ใบเดียวครอบเมนูทั้งหมด** ตามคำชี้แจงเจ้าของร้าน '
    '"หมายถึงให้ทำเป็นการ์ดใหญ่แล้วมีเมนูอยู่ด้ายใน ไม่ใช่แยกการ์ดแต่ละเมนู" (v110 แยกการ์ดรายการ = เข้าใจไม่ตรง) '
    '— ปรับบล็อก @media(min-width:1024px) เดิม: .mobile-nav-items = การ์ดใบเดียว (ขาว ขอบ var(--border) มุมมน 12px '
    'เงา var(--shadow-sm) padding 5px gap 2px) + ป้าย "เมนูหลัก" (::before) อยู่ในการ์ด + รายการข้างในกลับเป็นแถว'
    'ธรรมดาแบบเดิม (โปร่ง ไม่มีขอบ/เงา hover เทาอ่อน) + active กลับไปใช้แคปซูลเขียวไล่สี+แถบตั้งจากกฎ 6 เดิม '
    '(ไม่เขียนทับ — specificity .active ชนะกฎระดับรายการอยู่แล้ว) + คง nowrap กันชื่อ "แจ้งเตือน" ตก 2 บรรทัด '
    '— collapsed (v85): การ์ดแคบ ป้ายซ่อน (กฎ body.sidebar-collapsed ::before specificity สูงกว่าชนะเอง) '
    '— มือถือไม่กระทบ (เทียบ baseline: ไม่มีขอบ/โปร่ง/radius 0 เหมือนเดิมทุกค่า) — bump v111 3 จุด — ทดสอบ: '
    'node --check PASS + desktop 1280 computed (การ์ดขาว radius 12px เงานุ่ม / รายการโปร่ง / active gradient+'
    'inset bar คืน) + ภาพจริง + collapsed ครบ + 0 error — prod ยืนยัน (curl v111/fixpro-v111/กฎการ์ดใหญ่=1 + '
    'computed desktop/mobile) — รอบก่อนหน้า: **v110 = เมนูซ้าย desktop ทำเป็นการ์ดขาว**')
t = t.replace(old_head, new_head)

# 3) บรรทัดยืนยัน production (0.1 ท้าย) → v111
lines = t.split('\n')
hits = [i for i, l in enumerate(lines) if l.startswith('- ยืนยันบน production แล้ว (อ่านอย่างเดียว):')]
assert len(hits) == 1
lines[hits[0]] = ('- ยืนยันบน production แล้ว (อ่านอย่างเดียว): sw.js = fixpro-v111 + APP_VERSION v111 + เมนูซ้าย '
    'desktop = การ์ดใหญ่ใบเดียวครอบเมนู (computed: การ์ดขาว radius 12px เงานุ่ม, รายการโปร่งไม่มีขอบ, active '
    'แคปซูลเขียวไล่สี+แถบตั้งแบบเดิม) + การ์ดสรุปขาว + ธีมขาว v104/v109 คงอยู่ + mobile เดิมเป๊ะ (no border/'
    'transparent/radius 0) + CSP ใหม่ v102 คงอยู่ + ข้อมูลจริงครบ (8 ลูกค้า 12 งาน), ไฟล์นี้เปิดได้ที่ '
    'https://fixpro-7b397.web.app/HANDOFF_FIXPRO.md')
t = '\n'.join(lines)

# 4) ข้อ 8 ประวัติ: แทรก v111 บนสุด
anchor = '- v110: **เมนูซ้าย desktop ทำเป็นการ์ดขาว**'
assert t.count(anchor) == 1
v111 = ('- v111: **เมนูซ้าย desktop = การ์ดใหญ่ใบเดียวครอบเมนูทั้งหมด** ตามคำชี้แจงเจ้าของร้าน "หมายถึงให้ทำเป็นการ์ด'
    'ใหญ่แล้วมีเมนูอยู่ด้ายใน ไม่ใช่แยกการ์ดแต่ละเมนู" (แก้จาก v110 ที่แยกการ์ดรายการ) — container เป็นการ์ด รายการ'
    'ข้างในเป็นแถวธรรมดา active ใช้กฎ 6 เดิม + bump v111 3 จุด — ทดสอบ: node --check PASS + desktop/mobile '
    'computed + ภาพจริง + collapsed + 0 error — **ยืนยัน production 2026-11-21 (อ่านอย่างเดียว): curl v111 ครบ + '
    'computed desktop การ์ดใหญ่/mobile เดิม + ภาพจริง** — สคริปต์ bump = scripts/v111_bigcard.py\n')
t = t.replace(anchor, v111 + anchor)

open(p, 'w', encoding='utf-8').write(t)
t2 = open(p, encoding='utf-8').read()
checks = {
    'งานถึง v111': '- **งานถึง v111 เสร็จหมดแล้ว' in t2,
    'สรุป v111': '- สรุปรอบล่าสุด: **v111 = เมนูซ้าย desktop เป็นการ์ดใหญ่ใบเดียวครอบเมนูทั้งหมด**' in t2,
    'รอบก่อนหน้า v110': 'รอบก่อนหน้า: **v110 = เมนูซ้าย desktop ทำเป็นการ์ดขาว**' in t2,
    'prod v111': 'production: **v111**' in t2,
    'ประวัติ v110 คงอยู่': '- v110: **เมนูซ้าย desktop ทำเป็นการ์ดขาว**' in t2,
}
print(checks)
assert all(checks.values())
print('handoff v111 อัปเดตสำเร็จ')
