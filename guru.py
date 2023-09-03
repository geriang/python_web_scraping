from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.propertyguru.com.sg/")

search_field = driver.find_element(By.CSS_SELECTOR, "input.rbt-input-main.form-control.rbt-input")
search_field.send_keys("Bukit Batok")

search_button = driver.find_element(By.CSS_SELECTOR, "span.search-panel-group-text.input-group-text")
search_button.click()
# username = driver.find_element(By.NAME, "username")
# username.send_keys("XXXXXXXX")
# # username.send_keys(Keys.ENTER)
#
# password = driver.find_element(By.NAME, "password")
# password.send_keys("XXXXXXXXX")
# #
# submit = driver.find_element(By.TAG_NAME, "button")
# submit.click()

