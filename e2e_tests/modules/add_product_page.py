from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .po.page_objects import Page


class AddProductPage(Page):
    # Texts
    def title_name(self):
        return self.wait.until(
            EC.presence_of_element_located((By.XPATH, "h4[contains(.,'Adicionar produto')]"))
        )

    def subtitle_text(self):
        return self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.m4 > .row:nth-child(2)'))
        )

    # Product Fields
    def product_name_input(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, 'produtonome'))
        )

    def product_value_input(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, 'produtovalor'))
        )

    def product_colors_input(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, 'produtocores'))
        )

    # Buttons
    def save_bttn(self):
        return self.wait.until(
            EC.presence_of_element_located((By.XPATH,
                                            "//button[@name='action']"))
        )

    def product_list_bttn(self):
        return self.wait.until(
            EC.presence_of_element_located((By.XPATH,
                                            "//a[contains(text(),'Lista de Produtos')]"))
        )

    # Toastr
    def toastr_output(self):
        return self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.toast'))
        )
