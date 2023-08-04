from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Firefox()
# 打开首页
driver.get("http://localhost/upload/index.php")
# # 点击登录
# driver.find_element_by_css_selector("#ECS_MEMBERZONE > a:nth-child(2) > img:nth-child(1)").click()
driver.find_element(By.CSS_SELECTOR,"#ECS_MEMBERZONE > a:nth-child(2) > img:nth-child(1)").click()
sleep(1)
# 输入关键字a
driver.find_element(By.CSS_SELECTOR,"form#searchForm>input:nth-child(2)").send_keys("a")
# 点击搜索
driver.find_element(By.CSS_SELECTOR,"form#searchForm>input:nth-child(3)").click()
sleep(2)
# 点击选购中心：[href='pick_out.php']
driver.find_element(By.CSS_SELECTOR,"a[href='pick_out.php']").click()
sleep(2)
# 点击左上角ECSHOP商标
driver.find_element(By.CSS_SELECTOR,"a[name='top']>img").click()
sleep(2)
# 练习：点击“高级搜索”，等待2秒
driver.find_element(By.CSS_SELECTOR,"div#search a").click()
sleep(2)
# 输入价格最小值100，最大值500
driver.find_element(By.CSS_SELECTOR,"#min_price").send_keys("100")
driver.find_element(By.CSS_SELECTOR,"#max_price").send_keys("500")
# 点击“立即搜索”
driver.find_element(By.CSS_SELECTOR,"[name='Submit']").click()
sleep(5)
driver.quit()