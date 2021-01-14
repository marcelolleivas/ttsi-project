from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .po.page_objects import Page


class AddProductPage(Page):
    # Texts
    def title_name(self):
        return self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Adicionar produto'))
        )

    def subtitle_text(self):
        return self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Não esqueça de preencher'))
        )

    # Product Inputs
    def product_name_input(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, 'produtonome'))
        )

    def product_value_input(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, 'produtovalor'))
        )

    def product_name_input(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, 'produtonome'))
        )

    def product_colors_input(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, 'produtocores'))
        )

    # Buttons
    def save_bttn(self):
        return self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, 'SALVAR'))
        )

    def product_list_bttn(self):
        return self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT,
                                            'LISTA DE PRODUTOS'))
        )
