#尝试使用cookie的方式跳过登陆功能

from selenium import webdriver


driver = webdriver.Chrome()

#使用add_cookie方法，直接传入关键参数 token，再刷新页面
driver.add_cookie({'name':'token','value':'c9395f2e-bea7-475a-9288-7f6cf616e52e'})

driver.refresh()