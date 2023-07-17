import pymysql

conn = pymysql.connect(host='192.168.171.133', db='wa_test', user='root', passwd='123456')
cursor = conn.cursor()
sqls = ["delete from info where id=4", "delete from users where id=4",
        "insert into users(id,username,password)values(4,'test01',md5('123456'))",
        "insert into info(id,name)values(4,'测试一')"]
for sql in sqls:
    cursor.execute(sql)
conn.commit()
conn.close()
#
import requests

url = 'http://192.168.171.133/apitest/login/'
args = {'username': 'test01', 'password': '123456'}
res = requests.post(url, args)
print(res.text)         # 调试
#
actual = res.text       # 实际结果
expect = '登录验证成功'   # 预期结果
if expect in actual:    # 实际结果用的text,用in比较
    print('响应结果比对通过')
else:
    print(f'响应结果比对失败==预期：{expect}==实际：{actual}')
