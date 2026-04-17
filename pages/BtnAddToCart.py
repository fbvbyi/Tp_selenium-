from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BtnAddToCart():

    def __init__(self,driver : WebDriver):
        self.driver = driver
        self.btn_Availability ='(//button[@title= "Add to Cart"])[2]'

    def clickOn_BtnAdd(self):
        c_btn_Availability = self.driver.find_element(By.XPATH, self.btn_Availability)
        c_btn_Availability.click()
