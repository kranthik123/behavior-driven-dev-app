from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from xvfbwrapper import Xvfb
from selenium.webdriver import DesiredCapabilities

def before_all(context):
    context.vdisplay = Xvfb(width=1920, height=1080, colordepth=16)
    context.vdisplay.start()
    print("> Starting the Browser")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--verbose')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument('--remote-debugging-port=9222')
    # chrome_options.add_argument('--window-size=1920,1080')
    # chrome_options.add_argument('--lang=en_US')
    # chrome_options.add_argument('--ignore-certificate-errors')
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['acceptSslCerts'] = True
    capabilities['acceptInsecureCerts'] = True
    context.browser = webdriver.Chrome('/features/chromedriver', chrome_options=chrome_options,desired_capabilities=capabilities)
    context.browser.implicitly_wait(15)

def after_all(context):
    print("> Closing the browser")
    context.browser.close()
    context.browser.quit()
    context.vdisplay.stop()
