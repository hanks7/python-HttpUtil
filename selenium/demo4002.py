from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.get("http://localhost/upload/index.php")
# 点击登录
driver.find_element(By.CSS_SELECTOR,"font#ECS_MEMBERZONE>a:nth-child(2)>img").click()
sleep(2)
# 输入用户名
driver.find_element(By.CSS_SELECTOR,"tr:first-child>td:last-child>input").send_keys("1234")
# 输入密码
driver.find_element(By.CSS_SELECTOR,"tr:nth-child(2)>td:last-child>input").send_keys("567")
# 练习：点击登录页里的“密码问题找回密码”这个超级链接
driver.find_element(By.CSS_SELECTOR,"tr:last-child>td:last-child>a:first-child").click()

# 点击留言板
driver.find_element(By.LINK_TEXT,"留言板").click()
sleep(3)
# 输入主题文本框里的数据
driver.find_element(By.NAME,"msg_title").send_keys("111")
# 没有报错，向第一个文本框（关键字文本框）里输入433
driver.find_element(By.TAG_NAME,"input").send_keys("433")

# 定位一组单选按钮：留言类型里的5个单选按钮
# 1.点击其中的第2个单选按钮
driver.find_elements(By.NAME,"msg_type")[1].click()
sleep(3)
# 2.逐一点击留言类型里的每个单选按钮
a=driver.find_elements(By.NAME,"msg_type")
print(type(a))#<class 'list'>
print(len(a))#5
for b in a:
    b.click()
    sleep(1)
# 3.点击从2个到最后一个单选按钮
for i in range(1,len(a)):
    print(i)
    a[i].click()
    sleep(3)
    # 刷新网页
    driver.refresh()
    # 解决方案是重新定位元素，再次赋值给变量。
    a=driver.find_elements(By.NAME,"msg_type")

# 需求：逐个点击首页的那一排超级链接
c=driver.find_elements(By.XPATH,"//div[@id='mainNav']/a")
for i in range(0,len(c)):
    c[i].click()
    sleep(3)
    c = driver.find_elements(By.XPATH, "//div[@id='mainNav']/a")

sleep(4)
driver.quit()