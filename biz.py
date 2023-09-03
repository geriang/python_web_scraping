# import time
# from undetected_chromedriver import Chrome
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# # chrome = Chrome()
# # chrome.get("https://www.sgpbusiness.com/activities/industrial-classification/Real-Estate-Activities/Real-Estate-Activities/Real-Estate-Activities-With-Own-Or-Leased-Property/Real-Estate-Activities-With-Own-Or-Leased-Property/Letting-Of-Self-owned-Or-Leased-Real-Estate-Property-Except-Food-Courts-Coffee-Shops-And-Eating-Houses-Eg-Office-Or-Exhibition-Space-Shopping-Mall-Self-storage-Facilities")
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.sgpbusiness.com/activities/industrial-classification/Real-Estate-Activities/Real-Estate-Activities/Real-Estate-Activities-With-Own-Or-Leased-Property/Real-Estate-Activities-With-Own-Or-Leased-Property/Letting-Of-Self-owned-Or-Leased-Real-Estate-Property-Except-Food-Courts-Coffee-Shops-And-Eating-Houses-Eg-Office-Or-Exhibition-Space-Shopping-Mall-Self-storage-Facilities")
#
# # company_list = chrome.find_element(By.CSS_SELECTOR, "div.list-group.list-group-flush")
# company_list = driver.find_element(By.CSS_SELECTOR, "div.list-group.list-group-flush")
# companies = company_list.find_elements(By.TAG_NAME, "a")
# print(companies[0].text)
# wait = WebDriverWait(driver, 30)
#
# element = wait.until(EC.element_to_be_clickable(companies[0]))
# element.click()
# time.sleep(20)
# companies[0].click()

# time.sleep(3)
# company_info = driver.find_elements(By.CSS_SELECTOR, "ul.list-group.list-group-flush")
# for n in company_info:
#     print(n.text)
# print(company_list)
# for n in companies:
#     print(n.text)


import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

df = pd.DataFrame(columns=["UEN", "Company Name", "Registration Date", "Status", "Street", "Unit", "Postal Code"])

