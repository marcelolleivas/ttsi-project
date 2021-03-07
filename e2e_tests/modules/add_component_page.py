from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .po.page_objects import Page


class AddComponentPage(Page):

    def page_title(self):
        return self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Adicionar Componente ao Produto'))
        )

    def component_name_input(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, 'componentenomeadicionar'))
        )

    def component_quantity_input(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, 'componentequantidadeadicionar'))
        )

    def save_bttn(self):
        return self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, 'SALVAR COMPONENTE'))
        )

    def cancel_bttn(self):
        return self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, 'CANCELAR'))
        )