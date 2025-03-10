from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep


class TutorialBrowser:
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

    def highlight_element(self, element, highlight_amount=3):
        """Blinks a red border around a Selenium WebElement."""
        original_style = self._driver.execute_script("return arguments[0].getAttribute('style')", element)
        for _ in range(highlight_amount):
            self._driver.execute_script("arguments[0].style.border='3px solid red'", element)
            sleep(.4)
            self._driver.execute_script("arguments[0].style.border='none'", element)
            sleep(.3)
        self._driver.execute_script("arguments[0].setAttribute('style', arguments[1])", element, original_style or "")

    def __del__(self):
        self._driver.quit()

    def input_to_element(self, filter, filter_str, input_str, delay=0.15, highlight_before=0):
        el = self.get_element(filter, filter_str)
        if highlight_before:
            self.highlight_element(el, highlight_before)
        for char in input_str:
            el.send_keys(char)
            sleep(delay)
