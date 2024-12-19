# import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
# with webdriver.Chrome(ChromeDriverManager().install()) as driver:
#     driver.get("https://stepik.org/course/104774")
#     time.sleep(5)

# import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.core.os_manager import ChromeType
# from selenium.webdriver.chrome.service import Service as ChromiumService
#
# with webdriver.Chrome(
#         service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())) as driver:
#     driver.get("https://stepik.org/course/104774")
#     time.sleep(5)

# пробный запуск с подключением расширения mouse coordinates
import time
from selenium import webdriver

options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension('/home/lex/.config/chromium/Default/Extensions/gkkmpbaijflcgbbdfjgihbgmpkhgpgof/coordinates_0.2_0.crx')

with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://stepik.org/course/104774'
    browser.get(url)
    time.sleep(15)