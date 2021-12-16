from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import veebileht.constants
from bs4 import BeautifulSoup
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_experimental_option('excludeSwitches', ['enable-logging'])
from random import randint

def run():

    s = Service("veebileht\webdriver\chromedriver.exe")
    browser = webdriver.Chrome(service = s, options=option)
    browser.get("http://facebook.com")
    browser.maximize_window()
    wait = WebDriverWait(browser, 30)
    email_field = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
    email_field.send_keys(veebileht.constants.account['email'])
    pass_field = wait.until(EC.visibility_of_element_located((By.NAME, 'pass')))
    pass_field.send_keys(veebileht.constants.account['pass'])
    pass_field.send_keys(Keys.RETURN)
    time.sleep(5)

    event_list = []

    for i in range(len(veebileht.constants.pages)):
        currentpage = (list(veebileht.constants.pages.values()))[i]
        browser.get(currentpage)
        time.sleep(5)
        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')
        temp = []
        event_dict = {}

        for z in soup.find(class_ = 'rq0escxv l9j0dhe7 du4w35lb hybvsw6c io0zqebd m5lcvass fbipl8qg nwvqtn77 k4urcfbm ni8dbmo4 stjgntxs sbcfpzgs'):
            for i in z.find_all(class_=veebileht.constants.cons['mains']):
            #print(i)
                if str(veebileht.constants.cons['dates_class']) in str(i):
                
                #for x in i.find_all(class_ = constants.cons['current_page']):
                #    event_dict["Current_Page"] = x.text

                    for j in i.find_all(class_=veebileht.constants.cons['names_class']):

                        if not len(j.text) == '':
                            event_dict["Event_Name"] = j.text
                            #print(j.text)
                        else:
                            event_dict["Event_Name"] = 'NONE'
                    for g in i.find_all(class_=veebileht.constants.cons['place_class']):
                        if not len(g.text) == '':
                            event_dict["Event_Place"] = g.text
                        else:
                            event_dict["Event_Place"] = 'NONE'
                    for h in i.find_all(class_=veebileht.constants.cons['dates_class']):
                        if not len(h.text) == '':
                            event_dict["Event_Time"] = h.text
                            #print(h)
                        else:
                            event_dict["Event_Time"] = 'NONE'
                    temp.append(event_dict)
        event_list.append(temp)

    return event_list
