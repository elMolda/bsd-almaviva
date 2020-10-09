import time
import threading
from selenium import webdriver

with open('caso.txt') as f:
    cases = f.readlines()


cases = [c.rstrip() for c in cases]

def view_case(case):
    browser = webdriver.Chrome()
    browser.get('http://bsd.open-eb.io#/pages/login')

    email = 'lmolano@almaviva.com.co'
    pwd = 'Opencomex2019'

    email_input_id = "mat-input-1"
    password_input_id = "mat-input-2"
    login_btn_selector = ".submit-button > .mat-button-wrapper"
    search_bar_selector = ".fuse-search-bar-expander"
    search_bar_input_id = "fuse-search-bar-input"

    browser.find_element_by_id(email_input_id).clear()
    browser.find_element_by_id(email_input_id).send_keys(email)
    browser.find_element_by_id(password_input_id).clear()
    browser.find_element_by_id(password_input_id).send_keys(pwd)
    browser.find_element_by_css_selector(login_btn_selector).click()

    time.sleep(0.3)
    browser.find_element_by_css_selector(search_bar_selector).click()
    browser.find_element_by_id(search_bar_input_id).send_keys(case)
    #time.sleep(600)

thread_list = []

for case in cases:
    t = threading.Thread(name=f'Caso: {case}', target=view_case, args=[case])
    t.start()
    time.sleep(1)
    print(f'Viewing {t.name}')
    thread_list.append(t)

#for thread in thread_list:
#    thread.join()
    
print('Finish viewing cases')
