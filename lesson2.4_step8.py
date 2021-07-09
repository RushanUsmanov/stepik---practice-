import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


# функция для подсчета формулы
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# Будет запускаться только из виртуального окружения в консоли
browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ждем появление кнопки 5 секунд
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    button = browser.find_element_by_id("book")
    button.click()

    x = browser.find_element_by_id("input_value")
    x = x.text
    y = calc(x)

    field = browser.find_element_by_id("answer")
    field.send_keys(y)

    submit = browser.find_element_by_id("solve")
    submit.click()

finally:
    time.sleep(4)
    browser.quit()
