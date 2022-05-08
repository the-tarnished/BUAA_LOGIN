###CONFIG
username = ""
password = ""
typeOfDriver = "Firefox" ##Firefox Edge Chrome
url = "https://gw.buaa.edu.cn/srun_portal_pc?ac_id=1&theme=buaa"
### END CONFIG



### import
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
import logging
import time

browser = None
logging.basicConfig(level=logging.INFO,format = '%(asctime)s - %(levelname)s: %(message)s')

def initBrowser() :
    global browser
    if typeOfDriver == "Chrome":
        option = ChromeOptions()
        option.add_experimental_option('excludeSwitches',['enable-automation'])
        option.add_experimental_option('useAutomationExtension',False)
        browser = webdriver.Chrome(options = option)
        browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',{'source':'Object.defineProperty(navigator,"webdriver",{get:() => undefined})'})
    elif typeOfDriver == "Firefox":
        browser = webdriver.Firefox()
    else :
        logging.info("Wrong Driver Type")

def connect() :
    browser.get(url)
    try:
        usernameInput = browser.find_element(By.ID,"username")
        logging.info("Input username")
        usernameInput.send_keys(username)
        time.sleep(1)
        passwordInput = browser.find_element(By.ID,"password")
        logging.info("Input password")
        passwordInput.send_keys(password)
        time.sleep(1)
        button = browser.find_element(By.ID,"login")
        logging.info("Login")
        button.click()
    except:
        logging.info("Already Login")
    browser.close()
if __name__ == "__main__":
    initBrowser()
    connect()
