from behave import when, then

from e2e_tests.modules.login_page import LoginPage
from e2e_tests.modules.product_list_page import ProductListPage


@when('insiro usuário "{user_login}"')
def input_valid_user(context, user_login):
    context.page = LoginPage(context.browser)
    context.page.user_input().send_keys(user_login)


@when('insiro a senha "{user_password}"')
def input_password(context, user_password):
    context.page.password_input().send_keys(user_password)


@when("clico em entrar")
def clicking_enter_bttn(context):
    context.page.entrar_bttn().click()


@then('devo estar na rota "{test_type}"')
def assert_is_logged_in(context, test_type):
    if test_type == "positivo":
        product_list_page = ProductListPage(context.browser)
        product_list_page.header_title()
    elif test_type == "negativo":
        assert "Falha ao fazer login" in context.page.toastr.text()

