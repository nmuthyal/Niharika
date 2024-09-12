from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configure WebDriver (headless for faster execution, you can turn off headless mode if you want to see the browser)
chrome_options = Options()
chrome_options.add_argument("--headless")
service = Service(executable_path=r'C:\Users\mutab\Downloads\chromedriver-win64\chromedriver.exe')  # Adjust this path as needed

# Start WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# 1. Open amazon.in
driver.get("https://www.amazon.in")

# Maximize the window (optional)
driver.maximize_window()

# Allow page to load
time.sleep(3)

# 2. Search for 'lg soundbar'
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("lg soundbar")
search_box.submit()

# Allow the search results to load
time.sleep(3)

# 3. Read product names and prices on the first search result page
products = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']"))
)
prices = driver.find_elements(By.XPATH, "//span[@class='a-price-whole']")

# Create dictionary to store product name and price pairs
product_price_map = {}

# Iterate over the products and prices and populate the dictionary
for i, product in enumerate(products):
    product_name = product.text
    try:
        price = int(prices[i].text.replace(",", ""))  # Remove commas from price and convert to integer
    except (IndexError, ValueError):
        price = 0  # Consider missing price as zero
    product_price_map[product_name] = price

# 4. Sort products by price
sorted_products = sorted(product_price_map.items(), key=lambda x: x[1])

# 5. Print sorted products by price, skipping the first two items
for product_name, price in sorted_products[2:]:
    print(f"{price} {product_name}")

# Close the browser
driver.quit()
