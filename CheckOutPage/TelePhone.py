from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class TelePhone():

    def __init__(self,driver : WebDriver):
        self.driver = driver
        self.Phone_ ='//input[@name="telephone"]'

    def clickPhone(self):
        c_Phone= self.driver.find_element(By.XPATH, self.Phone_)
        c_Phone.send_keys("0528156644")
        sleep(1)