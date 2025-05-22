from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
chrome_service = Service(executable_path="/usr/bin/chromedriver")
driver = webdriver.Chrome(options=options, service=chrome_service)
driver.get('https://automationintesting.online/')
driver.quit()