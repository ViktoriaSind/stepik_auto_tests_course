import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)

element1 = browser.find_element_by_name('firstname')
element1.send_keys("Vika")
element2 = browser.find_element_by_name('lastname')
element2.send_keys("Sindi")
element3 = browser.find_element_by_name('email')
element3.send_keys("123")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element_by_css_selector("[type='file']")
element.send_keys(file_path)

option2 = browser.find_element_by_css_selector("[type='submit']")
option2.click()

time.sleep(10)
browser.quit()