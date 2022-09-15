

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BookingFiltration():
    def __init__(self,driver:WebDriver):
        self.driver=driver

    def apply_star(self,*star_values):
        sf_box=self.driver.find_element(By.CSS_SELECTOR,'div[data-filters-group="class"]')
        star_child= sf_box.find_elements(By.CSS_SELECTOR,'*')
        for star_value in star_values:
            for star_ele in star_child:
                if (star_ele.get_attribute('innerHTML')).strip()== f'{star_value} stars':
                    star_ele.click()

    def sort_price_asc(self):
        ele=self.driver.find_element(By.CSS_SELECTOR,'button[data-testid="sorters-dropdown-trigger"]')
        ele.click()
        price=self.driver.find_element(By.CSS_SELECTOR,'button[data-id="price"]')
        price.click()



