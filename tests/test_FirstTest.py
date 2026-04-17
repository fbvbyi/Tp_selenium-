import sys
import os

import pytest

from CheckOutPage import EMail


sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from helpers.BaseTest import BaseTest
from pages.HomePage import HomePage
from pageFragments.HeaderPageFragment import  HeaderPageFragment
from pages.ProductListPage import ProductListPage
from pages.BtnAddToCart import BtnAddToCart
from pages.ViewCart import ViewCart
from pages.CheckOut import CheckOut
from CheckOutPage.GuestCheckout import GuestCheckOut
from CheckOutPage.FirstName import FirstName
from CheckOutPage.Nom import Nom
from CheckOutPage.EMail import EMail
from CheckOutPage.TelePhone import TelePhone
from CheckOutPage.Adress1 import Adress
from CheckOutPage.City import City
from CheckOutPage.PostCode import PostCode

class Test_FirstTest(BaseTest): # héritage

    @pytest.mark.test_MyFirstTest
    def test_MyFirstTest(self):
        self.open_application()
        
        home = HomePage(self.driver)
        home.is_page_visible("Your Store")

        header = HeaderPageFragment(self.driver)
        header.select_Menu()
        header.select_SubMenu()

        ProducList = ProductListPage(self.driver)
        ProducList.clickOn_Filter_InStock()
        ProducList.select_img_ProductItem()

        btn = BtnAddToCart(self.driver)
        btn.clickOn_BtnAdd()

        viewbtn = ViewCart(self.driver)
        viewbtn.clickOn_View()

        CheckOutbtn = CheckOut(self.driver)
        CheckOutbtn.clickOn_CheckOut()

        GuestCheckOutB = GuestCheckOut(self.driver)
        GuestCheckOutB.clickOn_GuestCheckOut()

        Firstname = FirstName(self.driver)
        Firstname.clickFirstName()

        name = Nom(self.driver)
        name.clickNom()

        mail = EMail(self.driver)
        mail.clickEmail()

        Phone = TelePhone(self.driver)
        Phone.clickPhone()

        adress = Adress(self.driver)
        adress.clickAdress()

        city = City(self.driver)
        city.clickCity()

        postcode = PostCode(self.driver)
        postcode.clickPostcode()









