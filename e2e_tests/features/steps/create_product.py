from behave import given, then, when, step

from e2e_tests.pages.login_page import LoginPage
from e2e_tests.pages.product_list_page import ProductListPage
from e2e_tests.pages.add_product_page import AddProductPage


@when(u'que eu esteja na página "{page}"')
def go_to_page(context, page):
    """"
    First logging in
    """
    login_page = LoginPage(context.browser)
    login_page.open("http://165.227.93.41/lojinha-web")
    login_page.user_input().send_keys("marceloleivass")
    login_page.password_input().send_keys("marcelo123")
    login_page.entrar_bttn().click()
    """
    Then, on list page, accessing Add Product Page
    """
    page = ProductListPage(context.browser)
    page.add_product_bttn().click()


@step(u'insiro valor em "{input_field}"')
def input_on_field(context, input_action):
    add_product_page = AddProductPage(context.browser)
    if input_action == "nome do produto":
        add_product_page.product_name_input().send_keys("Macbook Pro")
    elif input_action == "valor do produto":
        add_product_page.product_value_input().send_keys("4000")
    elif input_action == "cores do produto":
        add_product_page.product_colors_input().send_keys("Branco, preto")


@step(u'clico no botão "{bttn_name}"')
def clicking_save_bttn(context, bttn_name):
    add_product_page = AddProductPage(context.browser)
    if bttn_name == "salvar":
        add_product_page.save_bttn().click()
