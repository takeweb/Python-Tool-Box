import json
import urllib.request

url = 'https://slm-dev.ifieldcloud.jp/ifield_hitachiKenki-api/auth/Login?cid=maruiso201807&loginId=kesennuma&loginPw=kesennuma&mode=pc'
headers = {
    'Content-Type': 'application/json',
}
data = {
    'foo': 123,
}

req = urllib.request.Request(url, json.dumps(data).encode(), headers)
with urllib.request.urlopen(req) as res:
    body = res.read()
    print(body)