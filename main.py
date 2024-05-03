from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time

# URL to scrape
url = 'https://wenewz.com/#/front'

# Create a new Firefox profile
profile = webdriver.FirefoxProfile()

# Set the preference to Norwegian Bokmål
profile.set_preference("intl.accept_languages", "nb")

# Create a new instance of FirefoxOptions
options = Options()

# Set the profile in options
options.profile = profile

# Create a new instance of the Firefox driver with the options
driver = webdriver.Firefox(options=options)

# Go to the URL
driver.get(url)

# Wait until at least one link with the specific class name is present
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR,
         "a.noBorder.v-card.v-card--flat.v-card--link.v-sheet.v-sheet--outlined.theme--light.rounded-0"))
)

# Set the display style of the header element to none
driver.execute_script(
    "document.querySelector('header').style.display = 'none';")

driver.execute_script(
    "document.querySelectorAll('.v-btn__content').forEach(function(el) { el.style.display = 'none'; });")

# Record the start time
start_time = time.time()

# Set a time limit in minutes
minutes = 60

# Convert the time limit to seconds
time_limit = minutes * 60

# Initialize a counter for clicked links
clicked_links = 0

# Continue scrolling and clicking links until the time limit is reached
while time.time() - start_time < time_limit:
    # Scroll down the page
    for _ in range(5):  # Adjust this value based on your needs
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Allow time for the page to load

    # Find all links with the same CSS selector
    links = driver.find_elements(
        By.CSS_SELECTOR, "a.noBorder.v-card.v-card--flat.v-card--link.v-sheet.v-sheet--outlined.theme--light.rounded-0")

    # Iterate over each link
    for link in links:
        # Check if the time limit has been reached
        if time.time() - start_time > time_limit:
            print("Time limit reached")
            break

        # Get the href attribute of the link
        href = link.get_attribute('href')

        # Click the link
        link.click()

        # Increment the counter
        clicked_links += 1

        # Print the href attribute of the link and the number of clicked links
        print(f'Clicked link: {href} (Link {clicked_links})')

        # Wait until the close button is clickable
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable(
        #         (By.CSS_SELECTOR, "a[title='Lukk vindu']"))
        # )

        # Use JavaScript to set the display property to none
        driver.execute_script(
            "document.querySelector('.v-overlay__scrim').style.display = 'none';")
        driver.execute_script(
            "document.querySelector('.v-overlay.v-overlay--active.theme--dark').style.display = 'none';")
        driver.execute_script(
            "document.querySelector('.v-btn.v-btn--router.v-btn--text.theme--light.v-size--default').style.display = 'none';")
        driver.execute_script(
            "document.querySelectorAll('.v-btn__content').forEach(function(el) { el.style.display = 'none'; });")
        # Set the display style of the elements with the specific class to none
        driver.execute_script(
            "document.querySelectorAll('.title.v-btn.v-btn--block.v-btn--is-elevated.v-btn--has-bg.v-btn--router.theme--light.v-size--default').forEach(function(el) { el.style.display = 'none'; });")
        driver.execute_script(
            "document.querySelector('.pa-3.mb-2.v-card.v-sheet.theme--light.red.darken-4').style.display = 'none';")

        # Add a delay to allow any animations or overlays to finish
        time.sleep(4)

        # Find the close button and click it
        close_button = WebDriverWait(
            driver, 10).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "a[title='Lukk vindu']")))

        # Click the close button
        close_button.click()

        # Find all links again after clicking the current link
        links = driver.find_elements(
            By.CSS_SELECTOR,
            "a.noBorder.v-card.v-card--flat.v-card--link.v-sheet.v-sheet--outlined.theme--light.rounded-0")

# Print the total number of clicked links
print(f'Total clicked links: {clicked_links}')

# Close the browser
driver.quit()
