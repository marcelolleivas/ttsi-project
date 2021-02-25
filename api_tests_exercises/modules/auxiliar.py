from api_tests_exercises.helpers.constants import (
    VALID_USER_PAYLOAD,
    INVALID_USER_PAYLOAD
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
