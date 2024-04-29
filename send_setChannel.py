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
# http://testzsdl.zijiapuzi.com
# http://mico.zsdlpro.com/


base_url = 'http://testzsdl.zijiapuzi.com'
# base_url = 'http://mico.zsdlpro.com/'

url = '%s/base/app/android/setChannel' % base_url
body = '''{
  "channelList": [
{
"id": 1,
"channelName": "xiaomi", 
"appstoreUpdate": 0,
"fileEncode": "sdsd3243243"
},
{
"id": 2,
"channelName": "honor",  
"appstoreUpdate": 1,
"fileEncode": "sdsd3243243"
},
{
"id": 3,
"channelName": "huawei",  
"appstoreUpdate": 0,
"fileEncode": "sdsd3243243"
},
{
"id": 4,
"channelName": "oppo",  
"appstoreUpdate": 0,
"fileEncode": "sdsd3243243"
},
{
"id": 5,
"channelName": "vivo",  
"appstoreUpdate": 0,
"fileEncode": "sdsd3243243"
},
{
"id": 6,
"channelName": "yingyongbao",  
"appstoreUpdate": 0,
"fileEncode": "sdsd3243243"
}
]
}'''

print(f"url = '{url}'")
print(f"body = '''{body}'''")
on_post(url, body)
