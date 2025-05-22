import unittest;
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class HomePageTests(unittest.TestCase):
    def __init__(self, methodName = "runTest"):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        chrome_service = Service(executable_path="/usr/bin/chromedriver") # hack to make linux/wsl work
        self.driver = webdriver.Chrome(options=options, service=chrome_service)
        super().__init__(methodName)

    def setUp(self):
        if not self.driver is None:
            self.driver.get('https://automationintesting.online/')
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
    def test_page_loads(self):
        self.assertIn("Restful-booker", self.driver.title)
 