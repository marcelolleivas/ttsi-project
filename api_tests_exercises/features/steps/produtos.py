import json

from behave import given, then, step
from requests import post

from api_tests_exercises.helpers.constants import VALID_TOKEN
from api_tests_exercises.modules.auxiliar import (
    products_payload_builder
)


@given('que queira incluir um produto "{product_type}"')
def setup_products_payload(context, product_type):
    context.products_payload = products_payload_builder(product_type)
    context.product_type = product_type
    print(f"payload: {context.products_payload}")


@then('status de produto deve ser "{response_code}"')
def assert_products_service(context, response_code):
    url = f"{context.lojinha_service_url}/produto"

    response = post(
        url,
        headers=VALID_TOKEN,
        json=context.products_payload
    )

    expected_value = int(response_code)

    assertion_message = (
        f"Expected status code was {expected_value}",
        f"Received status code is {response.status_code}"
    )

    assert response.status_code == expected_value, assertion_message
    context.response_data = json.loads(response.text)


@step('resposta de produto deve ser de "{response_message}"')
def assert_response_message(context, response_message):
    SUCCEED_MESSAGE = "Produto adicionado com sucesso"
    if response_message == "sucesso":
        assertion_message = (
            f"Expected message was {SUCCEED_MESSAGE}\n"
            f"Received message is {context.response_data['message']}"
            f"Expected error was null"
            f"Received error is {context.response_data['error']}"
        )
        assert context.response_data["message"] == SUCCEED_MESSAGE and context.response_data["error"] == "", \
            assertion_message
