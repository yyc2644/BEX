from selenium.webdriver.chrome.options import Options  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
import time  

#搜狗浏览器的地址
# path = "C:\Users\Administrator\AppData\Local\SogouExplorer\SogouExplorer.exe"  
chrome_options = Options()
__browser_url = r'C:\Users\Administrator\AppData\Local\SogouExplorer\SogouExplorer.exe'
chrome_options.binary_location = __browser_url

driver = webdriver.Chrome(chrome_options=chrome_options)
time.sleep(3)
driver.get('http://www.baidu.com')
