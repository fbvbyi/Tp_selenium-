from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Adress():

    def __init__(self,driver : WebDriver):
        self.driver = driver
        self.Adress_ ='//input[@name="address_1"]'

    def clickAdress(self):
        c_Adress= self.driver.find_element(By.XPATH, self.Adress_)
        c_Adress.send_keys("Rue des plantes")
        sleep(1)