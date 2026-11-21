#!/usr/bin/env python3
"""FixPro — ขอสิทธิ์ GitHub ด้วย OAuth Device Flow (ใช้เมื่อ .secrets/gh_token.json หมดอายุ/โดนเพิกถอน)

CLIENT_ID ฝังไว้ในไฟล์นี้แล้ว (ค่า public ของ OAuth App — ปรากฏใน HANDOFF_FIXPRO.md ข้อ 3 เช่นกัน)
ถ้าต้องใช้ client id อื่น: --client-id / env GH_CLIENT_ID / ไฟล์ .secrets/gh_client_id.txt

ผลลัพธ์: เขียน token ไปที่ /home/z/my-project/.secrets/gh_token.json (อยู่นอก repo — ห้าม commit)
เวลาใช้: python /home/z/my-project/fixpro/scripts/gh_device_poll.py
"""
import json, os, sys, time, urllib.parse, urllib.request
from datetime import datetime

CLIENT_ID = '178c6fc778ccc68e1d6a'  # OAuth App ของ FixPro (public value — ไม่ใช่ความลับ)
SECRETS_DIR = '/home/z/my-project/.secrets'
TOKEN_PATH = os.path.join(SECRETS_DIR, 'gh_token.json')
SCOPES = 'repo,workflow'  # push โค้ด + แก้ .github/workflows (v102: ต้องมี workflow ด้วยถ้าจะ commit ไฟล์ในโฟลเดอร์นั้น)


def load_client_id(argv):
    for i, a in enumerate(argv):
        if a == '--client-id' and i + 1 < len(argv):
            return argv[i + 1].strip()
    env = os.environ.get('GH_CLIENT_ID')
    if env:
        return env.strip()
    path = os.path.join(SECRETS_DIR, 'gh_client_id.txt')
    if os.path.exists(path):
        return open(path).read().strip()
    return CLIENT_ID


def post(url, data):
    req = urllib.request.Request(url, data=urllib.parse.urlencode(data).encode(),
                                 headers={'Accept': 'application/json',
                                          'User-Agent': 'fixpro-device-flow'},
                                 method='POST')
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def main():
    client_id = load_client_id(sys.argv)
    if not client_id:
        sys.exit('ยังไม่มี CLIENT_ID (ควรฝังไว้แล้ว — ถ้าขาดให้ดู HANDOFF ข้อ 3)')
    os.makedirs(SECRETS_DIR, exist_ok=True)

    r = post('https://github.com/login/device/code', {'client_id': client_id, 'scope': SCOPES})
    code, dc, interval, expires = r['user_code'], r['device_code'], int(r.get('interval', 5)), int(r.get('expires_in', 900))
    print('เปิดลิงก์นี้แล้วใส่รหัส: ' + r['verification_uri'])
    print('รหัส: ' + code + '  (หมดอายุใน ' + str(expires // 60) + ' นาที)')

    deadline = time.time() + expires
    token = None
    while time.time() < deadline:
        time.sleep(interval)
        t = post('https://github.com/login/oauth/access_token',
                 {'client_id': client_id, 'device_code': dc,
                  'grant_type': 'urn:ietf:params:oauth:grant-type:device_code'})
        if t.get('access_token'):
            token = t['access_token']
            break
        err = t.get('error')
        if err == 'slow_down':
            interval += 5
        elif err and err != 'authorization_pending':
            sys.exit('GitHub ปฏิเสธ: ' + err + ' — ' + str(t.get('error_description', '')))
    if not token:
        sys.exit('หมดเวลารอการยืนยัน ลองใหม่')

    with open(TOKEN_PATH, 'w') as f:
        json.dump({'token': token, 'scope': SCOPES, 'saved_at': datetime.now().isoformat()}, f)
    os.chmod(TOKEN_PATH, 0o600)
    print('เซฟ token แล้ว: ' + TOKEN_PATH + ' (นอก repo — ห้าม commit token)')


if __name__ == '__main__':
    main()
