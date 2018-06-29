# !/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json
import uuid
import base64

def get_token():
    url = "https://openapi.baidu.com/oauth/2.0/token"
    grant_type = "client_credentials"
    api_key = "1dHoj1lYG4VDwL5c49Yo0P1H"
    secret_key = "7cae5e79ea3259df09210c3910d31c8a"
    data = {'grant_type': 'client_credentials', 'client_id': api_key, 'client_secret': secret_key}
    r = requests.post(url, data=data)
    token = json.loads(r.text).get("access_token")
    return token


def recognize(sig, rate, token):
    url = "http://vop.baidu.com/server_api"
    speech_length = len(sig)
    speech = base64.b64encode(sig).decode("utf-8")
    mac_address = uuid.UUID(int=uuid.getnode()).hex[-12:]
    rate = rate
    data = {
        "format": "pcm",
        "lan": "zh",
        "token": token,
        "len": speech_length,
        "rate": rate,
        "speech": speech,
        "cuid": mac_address,
        "channel": 1,
    }
    data_length = str(len(json.dumps(data).encode("utf-8")))
    headers = {"Content-Type": "application/json",
               "Content-Length": data_length}
    r = requests.post(url, data=json.dumps(data), headers=headers).text
    ret = json.loads(r)
    text = ret['result'][0]
    return text


def main():
    filename = "temp/voice.pcm"
    signal = open(filename, "rb")
    rate = 16000
    token = get_token()
    ret = recognize(signal.read(), rate, token)
    signal.close()
    return ret

if __name__ == '__main__':
    main()