import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector('#treasure')
people_checked = x_element.get_attribute('valuex')
x = people_checked
y = calc(x)

element1 = browser.find_element_by_css_selector('#answer')
element1.send_keys(y)

option1 = browser.find_element_by_css_selector("#robotCheckbox")
option1.click()
option2 = browser.find_element_by_css_selector("#robotsRule")
option2.click()
option2 = browser.find_element_by_css_selector("[type='submit']")
option2.click()

time.sleep(5)
browser.quit()
