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

searchbar = driver.find_element(By.NAME,'q')
searchbar.send_keys("suit for women")
searchbar.send_keys(Keys.ENTER)


driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")