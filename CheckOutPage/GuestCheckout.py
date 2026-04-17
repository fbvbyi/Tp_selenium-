from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class GuestCheckOut():

    def __init__(self,driver : WebDriver):
        self.driver = driver
        self.GuestCheckOut_Availability ='//label[@for="input-account-guest"]'

    def clickOn_GuestCheckOut(self):
        c_GuestCheckOut= self.driver.find_element(By.XPATH, self.GuestCheckOut_Availability)
        c_GuestCheckOut.click()
        sleep(2)