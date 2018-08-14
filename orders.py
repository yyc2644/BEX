#author：杨壹程
#批量挂单


#accessToken: 5c58c485-cec1-41f0-91e0-0659e790a8ea

from selenium import webdriver

driver = webdriver.Chrome()


# driver.get("http://192.168.1.248:9079/#/trade/index?marketId=33")

# driver.add_cookie({'name':'accessToken','value':'5c58c485-cec1-41f0-91e0-0659e790a8ea'})

driver.get("http://192.168.1.248:9079/#/")

driver.add_cookie({'name':'token','value':'5c58c485-cec1-41f0-91e0-0659e790a8ea'})


driver.refresh

