from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.flipkart.com/")

driver.maximize_window()

# Mouse hover on womens
actions = ActionChains(driver, duration=1500)
fashion_hover = driver.find_element(By.XPATH,'//span[text()="Fashion"]')
actions.move_to_element(fashion_hover).perform()
womens_footwear = driver.find_element(By.XPATH,'//a[contains(@href,"/womens-footwear/") and @class="_1BJVlg"]')
actions.move_to_element(womens_footwear).perform()
womens_heel = driver.find_element(By.XPATH,'//a[contains(@href,"/womens-footwear/heels/") and text()="Women Heels"]')
actions.click(womens_heel).perform()
time.sleep(2)
driver.execute_script("window.scrollBy(0,2000);")

time.sleep(3)
# search product
searchbar = driver.find_element(By.NAME,'q')
searchbar.send_keys("suit for women")
searchbar.send_keys(Keys.ENTER)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//img[@class="_53J4C-"]')))

allproduct = driver.find_elements(By.XPATH,'//img[@class="_53J4C-"]')
print("no. of src img",len(allproduct))

# fetch all source  src of image
for i in allproduct:
    val = i.get_attribute('src')
    print(val)

# scrolling page 5 times by page down key
for _ in range(5):
    driver.find_element(By.TAG_NAME,"body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)

time.sleep(3)

# choose any item and click
choose_product = driver.find_element(By.XPATH,'(//img[@class="_53J4C-"])[9]')
choose_product.click()
time.sleep(4)

driver.switch_to.window(driver.window_handles[1])
time.sleep(3)

# add to cart an item
add_to_cart = driver.find_element(By.XPATH,'//button[text()="Add to cart"]')

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to cart']")))

# smooth scrolling by pixel
for _ in range(6):
    driver.execute_script("window.scrollBy(0,400);")
    time.sleep(0.5)

add_to_cart.click()

time.sleep(2)
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)

# click on cart to verify product added or not
cart_view = driver.find_element(By.XPATH,'//span[text()="Cart"]')
cart_view.click()
time.sleep(3)

cart_product_name = driver.find_element(By.XPATH,'//a[contains(text(),"Women Kurta")]')
val = cart_product_name.text
print("Product name",val)
cart_product_price = driver.find_element(By.XPATH,'//span[@class="LAlF6k re6bBo" and contains(text(),"₹")]')
val1 = cart_product_price.text
print("Product price",val1)


# assert "Women Kurta" in val, "product not found in cart"
if "Women Kurta" in val:
    print("product successfully added to cart")
else:
    print("not added to cart")

# remove product from cart
remove_product = driver.find_element(By.XPATH,'//div[text()="Remove"]')
remove_product.click()
time.sleep(3)

# alert pop ups are shown
popup_remove = driver.find_element(By.XPATH,'//div[text()="Remove"]')
popup_remove.click()
time.sleep(3)
# driver.switch_to.alert.accept()

# verify that product is remove or not from cart
empty_cart = driver.find_element(By.XPATH,'//div[text()="Missing Cart items?" or text()="Your cart is empty"]')

# Using assert to verify that the cart is empty
assert empty_cart.is_displayed(), "The cart is not empty!"

# Step 5: Print success message if assertion passes
print("Assertion passed: The cart is empty.")

driver.quit()