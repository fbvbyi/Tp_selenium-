

from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Country():

    def __init__(self,driver : WebDriver):
        self.driver = driver
        self.postcode_ = '//input[@name="postcode"]'


    def clickCountry(self):
        c_country= driver.find_element(By.NAME, 'country_id')
        sleep(1)





//label[@for="input-payment-country"]