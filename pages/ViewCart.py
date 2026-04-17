from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ViewCart():

    def __init__(self,driver : WebDriver):
        self.driver = driver
        self.ViewCart_Availability ='//*[contains(text(),"View Cart")]'

    def clickOn_View(self):
        c_ViewCart_Availability = self.driver.find_element(By.XPATH, self.ViewCart_Availability)
        c_ViewCart_Availability.click()
        sleep(2)
