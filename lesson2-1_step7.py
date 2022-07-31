from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    value = browser.find_element(By.CSS_SELECTOR, "img[id = 'treasure']").get_attribute("valuex")
    answer = calc(value)

    answer_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_field.send_keys(answer)

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
 
