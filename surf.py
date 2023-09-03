from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Henry")

second_name = driver.find_element(By.NAME, "lName")
second_name.send_keys("Ang")

email = driver.find_element(By.NAME, "email")
email.send_keys("henry@ang.com")

button = driver.find_element(By.CSS_SELECTOR, ".btn")
button.send_keys(Keys.ENTER)


