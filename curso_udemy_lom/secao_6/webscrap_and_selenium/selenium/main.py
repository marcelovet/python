import time
from pathlib import Path

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# chromedriver
# https://chromedriver.chromium.org/downloads
# Selenium
# https://selenium-python.readthedocs.io/

ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC = ROOT_FOLDER / "drivers" / "chromedriver.exe"


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument("--headless")
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=str(CHROMEDRIVER_EXEC)
    )

    chrome_browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options,
    )

    return chrome_browser


if __name__ == "__main__":
    TIME_TO_WAIT = 10
    options = ('--disable-gpu', '--no-sandbox',)
    browser = make_chrome_browser(*options)

    # open chrome and get that page
    browser.get("https://www.google.com")

    # wait for find element
    element = "q"
    try:
        search_elem = WebDriverWait(browser, TIME_TO_WAIT).until(
            EC.presence_of_element_located(
                (By.NAME, element)
            )
        )
        search_elem.send_keys("Hello world!")
        search_elem.send_keys(Keys.ENTER)

        results = browser.find_element(By.ID, "search")
        links = results.find_elements(By.TAG_NAME, "a")
        links[0].click()
    except TimeoutException:
        print(f"element \"{element}\" not found")

    time.sleep(TIME_TO_WAIT)
