#!/usr/bin/env python3
"""handoff v114: บันทึกการลบเส้นแบ่ง + พื้นเข้มขึ้นอีกขั้น (ต้องรันบนสถานะ handoff v113)"""
p = '/home/z/my-project/fixpro/HANDOFF_FIXPRO.md'
t = open(p, encoding='utf-8').read()

# 1) หัวเอกสาร + สถานะ 0.1
assert 'production: **v113**' in t, 'เอกสารต้องอยู่สถานะ v113 ก่อน'
t = t.replace('production: **v113**', 'production: **v114**')
t = t.replace('- **งานถึง v113 เสร็จหมดแล้ว ไม่มีงานค้าง** — เวอร์ชันถัดไปที่ต้อง bump คือ **v114**',
              '- **งานถึง v114 เสร็จหมดแล้ว ไม่มีงานค้าง** — เวอร์ชันถัดไปที่ต้อง bump คือ **v115**')

# 2) สรุปรอบล่าสุด: แทรก v114 ก่อนหัว v113 และเปลี่ยนหัว v113 เป็น "รอบก่อนหน้า"
old_head = '- สรุปรอบล่าสุด: **v113 = พื้นหลังสีเดียวกันทั้งหมดบน desktop + เพิ่มความเข้ม**'
assert t.count(old_head) == 1
new_head = ('- สรุปรอบล่าสุด: **v114 = ลบเส้นแบ่ง + พื้นเข้มขึ้นอีกขั้น** ตามคำสั่งเจ้าของร้าน "ลบเส้นออก (ตามภาพ) แล้ว'
    'ทำพื้นหลังเข้มกว่านี้ให้การ์ดเด่น" — ลบ 3 เส้นที่ลอยบนพื้นเดียวกัน (scope desktop ≥1024 + light เท่านั้น): '
    'border-bottom แถบบน → transparent + box-shadow แถบบน → none + border-right แถบเมนูซ้าย → transparent '
    '(ขอบ/เงาการ์ดทุกใบคงเดิม — การ์ดเมนูยาวยังมีขอบ+เงา) — พื้นเข้มขึ้น #ECEFF5 → #E1E5EE (~11 จุด/ช่อง โทนเทา'
    'อมฟ้าเดิม) การ์ดขาวเด่นชัด — dark ไม่พัง (border rgba(45,49,72,.65) ของ dark header คงเดิม) — mobile เดิมเป๊ะ '
    '(body #F5F6FA + header border rgb(232,234,240) + เงาคงเดิม) — bump v114 3 จุด — ทดสอบ: node --check PASS + '
    'desktop 1280 computed (body rgb(225,229,238)/header_bb transparent/header_shadow none/sidebar_br transparent/'
    'การ์ดขอบ+เงาครบ/active gradient) + dark + collapsed + ภาพจริง + 0 error — prod ยืนยัน (curl v114/fixpro-v114/'
    'กฎ v114=1 + computed desktop/dark/mobile) — รอบก่อนหน้า: **v113 = พื้นหลังสีเดียวกันทั้งหมดบน desktop + เพิ่มความเข้ม**')
t = t.replace(old_head, new_head)

# 3) บรรทัดยืนยัน production (0.1 ท้าย) → v114
lines = t.split('\n')
hits = [i for i, l in enumerate(lines) if l.startswith('- ยืนยันบน production แล้ว (อ่านอย่างเดียว):')]
assert len(hits) == 1
lines[hits[0]] = ('- ยืนยันบน production แล้ว (อ่านอย่างเดียว): sw.js = fixpro-v114 + APP_VERSION v114 + desktop พื้นเดียว'
    'กัน #E1E5EE ไร้เส้นแบ่ง (computed: body rgb(225,229,238) + header_bb transparent + header_shadow none + '
    'sidebar_br transparent + การ์ดขาวขอบ/เงาครบ) + dark ไม่พัง (rgb(15,17,23)) + mobile เดิมเป๊ะ (rgb(245,246,250)/'
    'header border คงเดิม) + เมนูซ้ายการ์ดยาวขาว v111-v113 คงอยู่ + การ์ดสรุปขาว + CSP ใหม่ v102 คงอยู่ + ข้อมูลจริงครบ '
    '(8 ลูกค้า 12 งาน), ไฟล์นี้เปิดได้ที่ https://fixpro-7b397.web.app/HANDOFF_FIXPRO.md')
t = '\n'.join(lines)

# 4) ข้อ 8 ประวัติ: แทรก v114 บนสุด
anchor = '- v113: **พื้นหลังสีเดียวกันทั้งหมดบน desktop + เพิ่มความเข้ม**'
assert t.count(anchor) == 1
v114 = ('- v114: **ลบเส้นแบ่ง + พื้นเข้มขึ้นอีกขั้น** ตามคำสั่งเจ้าของร้าน "ลบเส้นออก (ตามภาพ) แล้วทำพื้นหลังเข้มกว่านี้ให้'
    'การ์ดเด่น" — เส้นใต้แถบบน (border+เงา) + เส้นขอบเมนูซ้าย = transparent / พื้น #ECEFF5 → #E1E5EE / ขอบการ์ดทุกใบ'
    'คงเดิม + bump v114 3 จุด — ทดสอบ: node --check PASS + desktop/dark/mobile computed + ภาพจริง + 0 error — '
    '**ยืนยัน production 2026-11-21 (อ่านอย่างเดียว): curl v114 ครบ + computed desktop ไร้เส้น/dark ไม่พัง/mobile '
    'เดิม** — สคริปต์ bump = scripts/v114_nolines_darker.py\n')
t = t.replace(anchor, v114 + anchor)

open(p, 'w', encoding='utf-8').write(t)
t2 = open(p, encoding='utf-8').read()
checks = {
    'งานถึง v114': '- **งานถึง v114 เสร็จหมดแล้ว' in t2,
    'สรุป v114': '- สรุปรอบล่าสุด: **v114 = ลบเส้นแบ่ง + พื้นเข้มขึ้นอีกขั้น**' in t2,
    'รอบก่อนหน้า v113': 'รอบก่อนหน้า: **v113 = พื้นหลังสีเดียวกันทั้งหมดบน desktop + เพิ่มความเข้ม**' in t2,
    'prod v114': 'production: **v114**' in t2,
    'ประวัติ v113 คงอยู่': '- v113: **พื้นหลังสีเดียวกันทั้งหมดบน desktop + เพิ่มความเข้ม**' in t2,
}
print(checks)
assert all(checks.values())
print('handoff v114 อัปเดตสำเร็จ')
