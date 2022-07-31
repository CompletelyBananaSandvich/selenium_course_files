from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calculate(value):
    return str(math.log(abs(12*math.sin(int(value)))))
try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/execute_script.html"
    browser.get(link)

    time.sleep(1)
    
    input_value = browser.find_element(By.ID, "input_value").text
    input_box = browser.find_element(By.ID, "answer")
    input_box.send_keys(calculate(input_value))

    time.sleep(1)

    captcha = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", captcha)
    captcha.click()

    radiobutton = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()
    
    submit = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()

finally:
    
    time.sleep(10)
    browser.quit()
    
