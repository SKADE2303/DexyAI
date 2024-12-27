from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import json
import time


service = Service("/usr/local/bin/chromedriver-linux64/chromedriver")  
driver = webdriver.Chrome(service=service)

driver.get("https://wellfound.com/login")  
print("Please log in manually in the browser window.")
time.sleep(30) 


cookies = driver.get_cookies()

with open("cookies.json", "w") as file:
    json.dump(cookies, file)

print("Cookies have been saved to 'cookies.json'!")
driver.quit()
