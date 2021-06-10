from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from config import configuration


class HyperOptic():
    def __init__(self):
        self.BASE_URL = "https://www.hyperoptic.com/"
        self.driver = webdriver.Chrome(executable_path=configuration.CHROME_DRIVER_URL)

    def get_broadband_only_deals(self):
        self.driver.get(url=self.BASE_URL)
        counter = 1

        # Accept the Cookies #
        wait = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "modal-button")))

        cookie_button = self.driver.find_element_by_class_name("modal-button")

        if cookie_button is not None:
            cookie_button.click()

        wait = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Broadband")))
        broadband_link = self.driver.find_element_by_link_text("Broadband")
        broadband_link.click()

        wait = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[6]/div/div[4]/div")))

        packages = self.driver.find_elements_by_class_name("package")  # Getting list of elements which named package class

        for package in packages:

            promotion = package.find_element_by_xpath("//div[4]/div/div/div[" + str(counter) + "]/div[1]/span").text
            if promotion == "":
                promotion = "No promotion for this package."

            contract_length = package.find_element_by_xpath("//div[4]/div/div/div[" + str(counter) + "]/div[3]/div[2]/span").text
            try:
                old_price = package.find_element_by_xpath("//div[4]/div/div/div[" + str(+counter) + "]/div[3]/div[1]/span[1]").text
                current_price = package.find_element_by_xpath("//div[4]/div/div/div[" + str(+counter) + "]/div[3]/div[1]/span[2]").text
                price = current_price + " reduced from " + old_price
            except NoSuchElementException:
                current_price = package.find_element_by_xpath("//div[4]/div/div/div[" + str(+counter) + "]/div[3]/div[1]/span[1]").text
                price = current_price

            size_unit = package.find_element_by_class_name("size").text + " " + package.find_element_by_class_name("unit").text

            print(" PRICE : " + price + " SPEED : " + size_unit + " CONTRACT INFO :" + contract_length + " Promotion : " + promotion)
            counter = counter + 1
