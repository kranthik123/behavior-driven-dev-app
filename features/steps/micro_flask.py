from behave import *
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time

@Given(u'User is on Home Page "http://localhost:5000/" on browser "chrome"')
def step_impl(context):
    context.browser.get('http://localhost:5000/')
    time.sleep(5)
    print("Given Statement was Successful")

@when(u'User Enters Username as "John Doe"')
def step_impl(context):
    #wait = WebDriverWait(context.browser, 15)
    #user = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
    #context.browser.find_element_by_xpath("//*[@id='username']").send_keys("John Doe")
    #context.browser.find_element_by_id("username").send_keys('John Doe')
    time.sleep(5)
    pass

@when(u'User clicks on "Submit" button')
def step_impl(context):
    #context.browser.find_element_by_id('btnSubmit').click()
    time.sleep(5)
    pass

@then(u'Message displayed "Hello John Doe"')
def step_impl(context):
    time.sleep(5)
    #for elem in context.browser.find_elements_by_xpath('.//span[@class = "demo"]'):
        #print (elem.text)
    pass

@then(u'close browser')
def step_impl(context):
    time.sleep(5)
    #context.browser.quit()
    pass
