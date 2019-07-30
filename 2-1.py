from selenium import webdriver
from selenium.webdriver.support.ui import Select
# select = Select(browser.find_element_by_tag_name("select"))
# select.select_by_value("1") # ищем элемент с текстом "Python"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

num1_element = browser.find_element_by_id("num1")
num1 = num1_element.text
num2_element = browser.find_element_by_id("num2")
num2 = num2_element.text

mySum = int(num1)+int(num2)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(mySum))

option3 = browser.find_element_by_css_selector("button")
option3.click()
