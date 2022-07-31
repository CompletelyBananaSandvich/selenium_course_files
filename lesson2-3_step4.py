from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

def calculate(value):
    return str(math.log(abs(12*math.sin(int(value)))))

try:
        
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    time.sleep(1)

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit.click()

    alert = browser.switch_to.alert
    alert.accept()

    input_value = browser.find_element(By.ID, "input_value").text
    answer_window = browser.find_element(By.ID, "answer")

    answer_window.send_keys(calculate(input_value))

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit.click()

finally:
    alert = browser.switch_to.alert
    answer = alert.text
    answer.copy()
    time.sleep(10)
    browser.quit()
    
