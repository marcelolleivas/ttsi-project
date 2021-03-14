from selenium import webdriver
from ipdb import spost_mortem

from e2e_tests.helpers.utils import clean_data

from e2e_tests.modules.login_page import LoginPage


def before_all(context):
    context.browser = webdriver.Chrome(executable_path='e2e_tests/driver/chromedriver')


def before_scenario(context, scenario):
    context.browser = webdriver.Chrome(executable_path='e2e_tests/driver/chromedriver')
    context.page = LoginPage(context.browser)
    context.page.open("http://165.227.93.41/lojinha-web")


def after_scenario(context, scenario):
    clean_data()
    context.browser.close()


def after_step(context, step):
    if context.config.userdata.getbool("debug") and step.status == 'failed':
        spost_mortem(step.exc_traceback)
