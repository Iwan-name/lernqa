import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# Укажите путь к ChromeDriver
# driver_path = '/usr/local/bin/chromedriver'
# service = Service(driver_path)
# Создайте экземпляр WebDriver
driver = webdriver.Chrome()

# Откройте веб-страницу
driver.get('https://www.google.com')

time.sleep(20)



