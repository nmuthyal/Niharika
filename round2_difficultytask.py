import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def url_locator():
    driver= webdriver.Chrome()
    driver.get('https://mathup.com/games/crossbit?mode=championship')
    start_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@class='GamePostStart_btn__yoMra btn ']")))
    start_button.click()
    for _ in range(10):
        elements = driver.find_element(By.XPATH, "(//*[@class='GamePostStart_value__zH0b9'])[4]")
        print(elements.text)

text = url_locator()