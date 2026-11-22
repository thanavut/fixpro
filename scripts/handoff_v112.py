#!/usr/bin/env python3
"""handoff v112: บันทึกการทำการ์ดเมนูซ้าย desktop ยาวถึงล่าง (ต้องรัน handoff_v111.py ก่อน)"""
p = '/home/z/my-project/fixpro/HANDOFF_FIXPRO.md'
t = open(p, encoding='utf-8').read()

# 1) หัวเอกสาร + สถานะ 0.1 (จากสถานะ v111 ที่ handoff_v111.py ทำไว้)
assert 'production: **v111**' in t, 'ต้องรัน handoff_v111.py ก่อน'
t = t.replace('production: **v111**', 'production: **v112**')
t = t.replace('- **งานถึง v111 เสร็จหมดแล้ว ไม่มีงานค้าง** — เวอร์ชันถัดไปที่ต้อง bump คือ **v112**',
              '- **งานถึง v112 เสร็จหมดแล้ว ไม่มีงานค้าง** — เวอร์ชันถัดไปที่ต้อง bump คือ **v113**')

# 2) สรุปรอบล่าสุด: แทรก v112 ก่อนหัว v111 และเปลี่ยนหัว v111 เป็น "รอบก่อนหน้า"
old_head = '- สรุปรอบล่าสุด: **v111 = เมนูซ้าย desktop เป็นการ์ดใหญ่ใบเดียวครอบเมนูทั้งหมด**'
assert t.count(old_head) == 1
new_head = ('- สรุปรอบล่าสุด: **v112 = การ์ดเมนูซ้าย desktop ยาวถึงด้านล่างเต็มความสูง** ตามคำสั่งเจ้าของร้าน "แล้วด้านล่าง'
    'เหลือไว้ทำไม ทำเป็นการ์ดยาวถึงด้านล่างไปเลย แล้วพื้นหลังเป็นสีเดียวกัน Desktop เท่านั้น อย่ายุ่ง Mobile เด็ดขาดถ้า'
    'ผมไม่สั่ง" (แนบภาพ 2 ใน: การ์ดจบที่ตั้งค่าแล้วเหลือพื้นขาวว่างใต้) — .mobile-nav (เฉพาะ @media ≥1024) = flex '
    'column + .mobile-nav-items flex:1 min-height:0 การ์ดยืดจากใต้ปุ่มย่อจนถึงล่าง (เหลือแค่ padding 10px ของ '
    'sidebar) — พื้นใต้รายการเมนู = var(--surface) สีเดียวกันทั้งการ์ด ไม่มีพื้นว่างนอกการ์ด — collapsed = การ์ดแคบ'
    'เต็มสูง — mobile ไม่แตะเลย (computed: flexDirection row / flexGrow 0 / ไม่มีขอบ / โปร่ง / radius 0 เหมือน '
    'baseline) — bump v112 3 จุด — ทดสอบ: node --check PASS + desktop 1280 computed (card_h 686/nav 740 '
    'bottom_gap 10 flex 1/1 active gradient คงเดิม) + ภาพจริง + collapsed + 0 error — prod ยืนยัน (curl '
    'v112/fixpro-v112/กฎการ์ดยาว=1 + computed desktop/mobile) — รอบก่อนหน้า: **v111 = เมนูซ้าย desktop เป็นการ์ดใหญ่ใบเดียวครอบเมนูทั้งหมด**')
t = t.replace(old_head, new_head)

# 3) บรรทัดยืนยัน production (0.1 ท้าย) → v112
lines = t.split('\n')
hits = [i for i, l in enumerate(lines) if l.startswith('- ยืนยันบน production แล้ว (อ่านอย่างเดียว):')]
assert len(hits) == 1
lines[hits[0]] = ('- ยืนยันบน production แล้ว (อ่านอย่างเดียว): sw.js = fixpro-v112 + APP_VERSION v112 + เมนูซ้าย desktop = '
    'การ์ดใหญ่ใบเดียวยาวถึงล่างเต็มความสูง (computed: flex column, การ์ดขาว radius 12px card_h 686/nav 740 '
    'bottom_gap 10, รายการโปร่ง, active แคปซูลเขียวไล่สี+แถบตั้งแบบเดิม) + การ์ดสรุปขาว + ธีมขาว v104/v109 คงอยู่ '
    '+ mobile เดิมเป๊ะ (flexDirection row/flexGrow 0/no border/radius 0) + CSP ใหม่ v102 คงอยู่ + ข้อมูลจริงครบ '
    '(8 ลูกค้า 12 งาน), ไฟล์นี้เปิดได้ที่ https://fixpro-7b397.web.app/HANDOFF_FIXPRO.md')
t = '\n'.join(lines)

# 4) ข้อ 8 ประวัติ: แทรก v112 บนสุด
anchor = '- v111: **เมนูซ้าย desktop = การ์ดใหญ่ใบเดียวครอบเมนูทั้งหมด**'
assert t.count(anchor) == 1
v112 = ('- v112: **การ์ดเมนูซ้าย desktop ยาวถึงด้านล่างเต็มความสูง** ตามคำสั่งเจ้าของร้าน "แล้วด้านล่างเหลือไว้ทำไม '
    'ทำเป็นการ์ดยาวถึงด้านล่างไปเลย แล้วพื้นหลังเป็นสีเดียวกัน" + ย้ำกฎเหล็ก "Desktop เท่านั้น อย่ายุ่ง Mobile เด็ดขาด'
    'ถ้าผมไม่สั่ง" — sidebar flex column + การ์ด flex:1 (พื้นสีเดียวกันทั้งคอลัมน์) + bump v112 3 จุด — ทดสอบ: '
    'node --check PASS + desktop/mobile computed + ภาพจริง + collapsed + 0 error — **ยืนยัน production '
    '2026-11-21 (อ่านอย่างเดียว): curl v112 ครบ + computed desktop การ์ดเต็มสูง/mobile เดิม + ภาพจริง** — '
    'สคริปต์ bump = scripts/v112_fullheight.py\n')
t = t.replace(anchor, v112 + anchor)

open(p, 'w', encoding='utf-8').write(t)
t2 = open(p, encoding='utf-8').read()
checks = {
    'งานถึง v112': '- **งานถึง v112 เสร็จหมดแล้ว' in t2,
    'สรุป v112': '- สรุปรอบล่าสุด: **v112 = การ์ดเมนูซ้าย desktop ยาวถึงด้านล่างเต็มความสูง**' in t2,
    'รอบก่อนหน้า v111': 'รอบก่อนหน้า: **v111 = เมนูซ้าย desktop เป็นการ์ดใหญ่ใบเดียวครอบเมนูทั้งหมด**' in t2,
    'prod v112': 'production: **v112**' in t2,
    'ประวัติ v111 คงอยู่': '- v111: **เมนูซ้าย desktop = การ์ดใหญ่ใบเดียวครอบเมนูทั้งหมด**' in t2,
    'กฎเด็ดขาด': 'อย่ายุ่ง Mobile เด็ดขาดถ้าผมไม่สั่ง' in t2,
}
print(checks)
assert all(checks.values())
print('handoff v112 อัปเดตสำเร็จ')
