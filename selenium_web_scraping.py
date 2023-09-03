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

    n = len(companies)
    time.sleep(5)
    for count in range(59):
        time.sleep(5)
        for coy in range(n):
            print(coy)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.list-group.list-group-flush")))
            company_list = driver.find_element(By.CSS_SELECTOR, "div.list-group.list-group-flush")
            companies = company_list.find_elements(By.TAG_NAME, "a")
            driver.execute_script("arguments[0].click();", companies[coy])
            company_info = driver.find_elements(By.CSS_SELECTOR, "ul.list-group.list-group-flush")

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

            time.sleep(5)
            driver.back()
            time.sleep(7)
            print("Done")

        #click next command
        next_button = driver.find_element(By.CSS_SELECTOR, "a.page-link[title='next']")

    driver.quit()

except Exception as e:
    print(f"An error occurred: {e}")



