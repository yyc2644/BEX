from selenium import webdriver


driver = webdriver.Chrome()
driver.get("http://192.168.1.248:9079/#/")


lanuage = driver.find_element_by_class_name("el-dropdown-trigger-text")
print(type(lanuage))
print(lanuage.text)
try:
    driver.find_element_by_class_name("el-dropdown-trigger-text").text =="中文"
    print("符合要求")
except EOFError:
    print("不是中文") 
# driver.find_element_by_link_text("简体中文")

