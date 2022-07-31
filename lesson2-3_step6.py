from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calculate(value):
    return str(math.log(abs(12*math.sin(int(value)))))

try:
        
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    time.sleep(1)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    browser.switch_to.window(browser.window_handles[1])

    value = browser.find_element(By.ID, "input_value").text
    answer_window = browser.find_element(By.ID, "answer")
    answer_window.send_keys(calculate(value))

    submit = browser.find_element(By.TAG_NAME, "button")
    submit.click()

finally:

    time.sleep(10)
    browser.quit()
    
