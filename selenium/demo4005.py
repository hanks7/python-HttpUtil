from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox()
# 打开首页
driver.get("http://localhost/upload/index.php")
# 输入关键字a
k=driver.find_element(By.ID,"keyword")
k.send_keys("a")
# 按下Ctrl+a全选
k.send_keys(Keys.CONTROL,"a")
sleep(2)
# 按下Ctrl+c全选
k.send_keys(Keys.CONTROL,"c")
sleep(2)
# 按下End键
k.send_keys(Keys.END)
sleep(2)
# 按下Ctrl+v全选
k.send_keys(Keys.CONTROL,"v")
sleep(2)
# 按下回车,网页刷新
k.send_keys(Keys.ENTER)#回车


sleep(3)
driver.quit()
