from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

num_element = browser.find_element_by_id("input_value")
num = num_element.text

y = calc(num)



element = browser.find_element_by_id("answer")
element.send_keys(y)
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true)", button)
option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
option1.click()

option2 = browser.find_element_by_css_selector("[id='robotsRule']")
option2.click()

button.click()