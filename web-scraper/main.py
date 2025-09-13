from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

url = 'https://www.hotstar.com/in/browse/reco-editorial/latest-releases/tp-ed_CJE3EAEaAQI'

options = Options()

driver = webdriver.Chrome(options=options)
driver.get(url)

time.sleep(3)

elements = driver.find_elements(By.CSS_SELECTOR, "div._2Qi2v27TcINx5EvPplHuDs div div")

for ele in elements:
    value = ele.get_attribute("aria-label")
    if value != None :
        print(value)

driver.quit()

