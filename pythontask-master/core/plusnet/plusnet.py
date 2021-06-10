from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from config import configuration


class PlusNet():
    def __init__(self):
        self.BASE_URL = "https://www.plus.net/"
        self.driver = webdriver.Chrome(executable_path=configuration.CHROME_DRIVER_URL)

    def get_broadband_only_deals(self):
        self.driver.get(url=self.BASE_URL)

        # cookie accept

        wait = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "cookie-consent-modal")))

        cookie_button = self.driver.find_element_by_id("cookie-button-save-default")

        if cookie_button is not None:
            cookie_button.click()

        menu = self.driver.find_element_by_id("plusnet-mobile-menu")

        link = menu.find_element_by_xpath("//ul/li[1]/a[2]")
        link.click()

        products = self.driver.find_elements_by_class_name("card-section")

        for product in products:
            product_title = product.find_element_by_tag_name("h3").text
            speed = product.find_element_by_class_name("speed-content").text
            contract_length = product.find_element_by_class_name("contract-length").text
            price = product.find_element_by_class_name("product-rental").text

            if product_title is "":
                return

            print("PRODUCt NAME : " + product_title + " SPEED: " + speed + "CONTRACT LENGTH : " + contract_length + " PRICE : " + price + "\n")