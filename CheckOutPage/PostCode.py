
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PostCode():

    def __init__(self,driver : WebDriver):
        self.driver = driver
        self.postcode_ ='//input[@name="postcode"]'

    def clickPostcode(self):
        c_postcode= self.driver.find_element(By.XPATH, self.postcode_)
        c_postcode.send_keys("35000")
        sleep(1)


