from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Nom():

    def __init__(self,driver : WebDriver):
        self.driver = driver
        self.Nom_ ='//input[@name="lastname"]'

    def clickNom(self):
        c_Name= self.driver.find_element(By.XPATH, self.Nom_)
        c_Name.send_keys("Magalie")
        sleep(1)