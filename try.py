from selenium import webdriver
from browsermobproxy import Server
import json
import time

def test_har():
    server = Server(r"C:\browsermob-proxy-2.1.3\bin\browsermob-proxy.bat")
    server.start()
    proxy = server.create_proxy(params={"trustAllServers": "true"})
    options = webdriver.ChromeOptions()
    options.add_argument("--proxy-server={}".format(proxy.proxy))
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    proxy.new_har("https://www.baidu.com", options={'captureHeaders': True, 'captureContent': True, 'captureBinaryContent': True})
    driver.get("https://www.baidu.com")
    time.sleep(5)
    driver.refresh()
    time.sleep(5)
    with open("harfile.har", "w") as harfile:
        harfile.write(json.dumps(proxy.har))
    server.stop()
    driver.quit()