from selenium import webdriver
from selenium.webdriver.common.by import By

# keep chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

events = driver.find_element(By.CSS_SELECTOR, "div.medium-widget.event-widget.last")
events_time = events.find_elements(By.TAG_NAME, "time")
events_name = events.find_elements(By.TAG_NAME, "a")
# solution
# events_time = driver.find_elements(By.CSS_SELECTOR, "event-widget time")
# events_name = driver.find_elements(By.CSS_SELECTOR, "event-widget li a")

# events = {}
# for n in range(len(events_time)):
#     events[n] = {
#                 "time": events_time[n].text,
#                 "name": events_name[n+1].text
#                  }

events = {n: {"time": events_time[n].text, "name":events_name[n+1].text} for n in range(len(events_time))}

print(events)

driver.quit()
