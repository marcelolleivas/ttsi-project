import json
from json import dumps

from behave import given, then, step
from requests import post

from api_tests_exercises.helpers.constants import DEFAULT_HEADERS
from api_tests_exercises.modules.auxiliar import (
    login_payload_builder
)


@given('que tente fazer login com usuário "{user_status}"')
def setup_login_payload(context, user_status):
    context.login_payload = login_payload_builder(user_status)
    context.user_status = user_status


@then('status da requisição deve ser "{login_status}"')
def assert_login_service(context, login_status):
    STATUS_CODES = {"aprovado": 200, "reprovado": 401}
    url = f"{context.lojinha_service_url}/login"
    response = post(
        url,
        headers=DEFAULT_HEADERS,
        data=dumps(context.login_payload)
    )

    expected_value = STATUS_CODES.get(login_status.lower())

    assertion_message = (
        f"Expected status code was {expected_value}\n"
        f"Received status code is {response.status_code}"
    )
    assert response.status_code == expected_value, assertion_message

    context.response_data = json.loads(response.text)


@step('resposta deve ser de "{response_status}"')
def assert_response_data(context, response_status):
    SUCCEED_MESSAGE = "Sucesso ao realizar o login"
    if response_status == "sucesso":
        assertion_message = (
            f"Expected message was {SUCCEED_MESSAGE}\n"
            f"Received message is {context.response_data['message']}"
            f"Expected error was null"
            f"Received error is {context.response_data['error']}"
        )
        assert context.response_data["data"]["token"] and context.response_data["message"] == SUCCEED_MESSAGE \
               and context.response_data["error"] == "", assertion_message
