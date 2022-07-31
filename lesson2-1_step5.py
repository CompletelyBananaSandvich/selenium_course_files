from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "span[id = 'input_value']")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)

    flag_1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    flag_1.click()

    flag_2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    flag_2.click()

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    submit.click()

    time.sleep(1)

finally:
    time.sleep(10)

    browser.quit()
 
