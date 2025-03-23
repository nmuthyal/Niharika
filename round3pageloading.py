

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def url_locator():
    load = []
    for _ in range(10):
        driver = webdriver.Chrome()
        driver.get('https://mathup.com/games/crossbit?mode=daily_challenge')
        start_time=time.time()

        start_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@class='GamePostStart_btn__yoMra btn ']")))
        end_time=time.time()
        times = end_time - start_time
        print(f'{times:.2f} seconds')
        load.append(times)
    avg_time = sum(load)/len(load)
    print(f'AVG time for 10 times of page is {avg_time:.2f} seconds')

text = url_locator()
