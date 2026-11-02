# 🔧 FixPro — ระบบจัดการงานช่าง

เว็บแอป (PWA) สำหรับช่างรับซ่อม/บริการ ใช้จัดการลูกค้า งานซ่อม นัดหมายบำรุงรักษา รายงานรายได้ และส่งใบเสร็จ/แจ้งเตือนผู้ใช้ผ่าน LINE — ใช้งานได้ทั้งบนมือถือและคอม ทำงานได้แม้ไม่มีอินเทอร์เน็ต

**เว็บไซต์:** https://thanavut.github.io/fixpro/

## ✨ ฟีเจอร์

- 📇 **ลูกค้า** — เพิ่ม/แก้ไข/ลบ พร้อมที่อยู่ Line ID และหมายเหตุ ค้นหาตามชื่อ/เบอร์
- 🔧 **งานซ่อม** — บันทึกงานแยกตามประเภท (ล้างแอร์ / ล้างเครื่องซักผ้า / ซ่อมไฟฟ้า / อื่นๆ) พร้อมรูปถ่ายงาน ค่าบริการ และสถานะ
- 🔔 **แจ้งเตือนบำรุงรักษา** — ระบบคำนวณวันครบกำหนดประจำปีให้อัตโนมัติ (เช่น ล้างแอร์วันนี้ นัดครั้งถัดไปอีก 1 ปี) จัดกลุ่ม เกินกำหนด / ใกล้ถึง / กำลังจะถึง
- 📈 **รายงาน** — รายได้ 6 เดือนย้อนหลัง แยกตามประเภทงาน และลูกค้า Top 5
- 🧾 **ใบเสร็จ** — ดูใบงาน ส่งเป็นข้อความผ่าน LINE หรือคัดลอกข้อความ
- 📤 **ส่งออก** — Excel (.xlsx 3 แผ่นงาน), PDF รายงาน (รองรับภาษาไทยเต็มรูปแบบ), สำรอง/กู้คืนไฟล์ .json
- 🌙 **โหมดมืด** + ติดตั้งเป็นแอปมือถือได้ (PWA) + ใช้งานออฟไลน์ได้
- ☁️ **ซิงค์ข้อมูล** (ตัวเลือก) — เชื่อมต่อ Firebase เพื่อเก็บข้อมูลบนคลาวด์

## 🚀 เริ่มใช้งานเร็ว ๆ

1. เปิด https://thanavut.github.io/fixpro/
2. กดปุ่ม **"เริ่มใช้งานเลย (ไม่ต้องเข้าสู่ระบบ)"** — เริ่มเพิ่มลูกค้าและบันทึกงานได้ทันที (ข้อมูลเก็บในเครื่อง)
3. อยากซิงค์ข้ามเครื่องภายหลัง → เมนู **ตั้งค่า** → กรอก Firebase Config → บันทึก แล้วล็อกอินด้วยอีเมลที่ลงทะเบียน

> ครั้งแรกจะมีข้อมูลตัวอย่างให้ 3 ลูกค้า 4 งาน เพื่อลองเล่น ลบได้ตามปกติ

## ☁️ เชื่อมต่อ Firebase (ซิงค์ข้ามเครื่อง)

1. สร้างโปรเจกต์ที่ https://console.firebase.google.com → **Add project**
2. **Build → Authentication → Get started → Email/Password → Enable**
3. **Build → Firestore Database → Create database** (เริ่มแบบ production mode)
4. ไปที่ **Project settings → Your apps → Web app** แล้วคัดลอกค่า `firebaseConfig` (apiKey, authDomain, projectId, storageBucket, messagingSenderId, appId)
5. ใน FixPro เปิด **ตั้งค่า → Firebase Cloud** กรอกค่าทั้งหมด → **บันทึก**
6. ตั้งค่า Firestore Rules (Console → Firestore → Rules) ตามตัวอย่าง:

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{uid} {
      allow read, write: if request.auth != null && request.auth.uid == uid;
    }
    match /customers/{doc} {
      allow read, write: if request.auth != null;
    }
    match /jobs/{doc} {
      allow read, write: if request.auth != null;
    }
  }
}
```

7. กลับมาที่แอป → กด **ลงทะเบียน** สร้างบัญชี → เข้าใช้งานได้ทันที (ไม่ต้องรออนุมัติ)

## 🖼️ เปิดใช้รูปถ่ายงาน (Cloudinary)

รูปถ่ายอัปโหลดขึ้น Cloudinary (ฟรี) — ไปที่ **ตั้งค่า → Cloudinary** กรอก Cloud Name และ Upload Preset (สร้าง preset แบบ unsigned ที่ Cloudinary Console → Settings → Upload)

## 🌐 Deploy (GitHub Pages)

เว็บ deploy จาก branch `main` โดยตรง (Settings → Pages → Source: **Deploy from a branch** → `main` / `/ (root)`):

1. เปิดใช้งาน Pages ครั้งเดียว (ทำแล้ว) — เว็บใช้งานได้ที่ `https://thanavut.github.io/fixpro/`
2. ทุกครั้งที่ push ไปที่ branch `main` เว็บจะอัปเดตอัตโนมัติภายใน 1–2 นาที

## 📁 โครงสร้างไฟล์

```
├── index.html            # ตัวแอปทั้งหมด (HTML + CSS + JS ในไฟล์เดียว)
├── manifest.webmanifest  # ไฟล์ PWA สำหรับติดตั้งเป็นแอปมือถือ
├── sw.js                 # Service worker — แคชไฟล์ไว้ใช้ตอนออฟไลน์
├── icons/                # ไอคอนแอป 192/512 px
└── README.md             # คู่มือการใช้งาน
```

## 🔄 การสำรองข้อมูล

- **สำรอง:** ตั้งค่า → สำรองข้อมูล → ดาวน์โหลดไฟล์ .json (ควรทำเป็นประจำ โดยเฉพาะเมื่อใช้โหมดเก็บในเครื่อง)
- **กู้คืน:** ตั้งค่า → กู้คืนข้อมูล → เลือกไฟล์ .json ที่สำรองไว้

## 🛠 เทคโนโลยี

HTML/CSS/JavaScript ล้วน (ไม่ต้อง build) · Firebase (Auth + Firestore) · Cloudinary · SheetJS · jsPDF + ฟอนต์ Sarabun · Font Awesome · ฟอนต์ Kanit

## 📄 License

ISC
