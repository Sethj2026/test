from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
opts = Options()
browser = Firefox(options=opts)
browser.get('https://google.com')
time.sleep(3600)