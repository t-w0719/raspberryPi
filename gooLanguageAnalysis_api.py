# -*- coding: utf-8 -*-                                                              
import requests                                             

##
# 録音例：
# arecord -f S16_LE -r 16000 -D hw:0,0 test.wav
# 16ビット 16000Hzの音声データにしないといけない
##

#xxxxの部分に自分のAPIキーを入力する 
APIKEY='xxxx'
path = '/home/pi/test.wav'
url = "https://api.apigw.smt.docomo.ne.jp/amiVoice/v1/recognize?APIKEY={}".format(APIKEY)
files = {"a": open(path, 'rb'), "v":"on"}
r = requests.post(url, files=files)
print r.json()['text']
