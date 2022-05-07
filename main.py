from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
import time

user_agent = UserAgent()
url = "https://rt.pornhub.com/view_video.php?viewkey=ph6265926968eac/"
proxy_ip = "45.238.142.10:3128"
# Путь до веб-драйвера
executable_path = "/Users/damir/Documents/Apps/pyhub/chromedriver/chromedriver"

# Проверка на webdriver
# url = "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"
options = webdriver.ChromeOptions()

# Различные аргументы для запуска "https://peter.sh/experiments/chromium-command-line-switches/"
# user agent
options.add_argument(f"user-agent={user_agent.chrome}")
# proxy server
options.add_argument(f"--proxy-server={proxy_ip}")
# disable webdriver
options.add_argument("--disable-blink-features=AutomationControlled")
# mute audio
options.add_argument("--mute-audio")

driver = webdriver.Chrome(executable_path=executable_path, options=options)

# Входная точка тут
try:
  driver.get(url=url)
  time.sleep(500)
except Exception as ex:
  print(ex)
finally:
  driver.close()
  driver.quit()