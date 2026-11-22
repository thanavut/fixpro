#!/usr/bin/env python3
"""handoff v113: บันทึกการทำพื้นหลังสีเดียวกันทั้งหมดบน desktop + เพิ่มความเข้ม"""
p = '/home/z/my-project/fixpro/HANDOFF_FIXPRO.md'
t = open(p, encoding='utf-8').read()

# 1) หัวเอกสาร + สถานะ 0.1
assert 'production: **v112**' in t, 'เอกสารต้องอยู่สถานะ v112 ก่อน'
t = t.replace('production: **v112**', 'production: **v113**')
t = t.replace('- **งานถึง v112 เสร็จหมดแล้ว ไม่มีงานค้าง** — เวอร์ชันถัดไปที่ต้อง bump คือ **v113**',
              '- **งานถึง v113 เสร็จหมดแล้ว ไม่มีงานค้าง** — เวอร์ชันถัดไปที่ต้อง bump คือ **v114**')

# 2) สรุปรอบล่าสุด: แทรก v113 ก่อนหัว v112 และเปลี่ยนหัว v112 เป็น "รอบก่อนหน้า"
old_head = '- สรุปรอบล่าสุด: **v112 = การ์ดเมนูซ้าย desktop ยาวถึงด้านล่างเต็มความสูง**'
assert t.count(old_head) == 1
new_head = ('- สรุปรอบล่าสุด: **v113 = พื้นหลังสีเดียวกันทั้งหมดบน desktop + เพิ่มความเข้ม** ตามคำสั่งเจ้าของร้าน '
    '"เปลี่ยนสีพื้นหลังให้เหมือนกันทั้งหมด (เหมือนภาพที่ 3) และ เพิ่มความเข้มอีกเล็กน้อย" (แนบ 3 ภาพ: เมนูซ้าย/แถบบน/'
    'พื้นเนื้อหา = ตัวอ้างอิง) — พื้นแถบบน (เดิม frosted ขาว rgba(255,255,255,.72)+blur) + แถบเมนูซ้าย (เดิม '
    'var(--surface) ขาว) = สีเดียวกับพื้นเนื้อหา var(--bg) และเข้มขึ้น #F5F6FA → #ECEFF5 (โทนเทาอมฟ้าเดิม ~9 จุด/'
    'ช่อง) — scope html:not([data-theme="dark"]) + @media ≥1024px: **จำเป็น** เพราะตัวแปร dark อยู่บน <html> '
    '(documentElement) ถ้า override --bg ที่ body แบบไม่ scope จะทับ dark ทั้ง desktop — header คง frosted 0.72+blur '
    'แค่เปลี่ยนสี — dark ยืนยันไม่พัง (body rgb(15,17,23)/header rgba(26,29,38,.72)) — mobile เดิมเป๊ะ (body #F5F6FA/'
    'header ขาว/sidebar ขาว) — bump v113 3 จุด — ทดสอบ: node --check PASS + desktop 1280 computed (body/header/'
    'sidebar = #ECEFF5 ทั้ง 3, การ์ดขาว, active gradient คงเดิม) + dark ครบ + collapsed + ภาพจริง + 0 error — prod '
    'ยืนยัน (curl v113/fixpro-v113/กฎพื้นเดียวกัน=1 + computed desktop/dark/mobile) — รอบก่อนหน้า: '
    '**v112 = การ์ดเมนูซ้าย desktop ยาวถึงด้านล่างเต็มความสูง**')
t = t.replace(old_head, new_head)

# 3) บรรทัดยืนยัน production (0.1 ท้าย) → v113
lines = t.split('\n')
hits = [i for i, l in enumerate(lines) if l.startswith('- ยืนยันบน production แล้ว (อ่านอย่างเดียว):')]
assert len(hits) == 1
lines[hits[0]] = ('- ยืนยันบน production แล้ว (อ่านอย่างเดียว): sw.js = fixpro-v113 + APP_VERSION v113 + พื้นหลัง desktop '
    'สีเดียวกันทั้งหมด = #ECEFF5 (computed: body rgb(236,239,245) + header rgba(236,239,245,.72) + sidebar '
    'rgb(236,239,245)) + dark ไม่พัง (rgb(15,17,23)) + mobile เดิมเป๊ะ (rgb(245,246,250)/header ขาว) + เมนูซ้าย '
    'การ์ดยาวขาว v111/v112 คงอยู่ + การ์ดสรุปขาว + CSP ใหม่ v102 คงอยู่ + ข้อมูลจริงครบ (8 ลูกค้า 12 งาน), ไฟล์นี้เปิดได้ที่ '
    'https://fixpro-7b397.web.app/HANDOFF_FIXPRO.md')
t = '\n'.join(lines)

# 4) ข้อ 8 ประวัติ: แทรก v113 บนสุด
anchor = '- v112: **การ์ดเมนูซ้าย desktop ยาวถึงด้านล่างเต็มความสูง**'
assert t.count(anchor) == 1
v113 = ('- v113: **พื้นหลังสีเดียวกันทั้งหมดบน desktop + เพิ่มความเข้ม** ตามคำสั่งเจ้าของร้าน "เปลี่ยนสีพื้นหลังให้เหมือนกัน'
    'ทั้งหมด (เหมือนภาพที่ 3) และ เพิ่มความเข้มอีกเล็กน้อย" — แถบบน+เมนูซ้าย = สีเดียวกับพื้นเนื้อหา + #F5F6FA → #ECEFF5 '
    '+ scope html:not([data-theme=dark]) (ตัวแปร dark อยู่บน <html> ห้าม override body แบบไม่ scope) + bump v113 '
    '3 จุด — ทดสอบ: node --check PASS + desktop/dark/mobile computed + ภาพจริง + 0 error — **ยืนยัน production '
    '2026-11-21 (อ่านอย่างเดียว): curl v113 ครบ + computed desktop พื้นเดียวกัน/dark ไม่พัง/mobile เดิม** — สคริปต์ bump = '
    'scripts/v113_unified_bg.py\n')
t = t.replace(anchor, v113 + anchor)

open(p, 'w', encoding='utf-8').write(t)
t2 = open(p, encoding='utf-8').read()
checks = {
    'งานถึง v113': '- **งานถึง v113 เสร็จหมดแล้ว' in t2,
    'สรุป v113': '- สรุปรอบล่าสุด: **v113 = พื้นหลังสีเดียวกันทั้งหมดบน desktop + เพิ่มความเข้ม**' in t2,
    'รอบก่อนหน้า v112': 'รอบก่อนหน้า: **v112 = การ์ดเมนูซ้าย desktop ยาวถึงด้านล่างเต็มความสูง**' in t2,
    'prod v113': 'production: **v113**' in t2,
    'ประวัติ v112 คงอยู่': '- v112: **การ์ดเมนูซ้าย desktop ยาวถึงด้านล่างเต็มความสูง**' in t2,
}
print(checks)
assert all(checks.values())
print('handoff v113 อัปเดตสำเร็จ')
