from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    time.sleep(1)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'lesson2-2_step8.txt')

    input_windows = browser.find_elements(By.TAG_NAME, "input")
    input_values = ["Censored", "Censored", "Censored", file_path]

    for i in range(len(input_windows)):
        input_windows[i].send_keys(input_values[i])

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit.click()
    
finally:

    time.sleep(10)
    browser.quit()
    
