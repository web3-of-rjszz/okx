import requests
import time
import hmac
import base64
import json
import datetime

# 提现，提现地址需要是白名单内的地址
def okx_withdraw(api_key, secret_key, passphrase, ccy, amt, toAddr, fee, chain):
    method = "POST"
    path = "/api/v5/asset/withdrawal"
    timestamp = datetime.datetime.utcnow().isoformat(timespec="milliseconds") + "Z"
    body = json.dumps({
        "ccy": ccy, "amt": amt, "dest": "4", 
        "toAddr": toAddr, "fee": fee, "chain": chain
    })
    message = timestamp + method + path + body
    signature = base64.b64encode(hmac.new(secret_key.encode(), message.encode(), "sha256").digest()).decode()
    
    headers = {
        "OK-ACCESS-KEY": api_key,
        "OK-ACCESS-SIGN": signature,
        "OK-ACCESS-TIMESTAMP": timestamp,
        "OK-ACCESS-PASSPHRASE": passphrase,
        "Content-Type": "application/json"
    }
    return requests.post("https://www.okx.com" + path, data=body, headers=headers).json()