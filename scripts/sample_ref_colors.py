#!/usr/bin/env python3
"""วัดสีจริงจากเฟรมคลิปตัวอย่าง Admin Dashboard V2 (@paulcodes4)
พิกัด = พิกเซลจริงในเฟรม 576x1024 (แถบ dashboard อยู่ y 340-730)
ใช้ median ของพื้นที่ 5x5 รอบจุด เพื่อลด noise จาก video compression"""
from PIL import Image
import statistics

def sample(im, x, y, r=2):
    px = im.load()
    R, G, B = [], [], []
    for dx in range(-r, r + 1):
        for dy in range(-r, r + 1):
            xx, yy = min(max(x + dx, 0), im.width - 1), min(max(y + dy, 0), im.height - 1)
            c = px[xx, yy]
            R.append(c[0]); G.append(c[1]); B.append(c[2])
    return (int(statistics.median(R)), int(statistics.median(G)), int(statistics.median(B)))

def hexs(c):
    return '#%02X%02X%02X' % c

points = {
    'f_07': [
        ('body บน (เหนือ header)', 233, 357),
        ('body ขวา (นอกแผง)', 572, 573),
        ('body ล่างซ้าย', 8, 607),
        ('sidebar bg (บน)', 83, 447),
        ('sidebar bg (ล่าง)', 83, 657),
        ('search pill ใน header', 133, 372),
        ('วงกลมไอคอน header', 448, 372),
        ('แผงใหญ่ (ข้าง Finance)', 317, 402),
        ('การ์ดสรุป 1 (แถวบน)', 200, 440),
        ('การ์ดสรุป 1 (ใต้เลข)', 150, 467),
        ('การ์ดสรุป 4', 500, 473),
        ('การ์ดกราฟใหญ่', 333, 593),
        ('การ์ดโดนัท', 533, 527),
        ('ชิปย่อยในการ์ดโดนัท', 433, 593),
        ('แผงตาราง payouts', 550, 640),
        ('ปุ่มดำ Pay Adrian', 517, 416),
        ('ปุ่มเทา Revert QB', 457, 416),
        ('pill กรองเข้ม (Due)', 467, 632),
        ('วงโดนัท cyan', 477, 537),
    ],
    'f_04': [
        ('sidebar bg ซ้าย', 20, 490),
        ('sidebar bg กลาง', 87, 600),
        ('active pill Overview', 50, 528),
        ('แผงเนื้อหาใหญ่', 267, 573),
        ('header ช่องว่างขวา', 300, 372),
        ('body บน f_04', 167, 355),
        ('body ล่างขวา f_04', 567, 723),
        ('กล่อง Business plan', 50, 673),
    ],
    'f_10': [
        ('body ล่างขวา (teal อ่อน)', 572, 707),
        ('การ์ดทะเบียนบ้าน (แก้วสว่าง)', 300, 480),
    ],
}

for fname, pts in points.items():
    im = Image.open(f'/tmp/ref/{fname}.jpg').convert('RGB')
    print(f'--- {fname} ---')
    for label, x, y in pts:
        c = sample(im, x, y)
        print(f'{label:38s} ({x:3d},{y:3d}) = {hexs(c)}  rgb{c}')
