# -*- coding: utf-8 -*-

import requests
import json

#xxxxの部分に自分のAPIキーを入力する
APIKEY='xxxx'

url = "https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue?APIKEY={}".format(APIKEY) 
payload = {
 "utt": "こんにちは",
 "context": "",
 "nickname": "光",
 "nickname_y": "ヒカリ",
 "sex": "女",
 "bloodtype": "B",
 "birthdateY": "1997",
 "birthdateM": "5",
 "birthdateD": "30",
 "age": "16",
 "constellations": "双子座",
 "place": "東京",
 "mode": "dialog",
}

r = requests.post(url, data=json.dumps(payload))
print r.json()['utt']
