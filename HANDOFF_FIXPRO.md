# HANDOFF — แอป FixPro ระบบจัดการงานช่าง (ไฟล์ส่งต่อระหว่างแชท — อยู่ใน repo นี้)

> ไฟล์นี้ commit ไว้ใน repo เพื่อให้ "ทุกแชท" อ่านได้เสมอ: clone repo นี้ (public, ไม่ต้องมี token ก็ clone ได้) หรือดึงจากเว็บจริงที่ `https://fixpro-7b397.web.app/HANDOFF_FIXPRO.md`
> ถ้าผู้ใช้ให้ทำงานต่อเรื่อง FixPro ให้อ่านไฟล์นี้ก่อนเริ่ม แล้วทำงานตามที่นี่ทุกข้อ
> ปรับปรุงล่าสุด: 2026-11-10 · เวอร์ชันปัจจุบันที่อยู่บน production: **v52**

## 0) จุดสำคัญที่สุดสำหรับแชทใหม่
- **แต่ละแชทมี workspace/เครื่องแยกกัน** — ไฟล์ในแชทเก่า (repo clone, token, เบราว์เซอร์ทดสอบ) ไม่ย้ายมาเอง แชทใหม่ต้องจัดของตัวเองใหม่ตามไฟล์นี้
- clone ได้ทันที: `git clone https://github.com/thanavut/fixpro.git` (repo public — โค้ดล่าสุด + git log ข้อความ commit ภาษาไทยละเอียดทุกเวอร์ชัน = ประวัติการแก้ครบ)
- **สิทธิ์ push**: ดูข้อ 3 — ทำ Device Flow เองในแชทของตัวเอง ห้ามขอ/ส่ง token ผ่านข้อความแชทเด็ดขาด

## 1) โปรเจกต์คืออะไร
- แอปจัดการงานช่าง FixPro (ลูกค้า / งานซ่อม / ค่าเดินทาง / ใบเสร็จ / LINE / รายงาน / แจ้งเตือน) UI ภาษาไทยทั้งหมด ติดตั้งเป็น PWA บนมือถือได้
- เจ้าของร้าน: บรรยุฐ พรหมทัศน์ (อีเมล thanavutp@gmail.com) — GitHub account: **thanavut**
- เข้าใช้จริง: https://fixpro-7b397.web.app
- โครงสร้าง: ไฟล์เดียว `index.html` (~3,880 บรรทัด: HTML+CSS+JS ทั้งหมด) + `sw.js` (offline cache) + manifest + icons + firestore.rules + `.github/workflows/deploy-firebase.yml`

## 2) วิธีทำงานกับเจ้าของร้าน (โปรโตคอลที่ใช้มาตลอด)
1. เจ้าของสั่งเป็นข้อ ๆ ภาษาไทยทางแชท (สั้น ตรงประเด็น)
2. แก้โค้ด → **bump เวอร์ชัน** (ข้อ 4) → ทดสอบในเบราว์เซอร์จริง (agent-browser, viewport มือถือ 390x844, เสิร์ฟ local ด้วย `python3 -m http.server 8846` ในโฟลเดอร์ repo)
3. commit ข้อความไทยละเอียด (เปลี่ยนอะไร + ผลทดสอบจริง) → push → รอ deploy → ทดสอบบน production → **รายงานกลับเป็นภาษาไทย** สรุปเป็นข้อ ๆ พร้อมผลทดสอบ และหมายเหตุ "ปิด-เปิดแอปใหม่เพื่อรับเวอร์ชันใหม่" เมื่อเหมาะสม

