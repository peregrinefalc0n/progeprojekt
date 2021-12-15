from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import constants
from bs4 import BeautifulSoup
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_experimental_option('excludeSwitches', ['enable-logging'])
from random import randint

def login():
    s = Service("C:\webdrivers\chromedriver.exe")
    browser = webdriver.Chrome(service = s, options=option)
    browser.get("http://facebook.com")
    browser.maximize_window()
    wait = WebDriverWait(browser, 30)
    email_field = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
    email_field.send_keys(constants.account['email'])
    pass_field = wait.until(EC.visibility_of_element_located((By.NAME, 'pass')))
    pass_field.send_keys(constants.account['pass'])
    pass_field.send_keys(Keys.RETURN)
    time.sleep(5)
    return browser

def scrape_page(browser, currentpage):
    browser.get(currentpage)
    time.sleep(5)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')

    event_dict = {}

    for i in soup.find_all(class_=constants.cons['mains']):
    
        if str(constants.cons['dates_class']) in str(i):
            event_dict['Page_Name'] = constants.cons['current_page'].text

            for j in i.find_all(class_=constants.cons['names_class']):
                
                if not len(j.text) == '':
                    event_dict["Event_Name"] = j.text
                else:
                    event_dict["Event_Name"] = 'NONE'
            for g in i.find_all(class_=constants.cons['place_class']):
                if not len(g.text) == '':
                    event_dict["Event_Place"] = g.text
                else:
                    event_dict["Event_Place"] = 'NONE'
            for h in i.find_all(class_=constants.cons['dates_class']):
                if not len(h.text) == '':
                    event_dict["Event_Time"] = h.text
                else:
                    event_dict["Event_Time"] = 'NONE'

    return event_dict

login_ = login()
event_dict = []
while 1>0:
    for i in range(len(constants.pages)):
        event_dict.append(scrape_page(login_, (list(constants.pages.values())[i])))
    print(event_dict)
    time.sleep(randint(60, 120) * 60)
        
