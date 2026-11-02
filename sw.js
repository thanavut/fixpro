/* FixPro Service Worker — แคชไฟล์แอปไว้ใช้งานตอนออฟไลน์ */
var CACHE = 'fixpro-v13';
var CORE = [
  './',
  './index.html',
  './manifest.webmanifest',
  './icons/icon-192.png',
  './icons/icon-512.png'
];
var CDN = [
  'https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js',
  'https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js',
  'https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.8.2/jspdf.plugin.autotable.min.js',
  'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css',
  'https://fonts.googleapis.com/css2?family=Kanit:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,300;1,400&display=swap'
];

self.addEventListener('install', function (e) {
  e.waitUntil(
    caches.open(CACHE)
      .then(function (c) { return c.addAll(CORE.concat(CDN)); })
      .catch(function (err) { console.warn('SW pre-cache บางรายการไม่สำเร็จ:', err); })
      .then(function () { return self.skipWaiting(); })
  );
});

self.addEventListener('activate', function (e) {
  e.waitUntil(
    caches.keys()
      .then(function (keys) { return Promise.all(keys.filter(function (k) { return k !== CACHE; }).map(function (k) { return caches.delete(k); })); })
      .then(function () { return self.clients.claim(); })
  );
});

self.addEventListener('fetch', function (e) {
  if (e.request.method !== 'GET') return;
  var url = new URL(e.request.url);

  // หน้าเว็บหลัก: network-first (ได้เวอร์ชันใหม่เสมอเมื่อออนไลน์) fallback เป็นแคช
  if (e.request.mode === 'navigate') {
    e.respondWith(
      fetch(e.request)
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
    url.hostname.indexOf('fonts.googleapis.com') !== -1 ||
    url.hostname.indexOf('fonts.gstatic.com') !== -1 ||
    url.hostname.indexOf('cdn.jsdelivr.net') !== -1 ||
    (url.hostname === 'www.gstatic.com' && url.pathname.indexOf('/firebasejs/') === 0);
  if (!cacheable) return;

  e.respondWith(
    caches.match(e.request).then(function (hit) {
      if (hit) return hit;
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
