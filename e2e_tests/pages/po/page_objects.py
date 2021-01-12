from abc import ABC
from selenium.webdriver.support.ui import WebDriverWait


class Page(ABC):
    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.wait = WebDriverWait(webdriver, 15)

    def open(self, url=''):
        self.webdriver.get(url)
