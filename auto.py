from selenium import webdriver
import time

link = "https://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
element1 = browser.find_element_by_xpath("//div[@class='first_block']//input[contains(@class, 'first')]")
element1.send_keys("Мой ответ")
element2 = browser.find_element_by_xpath("//div[@class='first_block']//input[contains(@class, 'second')]")
element2.send_keys("Мой ответ")
element3 = browser.find_element_by_xpath("//div[@class='first_block']//input[contains(@class, 'third')]")
element3.send_keys("Мой ответ")

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text