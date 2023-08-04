from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
# 打开首页
driver.get("http://localhost/upload/index.php")
# 点击登录
driver.find_element(By.CSS_SELECTOR,"font#ECS_MEMBERZONE>a:nth-child(2)>img").click()
sleep(2)
# 后退（转到上一页）  --了解
driver.back()
sleep(2)
# 前进（转到下一页）  --了解
driver.forward()
# 最小化
driver.minimize_window()
sleep(2)
# 最大化
driver.maximize_window()
sleep(2)
# 设置浏览器窗口的大小
driver.set_window_size(800,600)
# 获得标题
t1=driver.title
print(t1)
# 获得当前的url
u1=driver.current_url
print(u1)
# 获得网页源代码（从<html>到</html>之间的全部内容）
ps1=driver.page_source
print(ps1)
sleep(2)
driver.quit()