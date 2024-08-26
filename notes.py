from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.maximize_window()

# Open Flipkart
driver.get("https://www.flipkart.com")

# Handle the login popup if it appears
# try:
#     close_login_popup = driver.find_element(By.XPATH, "//button[contains(text(),'✕')]")
#     close_login_popup.click()
# except:
#     pass

# Pause to let the page load
time.sleep(2)

# 1. Scroll Down by Pixel Amount
driver.execute_script("window.scrollBy(0, 1000);")
time.sleep(3)

# 2. Scroll to the Bottom of the Page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

# 3. Scroll to a Specific Element (e.g., Footer)
footer_element = driver.find_element(By.XPATH, "//footer")
driver.execute_script("arguments[0].scrollIntoView();", footer_element)
time.sleep(3)

# 4. Scroll Horizontally (if applicable)
driver.execute_script("window.scrollBy(500, 0);")  # Scroll right
time.sleep(3)
driver.execute_script("window.scrollBy(-500, 0);")  # Scroll left
time.sleep(3)

# 5. Scroll Using the PAGE_DOWN and PAGE_UP Keys
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
time.sleep(3)

driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_UP)
time.sleep(2)

# 6. Scroll Using the ARROW_DOWN and ARROW_UP Keys
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_DOWN)
time.sleep(2)

driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_UP)
time.sleep(2)

# 7. Smooth Scrolling Down
for _ in range(5):
    driver.execute_script("window.scrollBy(0, 300);")  # Scroll down by 300 pixels
    time.sleep(0.5)

# 8. Smooth Scrolling Up
for _ in range(5):
    driver.execute_script("window.scrollBy(0, -300);")  # Scroll up by 300 pixels
    time.sleep(0.5)

# Final Wait and Close the Browser
time.sleep(2)
driver.quit()
