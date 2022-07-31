from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
import math
import time

def calculate(value):
    return str(math.log(abs(12*math.sin(int(value)))))

try:
        
    browser = webdriver.Chrome()

    link = "http://suninjuly.github.io/explicit_wait2.html"

    browser.get(link)

    price = WebDriverWait(browser, 15).until(ES.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button = browser.find_element(By.ID, "book")
    button.click()

    input_value = browser.find_element(By.ID, "input_value").text

    answer_window = browser.find_element(By.ID, "answer")
    answer_window.send_keys(calculate(input_value))

    submit = browser.find_element(By.ID, "solve")
    submit.click()

finally:
    
    time.sleep(10)
    browser.quit()
