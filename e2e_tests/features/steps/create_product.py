from behave import given, then, when, step

from e2e_tests.modules.login_page import LoginPage
from e2e_tests.modules.product_list_page import ProductListPage
from e2e_tests.modules.add_product_page import AddProductPage


@given('que esteja na página de adicionar produto')
def go_to_page(context):
    context.page = LoginPage(context.browser)
    context.page.user_input().send_keys("marceloleivass")
    context.page.password_input().send_keys("marcelo123")
    context.page.entrar_bttn().click()

    context.page = ProductListPage(context.browser)
    context.page.add_product_bttn().click()


@step('insere nome "{name}"')
def insert_on_name_field(context, name):
    context.page = AddProductPage(context.browser)
    context.page.product_name_input().send_keys(name)
    context.product_name = name


@step('insere valor "{price}"')
def insert_on_value_field(context, price):
    context.page = AddProductPage(context.browser)
    context.page.product_value_input().send_keys(price)
    context.product_value = price


@step('insere cor "{color}"')
def insert_on_color_field(context, color):
    context.page = AddProductPage(context.browser)
    context.page.product_colors_input().send_keys(color)


@step('clica em "{bttn_name}"')
def clicking_save_bttn(context, bttn_name):
    context.page = AddProductPage(context.browser)
    if bttn_name == "salvar":
        context.page.save_bttn().click()


@then('deve haver mensagem "{message}" na interface')
def assert_message_is_returned(context, message):
    context.page = AddProductPage(context.browser)
    toastr_text = context.page.toastr_output().text
    assert message in toastr_text


@step('lista de produtos "{contains_or_not}" produto')
def assert_product_is_listed(context, contains_or_not):
    context.page = AddProductPage(context.browser)
    context.page.product_list_bttn().click()

    if contains_or_not == "contem":
        print(context.product_value)
        context.page = ProductListPage(context.browser)
        assert context.page.name_product(context.product_name)
        assert context.product_value in context.page.price_product().text, f"element text is {context.page.price_product().text}"
