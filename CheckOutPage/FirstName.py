from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class FirstName():

    def __init__(self,driver : WebDriver):
        self.driver = driver
        self.First_Name ='//input[@name="firstname"]'

    def clickFirstName(self):
        c_FirstNameb= self.driver.find_element(By.XPATH, self.First_Name)
        c_FirstNameb.send_keys("John")
        sleep(1)