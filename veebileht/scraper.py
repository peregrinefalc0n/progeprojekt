from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from veebileht import constants
# other necessary ones
from bs4 import BeautifulSoup


def scrape_page():
    
    option = Options()
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    browser = webdriver.Chrome(executable_path="veebileht\webdriver\chromedriver.exe", options=option)
    browser.get("http://facebook.com")
    browser.maximize_window()
    wait = WebDriverWait(browser, 30)
    email_field = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
    email_field.send_keys(constants.EMAIL)
    pass_field = wait.until(EC.visibility_of_element_located((By.NAME, 'pass')))
    pass_field.send_keys(constants.PASSWORD)
    pass_field.send_keys(Keys.RETURN)
    time.sleep(5)

    browser.get('https://www.facebook.com/MITS.ATI/events/?ref=page_internal')
    time.sleep(5)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
        
    name_list = []
    place_list = []
    date_list = []

    for i in soup.find_all(class_=constants.mains):

        #j => Event name
        for j in i.find_all(class_=constants.names_class):
        #g => Event Place
            if not len(j.text) == '':
                name_list.append(j.text)
            else:
                name_list.append('NONE')
        for g in i.find_all(class_=constants.place_class):
            if not len(g.text) == '':
                place_list.append(g.text)
            else:
                place_list.append('NONE')
        for h in i.find_all(class_=constants.dates_class):
        
            if not len(h.text) == '':
                date_list.append(h.text)
            else:
                date_list.append('NONE')
        

    retlist = [name_list, place_list, date_list]

    return retlist


#GET INFO FROM THESE CLASSES

#print([item.text for item in soup.find_all(class_=mains)])

###DATES 
#print([item.text for item in soup.find_all(class_=names_class)])
#print([item.text for item in soup.find_all(class_=dates_class)])
#print([item.text for item in soup.find_all(class_=place_class)])

#for i in soup.find_all('div', attrs={'class': mains}):
#    i_descendants = i.descendants
#    for d in i_descendants:
#        if d.name == 'div' and d.get('class', '') == [dates_class]:
#            print(d.text)
#
#div = soup.find_all('div', {'class': mains})
#for i in div:
#    print(*i.descendants)

            
    

