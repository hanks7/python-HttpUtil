# coding=utf-8
import json

import requests


def on_post(s, body1):
    global save_jsonfile
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", s, headers=headers, data=body1.encode('utf-8'))
    json_load = json.loads(response.text)

    # 序列化后再打印
    json_data = json.dumps(json_load, indent=2, ensure_ascii=False)
    print(f"response = {json_data}")

    # <editor-fold desc="保存结果">
    save_jsonfile = r"test.json"
    with open(save_jsonfile, mode='w', encoding='utf-8') as json_file:
        json.dump(json_load, json_file, ensure_ascii=False, indent=2)
    # </editor-fold>
    return json_load


url = 'http://testzsdl.zijiapuzi.com/shop/order/selectWuLiuDetail'
body = '''{
  "orderId": 202306011425150097
}'''

print(f"url = '{url}'")
print(f"body = '''{body}'''")
on_post(url, body)
