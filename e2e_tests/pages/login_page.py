from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .po.page_objects import Page


class LoginPage(Page):

    def header_title(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, "logo-container"))
        )

    def user_input(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, "usuario"))
        )

    def password_input(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, "senha"))
        )

    def entrar_bttn(self):
        return self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[@name='action']"))
        )
