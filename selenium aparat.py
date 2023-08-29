import time

#for driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#for access the elements
from selenium.webdriver.common.by import By
#to send keys
from selenium.webdriver import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://aparat.com')

search_box = driver.find_element(By.ID, "search")
search_box.send_keys("موزیک ویدیو مازیار فلاحی")
search_box.send_keys(Keys.ENTER)

time.sleep(6)

list_links = driver.find_elements(By.CLASS_NAME, "grid-item")
a_tag_list = []
for list_link in list_links:
    atag = list_link.find_element(By.XPATH, ".//a")
    print(atag.get_attribute('href'))
    a_tag_list.append(atag.get_attribute('href'))

print(a_tag_list)

for link in a_tag_list:
    driver.switch_to.new_window('tab')
    driver.get(a_tag_list[0])
    

# shut down the browser
# driver.quit()
