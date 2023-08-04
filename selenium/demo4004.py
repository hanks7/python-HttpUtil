from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
# 打开首页
driver.get("http://localhost/upload/index.php")
# 点击“留言板”
driver.find_element(By.LINK_TEXT,"留言板").click()
sleep(1)
# 输入留言内容  \n代表换行符的转义字符
driver.find_element(By.NAME,"msg_content").send_keys("123\n456\\n")
# 输入电子邮件地址文本框里输入abc@123.com\n123
driver.find_element(By.NAME,"user_email").send_keys("abc@123.com\n123")
sleep(4)
driver.quit()