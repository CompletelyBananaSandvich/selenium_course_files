from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/selects1.html"
    browser.get(link)

    time.sleep(1)

    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)

    selector = Select(browser.find_element(By.ID, "dropdown"))
    selector.select_by_value(f"{num1 + num2}")

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    submit.click()
    
finally:
    time.sleep(10)
    browser.quit()
