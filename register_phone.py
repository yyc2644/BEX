from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://192.168.1.248:9079")

# driver.find_element_by_name("注册").click()
# driver.find_element_by_tag_name("注册").click()s
driver.find_element_by_class_name("el-button--default").click()
# 注册的验证码都是101010