from os import system
from threading import Thread 
from selenium.webdriver.common.by import By

class Gotty:
    def __init__(self, webbrowser, port=8080, terminal="bash"):
        self._webbrowser = webbrowser
        self._port = port
        self._terminal = terminal 
        self._terminal_thread = None

    def __enter__(self):
        # process already running
        if self._terminal_thread:
            return

        cmd = f"gotty -p {self._port} -w {self._terminal}" # Could also be using --once flag instead of context management
        self._terminal_thread = Thread(target=system, args=(cmd,)).start()
        self._webbrowser.get(f"http://localhost:{self._port}")
        return self

    def __exit__(self, *exc):
        if self._terminal_thread:
            try:
                self._terminal_thread.join(0)
            except:
                pass # TODO: do actual error handling
        self._terminal_thread = None
        return False 

    def run(self, cmd):
        self._webbrowser.input_to_element(By.CLASS_NAME, "xterm-helper-textarea", cmd + "\n", delay=0.05)
        print("Run cmd done!")


        

