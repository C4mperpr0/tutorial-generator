from tutorialbrowser import TutorialBrowser 
from gotty import Gotty
from selenium.webdriver.common.by import By
from time import sleep
import json


# don't forget to create credentials.json with your username and password
with open('credentials.json') as file:
    credentials = json.loads(file.read())

with TutorialBrowser() as w:

    '''
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

    # click login button
    el = w.get_element(By.CLASS_NAME, 'btn-confirm')
    w.highlight_element(el, 2)
    el.click()
    sleep(2)

    # click on new project
    el = w.get_element(By.PARTIAL_LINK_TEXT, 'New Project')
    w.highlight_element(el, 3)
    el.click()
    sleep(2)

    w.get("https://git.th-wildau.de/projects/new")
    sleep(2)

    # select blank project
    el = w.get_element(By.CSS_SELECTOR, '.new-namespace-panel-wrapper:nth-of-type(1)')
    w.highlight_element(el, 3)
    el.click()
    # w.get("https://git.th-wildau.de/projects/new/#blank_project")
    sleep(2)

    # select group
    el = w.get_element(By.CLASS_NAME, 'js-group-namespace-dropdown')
    w.highlight_element(el, 2)
    el.click()
    sleep(1)
    w.input_to_element(By.CLASS_NAME, 'gl-listbox-search-input', credentials['username'], highlight_before=1)
    el = w.get_element(By.CLASS_NAME, 'gl-new-dropdown-item-text-wrapper')
    w.highlight_element(el, 2)
    el.click()
    sleep(1)

    # input project name
    el = w.get_element(By.ID, 'project_name')
    w.input_to_element(By.ID, 'project_name', 'my-telematics-project', highlight_before=2)

    # create project
    el = w.get_element(By.CLASS_NAME, 'js-create-project-button')
    w.highlight_element(el, 3)
    el.click()
    sleep(2)
    '''

    sleep(3)

    with Gotty(w) as g:
        print("started")
        sleep(3)

        # go to work directory
        g.run("cd git")
        sleep(1)

        # clone repository
        g.run("git clone git@git.th-wildau.de:t23-p2-softwareprojekt-pokedex/my-telematics-project.git")
        sleep(3)
        g.run("cd my-telematics-project")

        # create file 
        g.run("echo \"Hello World!\" > my-file.txt")
        sleep(1)

        # see status
        g.run("git status")
        sleep(2)

        # add and stage file
        g.run("git add my-file.txt")
        sleep(2)

        # commit
        g.run("git commit -m \"my-file added and improved!\"")
        sleep(2)

        # push
        g.run("git push")
        sleep(5)

