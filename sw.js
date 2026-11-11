/* FixPro Service Worker — แคชไฟล์แอปไว้ใช้งานตอนออฟไลน์ */
var CACHE = 'fixpro-v57';
var CORE = [
  './',
  './index.html',
  './manifest.webmanifest',
  './manifest.webmanifest?v=57', // v56-57: URL เปลี่ยนบังคับ Chrome อ่าน manifest ใหม่ = เคลียร์สแปลชม่วงตกค้างยุค v49 (v57: bg สแปลชเป็นขาวตัดกับไอคอนเขียว)
  './icons/icon-192.png',
  './icons/icon-180.png',
  './icons/icon-512.png',
  // Firebase SDK เก็บในแอปเอง (โฟลเดอร์ /firebase) — เชื่อมคลาวด์ได้แม้เน็ตกระตุก/ออฟไลน์ ไม่พึ่ง gstatic อีกต่อไป
  // v40: ถอนระบบล็อกอินแล้วจึงไม่โหลด firebase-auth-compat.js (ไฟล์คงอยู่ใน repo สำหรับหน้าเก่าที่แคชค้างเท่านั้น)
  './firebase/firebase-app-compat.js',
  './firebase/firebase-firestore-compat.js',
  './assets/fontawesome/css/all.min.css',
  './assets/fontawesome/webfonts/fa-solid-900.woff2',
  './assets/fontawesome/webfonts/fa-solid-900.ttf',
  './assets/fontawesome/webfonts/fa-regular-400.woff2',
  './assets/fontawesome/webfonts/fa-regular-400.ttf',
  './assets/fontawesome/webfonts/fa-brands-400.woff2',
  './assets/fontawesome/webfonts/fa-brands-400.ttf',
  './assets/fontawesome/webfonts/fa-v4compatibility.woff2',
  './assets/fontawesome/webfonts/fa-v4compatibility.ttf',
  // v52: ฟอนต์ Kanit เก็บในแอปเอง — เจ้าของร้านสั่ง "ฟอนต์ต้องเป็น Kanit เท่านั้น"
  // แคชไว้ล่วงหน้า = ออฟไลน์/เน็ตกระตุกก็แสดง Kanit 100% ไม่มีทางโหลดไม่ได้
  './assets/fonts/kanit/kanit-400-latin.woff2',
  './assets/fonts/kanit/kanit-400-thai.woff2',
  './assets/fonts/kanit/kanit-500-latin.woff2',
  './assets/fonts/kanit/kanit-500-thai.woff2',
  './assets/fonts/kanit/kanit-600-latin.woff2',
  './assets/fonts/kanit/kanit-600-thai.woff2',
  './assets/fonts/kanit/kanit-700-latin.woff2',
  './assets/fonts/kanit/kanit-700-thai.woff2',
  './assets/fonts/kanit/kanit-800-latin.woff2',
  './assets/fonts/kanit/kanit-800-thai.woff2',
];
var CDN = [
  'https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js',
  'https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js',
  'https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.8.2/jspdf.plugin.autotable.min.js',
];

self.addEventListener('install', function (e) {
  e.waitUntil(
    caches.open(CACHE)
      // เก็บทีละไฟล์ — ห้ามใช้ addAll เด็ดขาด เพราะ addAll จะล้มทั้งชุดถ้าเส้นใดเส้นหนึ่งพลาด
      // (เคยทำให้ SDK ล็อกอินไม่เคยลงแคชเลย หน้าเข้าสู่ระบบจึงโหลดระบบไม่เคยสำเร็จ)
      .then(function (c) {
        return Promise.all(CORE.concat(CDN).map(function (u) {
          return c.add(u).catch(function (err) { console.warn('SW pre-cache ข้ามรายการ:', u, err && err.message); });
        }));
      })
      .then(function () { return self.skipWaiting(); })
  );
});

self.addEventListener('activate', function (e) {
  e.waitUntil(
    caches.keys()
      .then(function (keys) { return Promise.all(keys.filter(function (k) { return k !== CACHE; }).map(function (k) { return caches.delete(k); })); })
      .then(function () { return self.clients.claim(); })
      .then(function () {
        // หลังอัปเดต SW ให้แท็บที่เปิดค้างไว้รีโหลดตัวเองหนึ่งครั้ง เพื่อรับ HTML เวอร์ชันใหม่ทันที (ไม่ต้องปิด-เปิดแอปเอง)
        return self.clients.matchAll({ type: 'window' }).then(function (clients) {
          clients.forEach(function (c) {
            // ส่งข้อความให้หน้าเว็บรีโหลดตัวเองด้วย location.reload() (โหลดรายการประวัติเดิม ไม่เพิ่มรายการใหม่)
            // เดิมใช้ c.navigate() ทำให้ประวัติมีหน้าแอปเวอร์ชันเก่าค้างอยู่ข้างล่าง
            if (typeof c.postMessage === 'function') { c.postMessage({ type: 'FIXPRO_SW_UPDATED' }); }
          });
        });
      })
  );
});

self.addEventListener('fetch', function (e) {
  if (e.request.method !== 'GET') return;
  var url = new URL(e.request.url);

  // หน้าเว็บหลัก: network-first (ได้เวอร์ชันใหม่เสมอเมื่อออนไลน์) fallback เป็นแคช
  // cache:'no-cache' = บังคับ revalidate กับเซิร์ฟเวอร์ทุกครั้ง ไม่ติดแคช HTTP ที่ยังไม่หมดอายุ
  if (e.request.mode === 'navigate') {
    e.respondWith(
      fetch(e.request, { cache: 'no-cache' })
        .then(function (r) {
          var copy = r.clone();
          caches.open(CACHE).then(function (c) { c.put('./index.html', copy); });
          return r;
        })
        .catch(function () { return caches.match('./index.html'); })
    );
    return;
  }

  // API/ข้อมูล (firebase, cloudinary) — ไม่แคช
  if (url.hostname.indexOf('googleapis.com') !== -1 || url.hostname.indexOf('firebaseio.com') !== -1 || url.hostname.indexOf('cloudinary.com') !== -1) return;

  // ไฟล์ static: cache-first
  var cacheable =
    url.origin === location.origin ||
    url.hostname.indexOf('cdnjs.cloudflare.com') !== -1 ||
    url.hostname.indexOf('cdn.jsdelivr.net') !== -1 ||
    (url.hostname === 'www.gstatic.com' && url.pathname.indexOf('/firebasejs/') === 0);
  if (!cacheable) return;

  e.respondWith(
    caches.match(e.request).then(function (hit) {
      // ห้ามเอา opaque response กลับไปให้ request ที่มี integrity (SRI) — ตรวจ digest ไม่ได้ จะโดนบล็อกทันที
      if (hit && hit.type !== 'opaque') return hit;
      return fetch(e.request).then(function (r) {
        if (r.ok) {
          var copy = r.clone();
          caches.open(CACHE).then(function (c) { c.put(e.request, copy); });
        }
        return r;
      }).catch(function () { return hit; });
    })
  );
});
