from tutorialbrowser import TutorialBrowser 
from gotty import Gotty
from selenium.webdriver.common.by import By
from time import sleep
import json


# don't forget to create credentials.json with your username and password
with open('credentials.json') as file:
    credentials = json.loads(file.read())

with TutorialBrowser() as w:

    """
    # open page
    w.get("https://bellgardt.dev")
    sleep(5)

    # show input field and input search term
    w.input_to_element(By.TAG_NAME, 'input', "THW Git", highlight_before=3)
    sleep(1)

    # show search result
    el = w.get_element(By.CLASS_NAME, 'card-content')
    w.highlight_element(el)
    el.click()
    sleep(1)

    # input username and password
    w.input_to_element(By.ID, 'ldapmain_username', credentials['username'], highlight_before=1)
    w.input_to_element(By.ID, 'ldapmain_password', credentials['password'], highlight_before=1)

    # click submit button
    el = w.get_element(By.CLASS_NAME, 'btn-confirm')
    w.highlight_element(el, 2)
    el.click()
    sleep(3)

    """

    with Gotty(w) as g:
        print("started")
        sleep(3)

        print("start")
        g.run("speedtest-cli")
        print("end")

        sleep(30)



    sleep(50)

