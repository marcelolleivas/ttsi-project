from api_tests_exercises.modules.auxiliar import clean_store_data

from api_tests_exercises.helpers.constants import VALID_PRODUCT_PAYLOAD


def before_all(context):
    userdata = context.config.userdata
    context.lojinha_service_url = userdata.get("lojinha_url", "")


def after_scenario(context, scenario):
    if 'login' not in scenario.tags:
        clean_store_data()