## 3) สิทธิ์ GitHub — ทำเองในแชทของตัวเองด้วย Device Flow (สำคัญ)
- โค้ดบน repo public → clone/ดึงไฟล์ไม่ต้องใช้ token แต่ **push ต้องมี token ของตัวเอง**
- **ห้าม**ให้ใครพิมพ์/วาง token ลงข้อความแชท และห้ามบันทึก token ที่ปรากฏในข้อความ — ตามนโยบายความปลอดภัย
- ขอสิทธิ์เองแบบ Device Flow: ใช้สคริปต์ใน repo นี้ `scripts/gh_device_poll.py` (CLIENT_ID = `178c6fc778ccc68e1d6a`, scope = `repo`) → ได้รหัส 8 หลักให้เจ้าของเปิด https://github.com/login/device แล้วกดยืนยันครั้งเดียว → ได้ token
- เก็บ token ใน workspace ของแชทตัวเอง เช่น `.secrets/gh_token.json` (chmod 600) แล้วตั้ง remote: `git remote set-url origin "https://thanavut:<token>@github.com/thanavut/fixpro.git"` (ถ้าต้องดู remote ให้ mask: `git remote -v | sed -E 's#https://[^@]+@#https://***@#'`)
- เช็ค token ใช้ได้ (แสดงเฉพาะ HTTP code): `curl -s -o /dev/null -w "%{http_code}" -H "Authorization: token $TOKEN" https://api.github.com/user` → 200 = ใช้ได้ (token แบบนี้ไม่มีวันหมดอายุถ้าไม่ถูก revoke)
- ห้าม: commit token/ค่า config ลง repo, พิมพ์ token ลงเอกสาร, ส่ง token ข้ามแชท

## 4) Deploy + การ bump เวอร์ชัน (จำเป็นทุกครั้งที่แก้โค้ดแอป)
- push เข้า main → GitHub Actions `.github/workflows/deploy-firebase.yml` → Firebase Hosting (โปรเจกต์ fixpro-7b397) ปกติ 40–90 วิ
- **ทุกเวอร์ชันต้องแก้ 2 จุดเสมอ**: `sw.js` → `var CACHE = 'fixpro-vNN'` และ `index.html` → `var APP_VERSION = 'vNN'` (SW เปลี่ยนชื่อ cache = บังคับทุกเครื่องโหลดโค้ดใหม่ตอนเปิดครั้งถัดไป + แท็บที่เปิดค้างจะ reload ตัวเองเอง)
- เช็คว่าขึ้นจริง: `curl -s "https://fixpro-7b397.web.app/sw.js?cb=$RANDOM" | grep -oE "fixpro-v[0-9]+"` ต้องขึ้นเวอร์ชันใหม่ (ถ้าค้าง ให้เช็ค Actions run บน GitHub)
- แก้เฉพาะไฟล์เอกสาร (เช่น HANDOFF_FIXPRO.md) = ไม่ต้อง bump เวอร์ชัน

