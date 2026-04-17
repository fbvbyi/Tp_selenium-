from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class EMail():

    def __init__(self,driver : WebDriver):
        self.driver = driver
        self.Email_ ='//input[@name="email"]'

    def clickEmail(self):
        c_Email= self.driver.find_element(By.XPATH, self.Email_)
        c_Email.send_keys("kaka@yahoo.fr")
        sleep(1)