# coding=utf-8
import requests
import json

url = 'http://testzsdl.zijiapuzi.com/social/follow/selectMyFollowList'
body = '''{
  "page": 1,
  "rows": 50,
  "userId": 634810
}'''


def method_name(s=url, body1=body):
    response = requests.request(
        "POST",
        s,
        headers={
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'Content-Type': 'application/json'
        },
        data=body1)
    data = json.loads(response.text)

    return data


json_data = method_name(url, body)


# print(json.dumps(json_data, indent=2, ensure_ascii=False))  # 序列化后再打印

def on_post(s, body1):
    global save_jsonfile
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", s, headers=headers, data=body1.encode('utf-8'))
    json_load = json.loads(response.text)

    # 序列化后再打印
    # print(json.dumps(json_load, indent=2, ensure_ascii=False))

    # <editor-fold desc="保存结果">
    # save_jsonfile = r"test.json"
    # with open(save_jsonfile, mode='w', encoding='utf-8') as json_file:
    #     json.dump(json_load, json_file, ensure_ascii=False, indent=2)
    # </editor-fold>
    return json_load


for i in json_data['data']['list']:
    for k in i:
        if (k == 'beNoticedId'):
            url = 'http://testzsdl.zijiapuzi.com/account/user/getInfo'
            s = i[k]
            body = '''{
                  "userId": %d
                }''' % s
            json_data = on_post(url, body)
            print(f'studentNumber:{json_data["data"]["studentNumber"]}     userId: {s} ')
