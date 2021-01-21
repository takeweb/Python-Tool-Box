import urllib.request
import json

url = 'http://localhost:8080/ifield_hitachiKenki-api/auth/Login'
params = {
    'cid': 'maruiso201807',
    'loginId': 'kesennuma',
    'loginPw': 'kesennuma',
    'mode': 'pc',
}

req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)))
with urllib.request.urlopen(req) as res:
    body = res.read()
    data = json.dumps(json.loads(body),indent=4,ensure_ascii=False)
    print(data)