## 5) กลไกโค้ดที่ต้องรู้ก่อนแก้
- ข้อมูล: `DB = { customers, jobs }` เก็บ localStorage + ซิงค์ Firestore อัตโนมัติ (collections: `customers` / `jobs` / `shop` = ตั้งค่า) — Firebase compat SDK แพ็กใน repo ที่ `firebase/` (ไม่พึ่ง gstatic)
- **ไม่มีระบบล็อกอิน** (ถอนออกแล้วตั้งแต่ v40) — เปิดแอปใช้ได้เลย เชื่อมคลาวด์เอง
- หน้าตั้งค่า: ทุกการ์ด (ข้อมูลร้าน/ช่าง, ประเภทงาน, Firebase, Cloudinary) **ล็อกเสมอ** กดปุ่มดินสอ "แก้ไข" รายการ์ดถึงแก้ได้; บันทึก = ซิงค์คลาวด์ทันที (`pushConfigToCloud` + cfgDirty แบบ per-field กันเขียนทับข้ามการ์ด); ยกเลิก = คืนค่าเดิม; ถ้า db ไม่พร้อมมี `cfgPushPending` ลองซ้ำเองทุก 15 วิ
- มาตรฐาน UI ที่เจ้าของกำหนด (v43–v46) — อย่าผิดมาตรฐานย้อนหลัง: ช่องล็อก = โปร่งใส **ไม่มีกรอบ** (`.card.locked .form-control`), ช่องค้นหาทุกหน้า สูง 38px ฟอนต์ 14px ไอคอน 14px, ลูกค้า+ประวัติงานเรียง **updatedAt ใหม่สุดขึ้นบน** (งานเก่าไม่มี updatedAt เทียบด้วย serviceDate), ฟอนต์ **Kanit ทั้งแอป** (`input,select,textarea,button { font-family: inherit; }` + body Kanit), แถวประเภทงาน (`.jt-row`) ไม่มีกรอบ, การ์ดประเภทงานมีปุ่ม บันทึก/ยกเลิก (`saveJobTypesCard` / `cancelJobTypesCard` คืนจาก `_jtSnapshot` แล้วยิงคลาวด์ด้วย)
- ค่าเดินทาง (v44): field `travel` ในงาน — ฟอร์มมี ยอดรวมเก็บเงิน = ค่าบริการ+ค่าเดินทาง, ใบเสร็จ/LINE/รายงาน/Excel รวม `travel` ทุกจุด (`jobTotal(j)`) งานเก่าไม่มี travel = 0
- PDF รายงาน: jsPDF + ฟอนต์ Kanit โหลดจาก `https://cdn.jsdelivr.net/gh/google/fonts@main/ofl/kanit/` (`loadThaiFontB64`, Kanit-Regular/Bold.ttf) — อย่ากลับไปใช้ helvetica กับข้อความไทย
- **Desktop version (v48)**: ทุกกฎเดสก์ท็อปอยู่ใน `<style id="desktop-style">` บล็อกแยกก่อน `</head>` ภายใน `@media (min-width: 1024px)` เท่านั้น — **จอ < 1024px เรนเดอร์จาก CSS เดิม 100% ห้ามยุ่งมือถือเด็ดขาด** โครงเดสก์ท็อป: CSS Grid บน `#app-screen.active` (header เต็มความกว้าง + เมนูซ้าย 238px ซึ่งใช้ nav เดิม DOM เดิมจัดใหม่ด้วย CSS ล้วน) + เนื้อหา max-width 1280px · หน้าแรก/รายงาน/ตั้งค่า/รายละเอียดลูกค้า ใช้ grid 2 คอลัมน์ · ลูกค้า/งาน รายการ 2 คอลัมน์ · โมดัลกลางจอ · ห้ามใส่กฎเดสก์ท็อปในบล็อก CSS เดิม และห้ามแตะ JS เดิมเพื่อเดสก์ท็อป
- **กติกาฟอนต์ (v52) — เจ้าของร้านสั่ง "ฟอนต์ต้องเป็น Kanit เท่านั้น"**: Kanit เป็น self-hosted แล้ว — ไฟล์ woff2 10 ไฟล์ (weights 400/500/600/700/800 × subsets thai/latin, รวม ~161 KB) อยู่ที่ `assets/fonts/kanit/`, @font-face อยู่ใน `<style id="kanit-fonts">` หัวไฟล์ index.html, SW precache ครบทุกไฟล์ (sw.js CORE) → เน็ตกระตุก/ออฟไลน์ก็เป็น Kanit 100% **ไม่มีทางแสดงฟอนต์ระบบ** — ห้ามเปลี่ยนฟอนต์ / ห้ามกลับไปใช้ Google Fonts CDN; ถ้าต้องใช้น้ำหนักใหม่ให้ครบ 3 ขั้น: เพิ่มไฟล์ woff2 + เพิ่ม @font-face (จำ unicode-range ของ Google) + เพิ่มใน sw.js CORE; ตรวจว่าแอปไม่พึ่งเว็บฟอนต์ภายนอก: performance resources ต้องไม่มี fonts.googleapis.com/fonts.gstatic.com เลย
- **กติกา UI ที่เจ้าของร้านยืนยันแล้ว (v51) — สำคัญที่สุด อย่าฝ่าฝืนย้อนหลัง**: มือถือ/แท็บเล็ต (< 1024px) = หน้าตาเดิม v47 **ทุกอย่าง** ห้ามยุ่ง (พาเลตเขียว Material เดิม, ไม่มีเอฟเฟกต์, โมดัล bottom-sheet และไม่มี grabber); เดสก์ท็อป (>= 1024px) = เก็บเลย์เอาต์ v48 + เอฟเฟกต์แนวร่วมสมัยไว้ครบ แต่ **"สีและฟอนต์" ต้องเป็นของเดิม** (พาเลตเขียว Material: primary #2E7D32 / #43A047 / #1B5E20, accent #FF7043, info #1976D2, amber #FFA000, danger #DC2626 + ชื่อแบรนด์สีทึบ Kanit ห้าม gradient text) — วิธีตรวจ: fingerprint computed style มือถือ 390x844 เทียบ checkout ของ v47 (866d1af) ต้อง = 0 ต่าง
- **Modern FX (v51)**: เอฟเฟกต์แนวร่วมสมัยทั้งหมดอยู่ใน 2 บล็อก `<style id="modern-style">` + `<style id="modern-style-2">` และ **ครอบด้วย @media (min-width: 1024px) ทั้งก้อน** — มือถือจึงไม่เห็นเอฟเฟกต์แม้แต่ตัวเดียว (ต่างจาก v49/v50 เดิมที่เอฟเฟกต์หลุดไปมือถือ) · เอฟเฟกต์เดสก์ท็อป: header/เมนูซ้าย glass blur (ธีมมืดใช้โทนพื้นเดิม #1A1D26), aurora `body::after` หายใจ 26 วิ (โทนเขียว/ฟ้าของพาเลตเดิม), ripple ปุ่ม `.btn::after` (ระวัง `.btn` overflow:hidden เฉพาะเดสก์ท็อป), stagger การ์ดสถิติ/ตั้งค่า `cardIn` (ห้ามใส่ลิสต์ที่ re-render ทุกคีย์ค้นหา), pulse ป้ายแดง/จุดแจ้งเตือน (สีแดง #DC2626/เหลือง #FFA000 เดิม, box-shadow เท่านั้น ห้ามแตะ transform ของ nav-badge), กราฟ `barGrow`, banner ไล่เฉดเขียวไหล, pageIn/modalIn/toast แก้ว, chip ไอคอนสถิติ gradient ย้อมพาเลตเดิม (เขียว #43A047→#2E7D32, ส้ม #FF7043, ฟ้า #1976D2, เหลือง #FFA000, แดง #DC2626), เมนูซ้าย active ไล่เฉดเขียว+แถบตั้ง inset, hover เมาส์ (ปุ่มหลักไล่เฉดเลื่อน/แสงวิ่งการ์ดสถิติ/รูปซูม) — **เอฟเฟกต์ใหม่ให้ใส่ในบล็อกนี้เท่านั้น และย้อมสีด้วยพาเลตเดิมเสมอ** · prefers-reduced-motion ครอบด้วยกฎ `* !important` ท้ายบล็อก modern-style · หมายเหตุ: ตัวแปร `--brand-grad` ของ v49 ถูกถอนแล้ว (ห้ามอ้างอิง), gradient text ชื่อแบรนด์ถูกยกเลิกตามคำสั่ง "ฟอนต์เหมือนเดิม"
- ประเภทงาน: `cfg.jobTypes` = ลิสต์ `{id,label,deleted,remindYearly}` ใช้ผ่าน `getJobTypes()` / `typeLabel(id)`; งานเก่าเก็บ `serviceType` เป็น id
- เวอร์ชันแสดงท้ายหน้าตั้งค่า (footer) ดึงจาก `APP_VERSION`
- SW แคช: ไฟล์ใน repo + CDN (cdnjs, fonts.googleapis, fonts.gstatic, cdn.jsdelivr) cache-first; หน้าเว็บหลัก network-first; googleapis/firestore ไม่แคช

## 6) กติกาทดสอบ — ห้ามพังข้อมูลจริงของร้าน
- Production มีข้อมูลจริง (ลูกค้า/งาน/ตั้งค่า) — **ห้ามสร้าง-ลบข้อมูลทดสอบบน production ทุกชนิด** (ลูกค้า งาน ประเภทงาน ค่าตั้งค่า)
- CRUD ทดสอบทำบน localhost เท่านั้น: `python3 -m http.server 8846` ในโฟลเดอร์ repo → เปิด http://localhost:8846/index.html
- เบราว์เซอร์ทดสอบของแต่ละแชทเริ่มใหม่หมด (localStorage ว่าง) — ทดสอบ UI ได้เลยโดยไม่ต้องมีคลาวด์; **ถ้าต้องทดสอบซิงค์คลาวด์** ให้กรอก Firebase config ของร้านลงการ์ด Firebase ในหน้าตั้งค่าของแอปทดสอบ (ขอค่าจากเจ้าของร้าน — Firebase web API key ไม่ใช่ความลับที่ซ่อนไม่ได้ ความปลอดภัยจริงอยู่ที่ Firestore rules แต่กรอกเฉพาะในแอปเท่านั้น ห้าม commit ลง repo)
- บน production ทำได้เฉพาะ: อ่าน DOM/computed style/screenshot และกระบวนการ net-zero (เช่น กดแก้ไข→ยกเลิกทันที = ค่าเดิม)
- ก่อน push ทุกครั้ง: ดึง script inline ใน index.html ออกมา `node --check` ทีละ block + ทดสอบตามฟีเจอร์ที่แก้บน localhost + เช็ค `agent-browser errors` = ต้องไม่มี error
- ประเภทงานจริงของร้านตอนนี้: ล้างแอร์, ล้างเครื่องซักผ้า, เครื่องใช้ไฟฟ้า, อื่นๆ — อย่าแตะ
- ทดสอบเสร็จ รอ deploy (ข้อ 4) แล้วทดสอบซ้ำบน https://fixpro-7b397.web.app ก่อนรายงาน

## 7) ไฟล์/โฟลเดอร์อื่นที่เกี่ยว
- `firestore.rules` — กฎ Firestore v20 (ไม่มี auth: เปิดเฉพาะ customers/jobs/shop ให้แอปเขียนได้ อื่นปิด)
- `assets/fontawesome/`, `icons/`, `firebase/` — แพ็กใน repo (SW แคช)
- `scripts/` — เครื่องมือที่เคยใช้ (รวม `gh_device_poll.py` = ขอสิทธิ์ GitHub, `poll_deploy_v42.py` = รอ deploy)
- `firebase.json` — hosting public "." + headers/CSP; เว้นแต่ไฟล์ ignore ไฟล์ใน repo จะถูกเสิร์ฟบนเว็บจริงด้วย (HANDOFF_FIXPRO.md ก็เลยเปิดได้ที่เว็บ)

## 8) ประวัติเวอร์ชันล่าสุด (บริบท)
- v40: ถอนระบบล็อกอิน + กู้คืนฉุกเฉินออกทั้งหมด + แข็งซิงค์ตั้งค่า (merge:true ห้าม null ทับ)
- v41: ซิงค์ตั้งค่าไม่หายแบบเงียบ — cfgPushPending ลองใหม่ทุก 15 วิ/online/boot
- v42: การ์ดตั้งค่าล็อกเสมอ + ปุ่มแก้ไขรายการ์ด + บันทึกยิงคลาวด์ทันที + dirty-key กันเขียนทับ
- v43: ช่องล็อก = ไม่มีพื้นหลัง (โปร่งใส) ตามมาตรฐานช่องประเภทงาน
- v44: เพิ่มค่าเดินทาง (travel) ทุกจุด + ยอดรวมเก็บเงิน + Excel/รายงาน/LINE/ใบเสร็จ
- v45: เรียงลูกค้า/ประวัติงานตาม updatedAt ใหม่สุดก่อน + ช่องค้นหามาตรฐานเดียว 38px/14px + ช่องล็อกไม่มีกรอบ
- v46: Kanit ทั้งแอป (UI + PDF), แถวประเภทงานไม่มีกรอบทั้งหมด, การ์ดประเภทงานมีปุ่ม บันทึก/ยกเลิก (ตัดปุ่ม "เสร็จ" ออก) — commit e471778
- v47: ปุ่ม "+ เพิ่มประเภทงาน" ย่อขนาดเท่าปุ่มอื่น (สูง 34px ฟอนต์ 12.5px แบบ btn-sm) และย้ายจากใต้รายการมาอยู่แถวเดียวกับปุ่ม บันทึก/ยกเลิก (card-actions; ยังซ่อนเมื่อการ์ดล็อกเหมือนเดิม) — commit 866d1af
- v48: Desktop version จอ ≥1024px — เมนูซ้าย + เนื้อหา 2 คอลัมน์ทุกหน้า + โมดัลกลางจอ + hover เมาส์ (ทำแบบ additive ใน style block ใหม่เท่านั้น มือถือ <1024px เหมือนเดิม 100%)
- v49: ยกโฉม UI ทั้งแอปแนวร่วมสมัย "Modern Indigo" ตามคำสั่งเจ้าของร้าน (โทนเดิมเขียวเปลี่ยนได้) — เปลี่ยนพาเลต :root/dark + ล้างสี hardcoded เขียว/นาวีทุกจุด (auth, brand icon, avatar, glow ปุ่ม/FAB/กราฟ, jt-iconbtn, meta theme-color, manifest) + เพิ่มบล็อกเอฟเฟกต์ modern-style 16 กลุ่ม (glass/gradient mesh/spring/pulse/pill/toast/modal/chips) — LINE ยังเขียวแบรนด์เดิม, มาตรฐาน v43-v48 ไม่ถูกแตะ
- v50: Modern FX ชุด 2 ตามคำสั่ง "ทำต่อ" — aurora body::after หายใจทั้งแอป + เมนูล่าง glass จริง + ripple CSS + grabber โมดัลมือถือ + stagger การ์ดสถิติ/ตั้งค่า + pulse ป้ายแดง/จุดแจ้งเตือน + กราฟโตขึ้น + banner ไล่เฉดไหล + desktop hover extras (ปุ่มเลื่อนไล่เฉด/แสงวิ่งการ์ด/รูปซูม) — บล็อก modern-style-2 แยกหลัง v49, มาตรฐานเจ้าของร้านไม่ถูกแตะ
- v52: ล็อกฟอนต์ Kanit ถาวรตามคำสั่งเจ้าของร้าน "ฟอนต์ต้องเป็น kanit เท่านั้น" — ตรวจ audit พบว่า CSS/JS/PDF ใช้ Kanit ครบอยู่แล้ว แต่ตัวไฟล์ฟอนต์ยังโหลดจาก fonts.googleapis.com จึงมีจุดเสี่ยงจริง: เน็ตกระตุก/โหลดไม่ทัน (font-display:swap) ตัวอักษรจะแสดงเป็นฟอนต์ระบบชั่วขณะหรือตลอดกาล → แก้ที่ต้นตอด้วยการ self-host: ดาวน์โหลด Kanit woff2 จาก Google Fonts (weights 400-800 × thai/latin เท่าที่แอปใช้จริง — ไม่มี italic/300 ในแอป, รวม 160.8 KB) เก็บใน `assets/fonts/kanit/`, แทน <link> Google Fonts ด้วย `<style id="kanit-fonts">` 10 @font-face (unicode-range/font-display:swap คงเดิมตาม Google), sw.js ถอด URL Google Fonts ออกจาก CDN list และเพิ่ม 10 ไฟล์ลง CORE precache — computed font-family ยังเป็น 'Kanit', sans-serif เท่าเดิม หน้าตาไม่เปลี่ยนแม้แต่พิกเซลเดียว + APP_VERSION v52 + SW cache fixpro-v52 + อัปเดต handoff (กติกาฟอนต์ v52) — ทดสอบจริง: มือถือ 390x844: computed font-family ของ body/header/ปุ่ม/ช่องกรอก = 'Kanit', sans-serif เท่าเดิมทุกจุด (หน้าตาไม่เปลี่ยนแม้แต่พิกเซลเดียว) + document.fonts.check 400/700/800 ผ่าน + request ไป fonts.googleapis.com/fonts.gstatic.com = 0 รายการ; เดสก์ท็อป 1440x900 สว่าง/มืด: Kanit ทุกจุด เลย์เอาต์ v48 + เอฟเฟกต์คงเดิมครบ; SW fixpro-v52 ลงทะเบียนสำเร็จ + แคชฟอนต์ครบ 10 ไฟล์; **ทดสอบออฟไลน์จริง: ตัดเน็ต (set offline) แล้วรีโหลด = Kanit 400/600/800 โหลดจากแคชครบ ยังเป็น Kanit 100% ไม่มีทางกลายเป็นฟอนต์ระบบ**; node --check sw.js ผ่าน, CSS brace balance ครบทุกบล็อก (kanit-fonts 10/10), ไม่มี console error ตอนออนไลน์ (error ช่วงเทสออฟไลน์ = Firestore เข้าเน็ตไม่ได้ตามธรรมชาติ ระบบรีทรายเองได้) (SW v52)
- v51: คืน UI ตามคำสั่งเจ้าของร้าน "มือถือห้ามยุ่งให้เหมือนเดิมทุกอย่าง / เดสก์ท็อปแก้สีกับฟอนต์ให้เหมือนเดิม" — (1) มือถือ (< 1024px) = เหมือน v47 100%: คืนพาเลต :root/dark เป็นเขียว Material เดิมทั้งหมด + คืนสี hardcoded ทุกจุดที่ v49 แตะ (auth gradient, ไอคอนแบรนด์/avatar กลับ navy-gradient เดิม, glow เขียว rgba(46,125,50,…), jt-iconbtn ฟ้า #1976D2, กราฟรายงาน, stCols, meta theme-color + manifest เขียว #2E7D32) + ครอบบล็อก modern-style/modern-style-2 ด้วย @media (min-width: 1024px) ทั้งก้อน + ถอน grabber โมดัลมือถือ — พิสูจน์ด้วย diff เทียบ 866d1af เหลือแค่บล็อกเดสก์ท็อปกับเลขเวอร์ชัน + fingerprint 390x844 สว่าง/มืด = 0 ต่าง (2) เดสก์ท็อป = เก็บเลย์เอาต์ v48 + เอฟเฟกต์ v49/v50 ครบ แต่ย้อมสีใหม่ด้วยพาเลตเดิมทุกจุด (glass/aurora/pulse/chip/hover) + คืนสี hardcoded ใน desktop-style ที่ v49 ทับ + **ถอน gradient text ชื่อแบรนด์ กลับเป็นสีทึบ var(--primary)** ตามคำสั่งฟอนต์เหมือนเดิม + ถอนตัวแปร --brand-grad — Kanit คงเดิมทั้งแอป (3) APP_VERSION v51 + SW cache fixpro-v51 + อัปเดต handoff หัวข้อ 5 — ทดสอบจริง: node --check ผ่าน, มือถือ 390x844 สว่าง+มืดเทียบ v47 ทุกค่า, โมดัลมือถือ bottom-sheet ไม่มี grabber, เดสก์ท็อป 1440x900 สว่าง+มืด เลย์เอาต์ grid 238px + auroraDrift/fabPulse/cardIn/barGrow/modalIn/ripple ยืนยัน computed style ทุกตัว, ไม่มี console error (SW v51)
- ไฟล์ handoff นี้ถูกเพิ่มเข้า repo เป็นครั้งแรกหลัง v46 — เว้นแต่มีเวอร์ชันใหม่กว่านี้ใน git log ให้เชื่อ git log
