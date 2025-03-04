from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


class WebBrowser:
    def __init__(self, driver=webdriver.Firefox):
        # Set up the WebDriver (make sure you have the correct driver installed)
        self._driver = driver()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            self._driver.quit()
        except:
            pass
        # Handle any exception if needed
        if exc_type is not None:
            print(f"Exception type: {exc_type}, Exception value: {exc_value}")
        return False  # Return True to suppress exceptions, False to propagate them 

    def get(self, url):
        self._driver.get(url)

    def get_element(self, filter, filter_str):
        return self._driver.find_element(filter, filter_str)

    def highlight_element(self, element):
        """Blinks a red border around a Selenium WebElement."""
        original_style = self._driver.execute_script("return arguments[0].getAttribute('style')", element)
        for _ in range(3):
            self._driver.execute_script("arguments[0].style.border='3px solid red'", element)
            time.sleep(.4)
            self._driver.execute_script("arguments[0].style.border='none'", element)
            time.sleep(.3)
        self._driver.execute_script("arguments[0].setAttribute('style', arguments[1])", element, original_style or "")

    def __del__(self):
        self._driver.quit()

