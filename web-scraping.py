from selenium import webdriver
import time

driver = webdriver.Chrome() 
URL = "https://www.zoopla.co.uk/new-homes/property/london/?q=London&results_sort=newest_listings&search_source=new-homes&page_size=25&pn=1&view_type=list"
driver.get(URL)

time.sleep(2) # Wait a couple of seconds, so the website doesn't suspect you are a bot
try:
    driver.switch_to.frame('gdpr-consent-notice') # This is the id of the frame
    accept_cookies_button = driver.find_element('xpath', '//*[@id="save"]')
    accept_cookies_button.click()

except:
    pass # If there is no cookies button, we won't find it, so we can pass

time.sleep(2)
property = driver.find_element('xpath', '//*[@id="listing_61870745"]')
a_tag = property.find_element('tag name', 'a')
link = a_tag.get_attribute('href')
print(link)

driver.get(link)