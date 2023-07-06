from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print(driver.title)
time.sleep(1000);
driver.close()