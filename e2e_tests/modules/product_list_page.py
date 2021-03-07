from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .po.page_objects import Page


class ProductListPage(Page):

    def header_title(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, 'logo-container'))
        )

    def page_title(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, 'Lista de Produtos'))
        )

    def add_product_bttn(self):
        return self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Adicionar produto')]"))
        )

    def name_product(self, name):
        return self.wait.until(
            EC.presence_of_element_located((By.XPATH, f"//a[contains(text(),'{name}')]"))
        )

    def price_product(self):
        return self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'p'))
        )
