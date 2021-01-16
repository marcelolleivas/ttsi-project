from behave import given, then, when

from e2e_tests.pages.login_page import LoginPage
from e2e_tests.pages.product_list_page import ProductListPage


@given("que esteja na página de login da lojinha")
def login_page(context):
    login_page = LoginPage(context.browser)
    login_page.open('http://165.227.93.41/lojinha-web/')


@when("insiro usuário válido")
def input_valid_user(context):
    login_page = LoginPage(context.browser)
    login_page.user_input().send_keys('marceloleivass')


@when("insiro a senha")
def input_password(context):
    login_page = LoginPage(context.browser)
    login_page.password_input().send_keys('marcelo123')


@when("clico em entrar")
def clicking_enter_bttn(context):
    login_page = LoginPage(context.browser)
    login_page.entrar_bttn().click()


@then("devo estar na página de lista de produtos")
def should_be_on_product_list_page(context):
    product_list_page = ProductListPage(context.browser)
    """
    Just checking if header exists
    """
    product_list_page.header_title()
