from selenium import webdriver
from ipdb import spost_mortem


def before_all(context):
    context.browser = webdriver.Chrome(executable_path='/Users/marceloleivas/Desktop/ml_projects/python/ttsi-project/'
                                                       'e2e_tests/helpers/driver/chromedriver')


def after_all(context):
    context.browser.quit()


def after_step(context, step):
    if context.config.userdata.getbool("debug") and step.status == 'failed':
        spost_mortem(step.exc_traceback)
