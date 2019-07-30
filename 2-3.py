from selenium import webdriver
import os 

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

element1 = browser.find_element_by_xpath("//div[@class='form-group']//input[contains(@name, 'firstname')]")
element1.send_keys("Мой ответ")
element2 = browser.find_element_by_xpath("//div[@class='form-group']//input[contains(@name, 'lastname')]")
element2.send_keys("Мой ответ")
element3 = browser.find_element_by_xpath("//div[@class='form-group']//input[contains(@name, 'email')]")
element3.send_keys("Мой ответ")

file_element = browser.find_element_by_css_selector("[type='file']")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, '1.txt')
file_element.send_keys(file_path)

button = browser.find_element_by_css_selector("button")
button.click()