import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WELLFOUND_EMAIL = "hatwar.saket23@gmail.com"
WELLFOUND_PASSWORD = ""
THREAD_URL = "https://wellfound.com/jobs/messages/966551005"
MESSAGE = "Hello, this is an automated message!"

# Function to simulate random wait times
def random_sleep(min_seconds=1, max_seconds=3):
    time.sleep(random.uniform(min_seconds, max_seconds))

# Initialize the WebDriver with custom user agent
options = Options()

# Set a custom User-Agent (you can change this to any user agent string)
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
options.add_argument(f"user-agent={user_agent}")

service = Service("/usr/local/bin/chromedriver-linux64/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

random_sleep(5, 7)  

# Navigate to the thread
driver.get(THREAD_URL)
random_sleep(3, 5)  

# Locate the message box and send the message
message_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "textarea#response"))
)
random_sleep(1, 3)  
message_box.send_keys(MESSAGE)
message_box.send_keys(Keys.RETURN)

random_sleep(2, 4) 
print("Message sent successfully!")
driver.quit()
