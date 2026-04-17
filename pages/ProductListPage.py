from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep

class ProductListPage():

    def __init__(self,driver : WebDriver):
        self.driver = driver
        self.lbl_Availability ='//label[@for="mz-fss-0--1"]'
        self.img_ProductItem = '(//*[@class= "carousel-item active"]/*[@class= "lazy-load"])[3]'

    def clickOn_Filter_InStock(self):
        c_lbl_Availability = self.driver.find_element(By.XPATH, self.lbl_Availability)
        c_lbl_Availability.click()
        sleep(3)


    def select_img_ProductItem (self):
        c_img_ProductItem = self.driver.find_element(By.XPATH, self.img_ProductItem)
        c_img_ProductItem.click()