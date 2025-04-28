from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os,time
import chromedriver_autoinstaller


class CathayBankScreenshotter:
    def __init__(self, headless=True, wait_time=20):
        self.headless = headless
        self.wait_time = wait_time
        self.driver = self._init_driver()

    def _init_driver(self):
        chromedriver_path = chromedriver_autoinstaller.install()

        options = Options()
        if self.headless:
            options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument('--enable-unsafe-swiftshader')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-software-rasterizer')
        options.add_argument('--disable-webgl')
        user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/135.0.7049.115 Safari/537.36")
        options.add_argument(f"user-agent={user_agent}")

        options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        service = Service(executable_path=chromedriver_path)
        driver = webdriver.Chrome(service=service, options=options)

        driver.implicitly_wait(self.wait_time)
        driver.maximize_window()
        return driver

    def close(self):
        if self.driver:
            self.driver.quit()

    def ImageDict(self):
        basePath = os.path.abspath(os.path.join(os.path.dirname(os.getcwd()), "image"))
        if not os.path.isdir(basePath):
            os.makedirs(basePath)

        return basePath
    
    def screenshot(self, filename):
        filenamePath = os.path.join(self.ImageDict(), filename + '.png')
        self.driver.save_screenshot(filenamePath)