try:
    chrome_options = uc.ChromeOptions()
    # chrome_options.add_experimental_option("detach", True)
    # chrome_options.add_argument('--ignore-certificate-errors')
    # chrome_options.add_argument('--ignore-ssl-errors')

    # Initialize the Chrome driver using undetected_chromedriver
    driver = uc.Chrome(options=chrome_options)

    driver.get(
        "https://www.sgpbusiness.com/activities/industrial-classification/Real-Estate-Activities/Real-Estate-Activities/Real-Estate-Activities-With-Own-Or-Leased-Property/Real-Estate-Activities-With-Own-Or-Leased-Property/Letting-Of-Self-owned-Or-Leased-Real-Estate-Property-Except-Food-Courts-Coffee-Shops-And-Eating-Houses-Eg-Office-Or-Exhibition-Space-Shopping-Mall-Self-storage-Facilities")

    wait = WebDriverWait(driver, 40)  # Increased time to 40 seconds for debugging

    # Ensure the list is loaded
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.list-group.list-group-flush")))

    company_list = driver.find_element(By.CSS_SELECTOR, "div.list-group.list-group-flush")
    companies = company_list.find_elements(By.TAG_NAME, "a")

    # print(f"First company text: {companies[0].text}")  # Debugging information

    companies[0].click()

    company_info = driver.find_elements(By.CSS_SELECTOR, "ul.list-group.list-group-flush")
    # for n in company_info:
    # company_name_uen = company_info[0].find_elements(By.CSS_SELECTOR, "span[itemprop='name']")
    # print(f"UEN:{company_name_uen[0].text}")
    # print(f"Company Name:{company_name_uen[1].text}")
    # company_founding = company_info[0].find_element(By.CSS_SELECTOR, "span[itemprop='foundingDate']")
    # print(f"Company Reg. Date:{company_founding.text}")
    # company_status = company_info[0].find_element(By.CSS_SELECTOR, "span.text-success")
    # print(f"Company Status:{company_status.text}")
    # company_street = company_info[1].find_element(By.CSS_SELECTOR, "span[itemprop='streetAddress']").text.split("\n")
    # print(f"Street Address:{company_street[0]}")
    # print(f"unit: {company_street[1]}")
    # print(f"building: {company_street[2]}")
    # company_postal = company_info[1].find_element(By.CSS_SELECTOR, "span[itemprop='postalCode']")
    # print(f"Postal Code: Singapore {company_postal.text}")

    company_name_uen = company_info[0].find_elements(By.CSS_SELECTOR, "span[itemprop='name']")
    company_founding = company_info[0].find_element(By.CSS_SELECTOR, "span[itemprop='foundingDate']")
    company_status = company_info[0].find_element(By.CSS_SELECTOR, "span.text-success")
    company_street = company_info[1].find_element(By.CSS_SELECTOR, "span[itemprop='streetAddress']").text.split(
        "\n")
    company_postal = company_info[1].find_element(By.CSS_SELECTOR, "span[itemprop='postalCode']")
    new_row = pd.DataFrame({
        "UEN": [company_name_uen[0].text],
        "Company Name": [company_name_uen[1].text],
        "Registration Date": [company_founding.text],
        "Status": [company_status.text],
        "Street": [company_street[0]],
        "Unit": [company_street[1]],
        "Postal Code": [company_street[2]]
    })

    df = pd.concat([new_row], ignore_index=True)
    df.to_csv('company_data.csv')

    # time.sleep(5)
    #
    # wait = WebDriverWait(driver, 40)  # Increased time to 40 seconds for debugging
    # wait.until(EC.presence_of_element_located((By.LINK_TEXT,
    #                                            "LETTING OF SELF-OWNED OR LEASED REAL ESTATE PROPERTY EXCEPT FOOD COURTS, COFFEE SHOPS AND EATING HOUSES (E.G. OFFICE/EXHIBITION SPACE, SHOPPING MALL, SELF-STORAGE FACILITIES)")))
    # element = driver.find_element(By.LINK_TEXT, "LETTING OF SELF-OWNED OR LEASED REAL ESTATE PROPERTY EXCEPT FOOD COURTS, COFFEE SHOPS AND EATING HOUSES (E.G. OFFICE/EXHIBITION SPACE, SHOPPING MALL, SELF-STORAGE FACILITIES)")
    # driver.execute_script("arguments[0].click();", element)
    #
    # time.sleep(10)
    #
    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.list-group.list-group-flush")))
    #
    # company_list = driver.find_element(By.CSS_SELECTOR, "div.list-group.list-group-flush")
    # companies = company_list.find_elements(By.TAG_NAME, "a")
    #
    # # print(f"First company text: {companies[0].text}")  # Debugging information
    #
    # driver.execute_script("arguments[0].click();", companies[2])
    #
    # company_info = driver.find_elements(By.CSS_SELECTOR, "ul.list-group.list-group-flush")
    # for n in company_info:
    #     print(n.text)

    time.sleep(10)
    # go_back = driver.find_element(By.LINK_TEXT, "LETTING OF SELF-OWNED OR LEASED REAL ESTATE PROPERTY EXCEPT FOOD COURTS, COFFEE SHOPS AND EATING HOUSES (E.G. OFFICE/EXHIBITION SPACE, SHOPPING MALL, SELF-STORAGE FACILITIES)")
    # go_back.click()





    # driver.back()
    # time.sleep(2)
    #
    # wait = WebDriverWait(driver, 40)  # Increased time to 40 seconds for debugging
    #
    # # Ensure the list is loaded
    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.list-group.list-group-flush")))
    #
    # company_list = driver.find_element(By.CSS_SELECTOR, "div.list-group.list-group-flush")
    # companies = company_list.find_elements(By.TAG_NAME, "a")
    #
    # companies[1].click()
    #
    # company_info = driver.find_elements(By.CSS_SELECTOR, "ul.list-group.list-group-flush")
    # for n in company_info:
    #     print(n.text)
    #
    # time.sleep(20)

except Exception as e:
    print(f"An error occurred: {e}")



