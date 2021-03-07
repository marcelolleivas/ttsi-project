from requests import delete

from api_tests_exercises.helpers.constants import (
    VALID_USER_PAYLOAD,
    INVALID_USER_PAYLOAD,
    VALID_PRODUCT_PAYLOAD,
    VALID_TOKEN
)


def login_payload_builder(user_status: str):
    """Build a payload used on login service.

    Args:
        user_status(str): The user status could be valid or invalid.

    Returns:
        payload(dict): A dict, structured as an expected payload to
        login service.
    """
    payloads = {
        "valido": VALID_USER_PAYLOAD,
        "invalido": INVALID_USER_PAYLOAD
    }
    payload = payloads.get(user_status.lower())
    return payload


def more_than_one_colour():
    VALID_PRODUCT_PAYLOAD['produtocores'].append('preto')


def more_than_one_component():
    VALID_PRODUCT_PAYLOAD['componentes'].append(
        {
            "componentenome": "fone de ouvido",
            "componentequantidade": 1
        }
    )


def no_colour():
    VALID_PRODUCT_PAYLOAD.pop('produtocores')


def no_components():
    VALID_PRODUCT_PAYLOAD.pop('componentes')


def no_value():
    VALID_PRODUCT_PAYLOAD.pop('produtovalor')


def products_payload_builder(product_type: str):
    """Build a payload used on login service.
    Args:
        product_type(str): The product type could have the following states:
        simple; more than one colour; more than one component; without colour;
        without component; and without value.

    Returns:
        payload(dict): A dict, structured as an expected payload to
        product service.
    """

    handling = {
        "mais de uma cor": more_than_one_colour,
        "mais de um componente": more_than_one_component,
        "sem cor": no_colour,
        "sem componentes": no_components,
        "sem valor": no_value
    }
    if product_type != "simples":
        handling.get(product_type.lower())()
    return VALID_PRODUCT_PAYLOAD


def clean_store_data():
    """It's used to clean data that was made by the tests"""

    url = "http://165.227.93.41/lojinha/dados"
    response = delete(
        url,
        headers=VALID_TOKEN
    )
    return response
