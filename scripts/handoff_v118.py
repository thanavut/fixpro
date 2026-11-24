#!/usr/bin/env python3
"""handoff v118: บันทึกธีมที่ 3 Canopy (ต้องรันบนสถานะ handoff v117)"""
p = '/home/z/my-project/fixpro/HANDOFF_FIXPRO.md'
t = open(p, encoding='utf-8').read()

assert 'production: **v117**' in t, 'เอกสารต้องอยู่สถานะ v117 ก่อน'
t = t.replace('production: **v117**', 'production: **v118**')
t = t.replace('- **งานถึง v117 เสร็จหมดแล้ว ไม่มีงานค้าง** — เวอร์ชันถัดไปที่ต้อง bump คือ **v118**',
              '- **งานถึง v118 เสร็จหมดแล้ว ไม่มีงานค้าง** — เวอร์ชันถัดไปที่ต้อง bump คือ **v119**')

old_head = '- สรุปรอบล่าสุด: **v117 = ช่องระหว่างบรรทัดหน้างาน desktop เลิกเป็นสีขาว = สีพื้นเหมือนหน้าอื่น**'
assert t.count(old_head) == 1
new_head = ('- สรุปรอบล่าสุด: **v118 = ธีมที่ 3 "Canopy" หน้าตาแบบตัวอย่าง TikTok @settigation (CRM dashboard V10) เฉพาะ desktop** '
    'ตามคำสั่ง 4 ข้อ: ครบทุกหน้า / ไม่ทำโควต้า / กดสลับ 3 ธีม (สว่าง→มืด→canopy ไอคอน moon/sun/leaf + localStorage fixpro_theme) / '
    'ทำครั้งเดียวจบทั้งชุด + backup ก่อนเสมอ (git tag pre-v118-canopy + backups/fixpro_v117_pre_canopy/ + DB JSON 8 ลูกค้า 13 งาน '
    'ที่ backups/fixpro_localstorage_v118_pre_deploy.json) + ห้ามยุ่งโมบาย + font Kanit เดิม (ไม่แตะ font-family) — โครง: พื้นนอก'
    'เขียวเข้ม+แสงเขียวระยิบ → กรอบแอปลอยมุมโค้ง 24px → เมนูซ้ายเขียวเข้ม active แคปซูลขาว badge ส้ม → เนื้อหาพื้นเขียวเข้ม → '
    'การ์ด/ตาราง/ฟอร์มแก้วขาวโปร่ง blur → หัวเรื่องขาว → accent emerald #10B981 → hover ยกการ์ด — หน้าแรกโหมด canopy = ชุดใหม่: '
    'KPI 4 ใบ (รายได้เดือนนี้/งานเสร็จ/งานยังไม่เสร็จ/งานใหม่) sparkline SVG + chip %เทียบเดือนก่อน + Insight จากระบบแจ้งเตือนจริง + '
    'กราฟพื้นที่รายได้ 6 เดือน + โดนัทประเภทงาน — ทุกตัวเลขจาก DB จริง ไม่มีข้อมูลปลอม — ธีมสว่าง/มืด = เดิม 100% (ชุด canopy ซ่อน'
    'ด้วยกฎฐาน #canopy-dash + แสดงเฉพาะ html[data-theme="canopy"] + @media ≥1024px) — **บทเรียน 5 บั๊กที่วัดพบ**: (1) หน้าแรก '
    'desktop เดิม grid 2 คอลัมน์ 537×2px canopy-dash ตกครึ่งจอ → บังคับ 1 คอลัมน์เฉพาะ canopy (2) กฎ v114 ตั้ง --bg #E1E5EE บน '
    'body เงื่อนไข :not(dark) ทับตัวแปรธีมที่ตั้งบน html → ธีมใหม่ต้องประกาศ var บน body ซ้ำให้ชนะตามลำดับกฎ (3) .btn-secondary '
    'ถูกกฎ desktop L904 ทับเป็นพื้น var(--bg) → ในธีมพื้นเข้มปุ่มเข้มบนเข้ม (การ์ด Backup) → คืนค่า btn2 (4) ตัวเลข id ดิบ (t_...) '
    'ต้องแปลง typeLabel (5) ภาพหลัง toggle อาจจับกลาง pageIn animation (0.32s) ดูเหมือนสีปน — รอ 0.8s ค่อยถ่าย = จริงเสมอ — '
    'มือถือยืนยัน computed canopy = ค่า light เดิมทุกจุด — รอบก่อนหน้า: **v117 = ช่องระหว่างบรรทัดหน้างาน desktop เลิกเป็นสีขาว = '
    'สีพื้นเหมือนหน้าอื่น**')
