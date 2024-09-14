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
    print(f"\n运行结果 = {json_data}")

    # <editor-fold desc="保存结果">
    save_jsonfile = r"test.json"
    with open(save_jsonfile, mode='w', encoding='utf-8') as json_file:
        json.dump(json_load, json_file, ensure_ascii=False, indent=2)
    # </editor-fold>
    return json_load


# url = 'http://testzsdl.zijiapuzi.com/event/explore/selectExploreList'
# body = '''{
#   "city": "上海市",
#   "origin": "121.5762,31.178",
#   "page": 1,
#   "type": 0,
#   "rows": 10,
#   "userId": 634810  341102-1990-0801-0616
# }'''


# base_url = 'http://testzsdl.zijiapuzi.com'
# # base_url = 'http://mico.zsdlpro.com/'
#
# url = '%s/base/app/android/checkVersion' % base_url
# body = '''{
#   "isFirstStart": 0,
#   "userId": 0
# }'''

url = 'http://testzsdl.zijiapuzi.com/event/explore/selectExploreList'
body = '''{
      "city": "北京市",
      "origin": "",
      "page": 1,
      "type": 0,
      "rows": 10,
      "userId": 634810
    }'''


print(f"url = '{url}'")
print(f"body = '''{body}'''")
on_post(url, body)
