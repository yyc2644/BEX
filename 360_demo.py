from selenium.webdriver.chrome.options import Options  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
import time  

#360浏览器的地址  
chrome_options = Options()
__browser_url = r'C:\Users\Administrator\AppData\Roaming\360se6\Application\360se.exe'
chrome_options.binary_location = __browser_url

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('http://www.baidu.com')
time.sleep(3)