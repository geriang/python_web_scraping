from selenium import webdriver
from selenium.webdriver.common.by import By
import threading

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")
buy_cursor = driver.find_element(By.CSS_SELECTOR, "#buyCursor")


def end_program():
    cookie_numbers_int = get_cookie_num()
    print(f"Number of cookies per second: {cookie_numbers_int/20}")
    driver.quit()


def get_cookie_num():
    cookie_numbers = driver.find_element(By.CSS_SELECTOR, "#money")
    return int(cookie_numbers.text.replace(",", ""))


threading.Timer(120, end_program).start()

program_is_on = True


def click_grandma():
    buy_grandma = driver.find_element(By.CSS_SELECTOR, "#buyGrandma")
    buy_grandma.click()
    threading.Timer(7, click_grandma).start()


threading.Timer(7, click_grandma).start()
while program_is_on:
    cookie_count = get_cookie_num()
    cookie.click()
    # print(cookie_count)