t = t.replace(old_head, new_head)

lines = t.split('\n')
hits = [i for i, l in enumerate(lines) if l.startswith('- ยืนยันบน production แล้ว (อ่านอย่างเดียว):')]
assert len(hits) == 1
lines[hits[0]] = ('- ยืนยันบน production แล้ว (อ่านอย่างเดียว): sw.js = fixpro-v118 + APP_VERSION v118 + ธีม canopy ครบ (กรอบแอป '
    '24px/แสงเขียว/KPI 4 ใบ ฿5,040 จากข้อมูลจริง/insight/กราฟเส้น+โดนัท/แคปซูลขาว/leaf icon) + สลับครบวง canopy→light→dark→'
    'canopy + light = dash เดิม grid + --bg #E1E5EE + radius 0 + dark = --bg #0F1117 + radius 0 (ทั้งคู่ชุด canopy ซ่อน) + '
    'v113-v117 คงอยู่ + mobile prod = radius 0/body #F5F6FA/ชุด canopy ซ่อน/greeting เข้ม/header ขาว = เดิมเป๊ะ + CSP v102 '
    'คงอยู่ + ข้อมูลจริงครบ (8 ลูกค้า 13 งาน), ไฟล์นี้เปิดได้ที่ https://fixpro-7b397.web.app/HANDOFF_FIXPRO.md')
t = '\n'.join(lines)

anchor = '- v117: **ช่องระหว่างบรรทัดหน้างาน desktop เลิกเป็นสีขาว = สีพื้นเหมือนหน้าอื่น**'
assert t.count(anchor) == 1
v118 = ('- v118: **ธีมที่ 3 "Canopy" หน้าตาแบบตัวอย่าง TikTok @settigation เฉพาะ desktop** ตามคำสั่งเจ้าของร้าน 4 ข้อ (ครบทุกหน้า/'
    'ไม่ทำโควต้า/สลับ 3 ธีมได้/จบทั้งชุด) + backup ก่อนเสมอ (tag pre-v118-canopy + โฟลเดอร์ backup + DB JSON) + หน้าแรกโหมด '
    'canopy ชุดใหม่ KPI/insight/กราฟจาก DB จริง + แก้บั๊กวัดพบ 5 จุด (grid 2 คอลัมน์/var บน body ทับ/banner/btn-secondary/'
    'typeLabel) + font Kanit เดิม + bump v118 3 จุด — ทดสอบ: node --check PASS + ภาพจริง 4 หน้า + สลับธีมครบวง + light/dark/'
    'mobile ไม่เปลี่ยน + 0 error — **ยืนยัน production 2026-11-24 (อ่านอย่างเดียว): curl v118 ครบ + prod browser 3 ธีมครบ + '
    'mobile เดิมเป๊ะ** — สคริปต์ = scripts/v118_canopy_theme.py + handoff_v118.py\n')
t = t.replace(anchor, v118 + anchor)

open(p, 'w', encoding='utf-8').write(t)
t2 = open(p, encoding='utf-8').read()
checks = {
    'งานถึง v118': '- **งานถึง v118 เสร็จหมดแล้ว' in t2,
    'สรุป v118': '- สรุปรอบล่าสุด: **v118 = ธีมที่ 3 "Canopy"' in t2,
    'รอบก่อนหน้า v117': 'รอบก่อนหน้า: **v117 = ช่องระหว่างบรรทัดหน้างาน' in t2,
    'prod v118': 'production: **v118**' in t2,
    'ประวัติ v117 คงอยู่': '- v117: **ช่องระหว่างบรรทัดหน้างาน' in t2,
    'บทเรียน 5 บั๊ก': 'บทเรียน 5 บั๊กที่วัดพบ' in t2,
}
print(checks)
assert all(checks.values())
print('handoff v118 อัปเดตสำเร็จ')
