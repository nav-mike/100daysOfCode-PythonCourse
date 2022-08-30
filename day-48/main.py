from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime, timedelta

chrome_driver = "/Applications/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver)

# driver.get("https://www.amazon.com/dp/B07RTSW8JS/ref=syn_sd_onsite_desktop_154?ie=UTF8&psc=1&pd_rd_plhdr=t")
#
# price = driver.find_element(by=By.CLASS_NAME, value="a-offscreen")
# print(price)
# print(price.get_attribute('textContent'))
#
# driver.get("https://python.org")
#
# events = driver.find_elements(
#     by=By.CSS_SELECTOR,
#     value="#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul li"
# )
#
# events_dict = {}
# index = 0
#
# for event in events:
#     values = event.get_attribute('textContent').strip().split('\n')
#     events_dict[index] = {'time': values[0], 'name': values[1]}
#     index += 1
#
# print(events_dict)
#
#
# driver.quit()

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# articles_count = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount > a:nth-child(1)")
#
# print(articles_count.get_attribute('textContent'))
#
# search_input = driver.find_element(by=By.CSS_SELECTOR, value="#searchInput")
# search_input.send_keys("Python", Keys.ENTER)

# driver.get("http://secure-retreat-92358.herokuapp.com/")
#
# first_name_input = driver.find_element(by=By.CSS_SELECTOR, value="body > form > input.form-control.top")
# first_name_input.send_keys("Somename")
#
# last_name_input = driver.find_element(by=By.CSS_SELECTOR, value="body > form > input.form-control.middle")
# last_name_input.send_keys("Somelastname")
#
# email_input = driver.find_element(by=By.CSS_SELECTOR, value="body > form > input.form-control.bottom")
# email_input.send_keys("some-email@gmail.com")
#
# button = driver.find_element(by=By.CSS_SELECTOR, value="body > form > button")
# button.click()
#
# success = driver.find_element(by=By.CSS_SELECTOR, value="body > div > h1")
#
# if success.get_attribute('textContent') == "Success!":
#     print("Success!")

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(by=By.CSS_SELECTOR, value="#cookie")

start_time = datetime.now()
prev_time = start_time

while True:
    cookie.click()
    current_time = datetime.now()
    if current_time - prev_time > timedelta(minutes=5):
        break

    if current_time - prev_time > timedelta(seconds=5):
        prev_time = current_time
        cookie_count = int(
            driver.find_element(by=By.CSS_SELECTOR, value="#money").get_attribute('textContent').replace(',', '')
        )

        if cookie_count >= 123456789:
            driver.find_element(by=By.XPATH, value='"//*[@id="buyTime machine"]"').click()
        elif cookie_count >= 1000000:
            driver.find_element(by=By.CSS_SELECTOR, value='#buyPortal').click()
        elif cookie_count >= 50000:
            driver.find_element(by=By.XPATH, value='//*[@id="buyAlchemy lab"]').click()
        elif cookie_count >= 7000:
            driver.find_element(by=By.XPATH, value='//*[@id="buyShipment"]').click()
        elif cookie_count >= 2000:
            driver.find_element(by=By.XPATH, value='//*[@id="buyMine"]').click()
        elif cookie_count >= 500:
            driver.find_element(by=By.XPATH, value='//*[@id="buyFactory"]').click()
        elif cookie_count >= 100:
            driver.find_element(by=By.XPATH, value='//*[@id="buyGrandma"]').click()
        elif cookie_count >= 15:
            driver.find_element(by=By.XPATH, value='//*[@id="buyCursor"]').click()

cookie_count = int(driver.find_element(by=By.CSS_SELECTOR, value="#money").get_attribute('textContent'))
print(cookie_count)

driver.quit()
