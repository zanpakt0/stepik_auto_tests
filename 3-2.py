from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("button")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

num_element = browser.find_element_by_id("input_value")
num = num_element.text

y = calc(num)



element = browser.find_element_by_id("answer")
element.send_keys(y)

button = browser.find_element_by_css_selector("button")
button.click()