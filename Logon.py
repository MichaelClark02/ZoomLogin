from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from datetime import datetime 
from selenium.webdriver.common.alert import Alert 
from info import pw, user, zoomlinks, times
from selenium.webdriver.chrome.options import Options


options = Options()
prefs = {
    "download_restrictions": 3,
}
options.add_argument("user-data-dir=C:\\Users\\micha\\ChromeProfiles\\User Data")
options.add_experimental_option(
    "prefs", prefs
)
browser = webdriver.Chrome("C:\\Users\\micha\\ChromeDriver86\\chromedriver.exe", chrome_options=options)



def portalLogon():
    browser.get('https://my.harmonytx.org/idp/AuthnEngine#/authn')

    browser.find_element_by_xpath('/html/body/div/div/div/span/a').click()

    sleep(1)
    user_input = browser.find_element_by_xpath('/html/body/div/div/main/div/form/div[1]/div/input')
    user_input.send_keys(user)
    browser.find_element_by_xpath('//*[@id="authn-go-button"]').click()

    sleep(1)
    pw_input = browser.find_element_by_xpath('/html/body/div/div/main/div/form/div[1]/div/div/input')
    pw_input.send_keys(pw)
    browser.find_element_by_xpath('//*[@id="authn-go-button"]').click()

def zoomLogon():
    sleep(1)
    browser.get('https://harmonytx.zoom.us/')
    browser.find_element_by_xpath('/html/body/div/div[1]/div/div[5]/div[1]/a/span').click()
    browser.minimize_window()



portalLogon()
zoomLogon()



while True:
    hour = datetime.now().hour
    print(hour)
    if hour == times[0]:
        browser.maximize_window()
        browser.get(zoomlinks[0])
    elif hour == times[1]:
        browser.maximize_window()
        browser.get(zoomlinks[1])
    elif hour == times[2]:
        browser.maximize_window()
        browser.get(zoomlinks[2])
    elif hour == times[3]:
        browser.maximize_window()
        browser.get(zoomlinks[3])
    elif hour > 16:
        break
    sleep(3600)
    