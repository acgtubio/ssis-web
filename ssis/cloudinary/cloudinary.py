from os import getenv
import hashlib
from datetime import datetime
import requests

cldn_destroyUrl = 'https://api.cloudinary.com/v1_1/dhb9d15rg/image/destroy'

class Cloudinary:
    def __init__(self):
        self.__cldn_apikey = getenv("CLDN_API_KEY")
        self.__cldn_secret = getenv("CLDN_SECRET")
        self.__cldn_url = getenv("CLDN_URL")

    def uploadImage(self, ph, public_id, eager = ""):
        dt = datetime.now()
        ts = datetime.timestamp(dt)
    
        signature = self.__createSignature(ts = ts, public_id=public_id)

        payload = {
            'api_key': self.__cldn_apikey,
            'public_id': public_id,
            'timestamp': ts,
            'signature': signature
        }

        res = requests.post(self.__cldn_url, data=payload, files={'file': (ph.filename, ph.read())})
        js = res.json()

        if res.status_code == requests.codes.ok:
            return {
                'status_code': 200,
                'image_url': js['secure_url']
            }
        else: 
            return {
                'status_code': res.status_code,
                'message': res.text
            }

    def removeImg(self, public_id):
        dt = datetime.now()
        ts = datetime.timestamp(dt)
    
        signature = self.__createSignature(ts = ts, public_id=public_id)

        payload = {
            'api_key': self.__cldn_apikey,
            'public_id': public_id,
            'timestamp': ts,
            'signature': signature
        }

        res = requests.post(cldn_destroyUrl, data=payload)
        js = res.json()

        if res.status_code == requests.codes.ok:
            return {
                'status_code': 200
            }
        else: 
            return {
                'status_code': res.status_code,
                'message': res.text
            }


    def __createSignature(self, ts, public_id="", eager=""):
        public_id = f"public_id={public_id}&" if public_id !="" else ""
        eager = f"eager={eager}&" if eager !="" else ""

        ts = f"timestamp={ts}{self.__cldn_secret}"

        sigStr = eager + public_id + ts
        # print(sigStr)
        sigStr = sigStr.encode('utf-8')
        m = hashlib.sha1()
        m.update(sigStr)

        res = m.hexdigest()
        # print(res)
        return res