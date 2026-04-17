from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckOut():

    def __init__(self,driver : WebDriver):
        self.driver = driver
        self.CheckOut_Availability ='//*[contains(text(),"Checkout")]'

    def clickOn_CheckOut(self):
        c_CheckOut= self.driver.find_element(By.XPATH, self.CheckOut_Availability)
        c_CheckOut.click()
        sleep(2)