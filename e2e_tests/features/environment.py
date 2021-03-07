from selenium import webdriver
from ipdb import spost_mortem

from e2e_tests.helpers.utils import clean_data

from e2e_tests.modules.login_page import LoginPage


def before_all(context):
    context.browser = webdriver.Chrome(executable_path='/Users/marceloleivas/Desktop/ml_projects/python/ttsi-project/'
                                                       'e2e_tests/helpers/driver/chromedriver')


def before_scenario(context, scenario):
    context.page = LoginPage(context.browser)
    context.page.open("http://165.227.93.41/lojinha-web")


def after_scenario(context, scenario):
    clean_data()
    context.browser.quit()


def after_step(context, step):
    if context.config.userdata.getbool("debug") and step.status == 'failed':
        spost_mortem(step.exc_traceback)
