import sys
from playwright.sync_api import sync_playwright
import random
import time

# Check if a message argument is provided
if len(sys.argv) != 2:
    print("Usage: python send_message.py <message>")
    sys.exit(1)

# Retrieve the message from the command-line arguments
MESSAGE = sys.argv[1]

# Wellfound login credentials and thread URL
WELLFOUND_EMAIL = "hatwar.saket23@gmail.com"
WELLFOUND_PASSWORD = "Hatwar@2303"
THREAD_URL = "https://wellfound.com/jobs/messages/966551005"

def human_delay(min_delay=1, max_delay=3):
    """Simulates human-like random delay"""
    time.sleep(random.uniform(min_delay, max_delay))

def send_message():
    with sync_playwright() as p:
        # Launch the browser with human-like settings
        browser = p.chromium.launch(headless=False)  # Use headless=True for headless operation
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 720},  # Set realistic screen size
            locale="en-US",  # Mimic English language settings
            timezone_id="America/New_York"  # Mimic timezone settings
        )

        # Disable `navigator.webdriver` for bot detection
        context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
        """)

        page = context.new_page()

        try:
            # Log in to Wellfound
            print("Navigating to the login page...")
            page.goto("https://wellfound.com/login")
            human_delay(2, 4)

            print("Filling in login credentials...")
            page.fill("input[name='user[email]']", WELLFOUND_EMAIL)
            human_delay(1, 2)
            page.fill("input[name='user[password]']", WELLFOUND_PASSWORD)
            human_delay(1, 2)

            # Simulate pressing the Enter key slowly
            page.locator("input[name='user[password]']").press("Enter")
            human_delay(5, 7)

            # Wait for login to complete
            print("Waiting for login to complete...")
            page.wait_for_url("https://wellfound.com/dashboard", timeout=15000)

            # Navigate to the thread
            print("Navigating to the thread URL...")
            page.goto(THREAD_URL)
            human_delay(3, 5)

            # Locate the message box and send the message
            print("Sending the message...")
            message_box = page.locator("textarea#response")  # Adjust the selector if necessary
            message_box.click()
            human_delay(1, 2)

            # Simulate typing the message with a delay between keystrokes
            for char in MESSAGE:
                message_box.type(char, delay=random.uniform(50, 200))  # Typing delay in milliseconds
            
            human_delay(2, 4)
            message_box.press("Enter")

            print("Message sent successfully!")

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            # Close the browser
            browser.close()

if __name__ == "__main__":
    send_message()
