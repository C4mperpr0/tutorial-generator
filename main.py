from webbrowser import WebBrowser 
from selenium.webdriver.common.by import By
from time import sleep

with WebBrowser() as w:
    # open page
    w.get("https://bellgardt.dev")
    sleep(1)

    # show input field
    el = w.get_element(By.TAG_NAME, 'input')
    w.highlight_element(el)
    el.click()
    sleep(1)

    # input search term
    for char in 'THW Git':
        el.send_keys(char)
        sleep(.2)
    sleep(1)

    # show search result
    el = w.get_element(By.CLASS_NAME, 'card-content')
    w.highlight_element(el)
    el.click()
    sleep(1)

    sleep(50)

