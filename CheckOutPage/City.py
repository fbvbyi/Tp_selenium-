from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class City():

    def __init__(self,driver : WebDriver):
        self.driver = driver
        self.city_ ='//input[@name="city"]'

    def clickCity(self):
        c_city= self.driver.find_element(By.XPATH, self.city_)
        c_city.send_keys("RENNES")
        sleep(1)