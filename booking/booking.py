import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from lib2to3.pgen2 import driver
from selenium import webdriver
import os
from booking.booking_filter import BookingFiltration
from booking.booking_report import BookingReport
from prettytable import PrettyTable


class Booking(webdriver.Chrome):
    def __init__(self,driver_path=r"F:\Bot",teardown=False):
        self.driver_path=driver_path
        self.teardown=teardown
        os.environ['PATH']+=self.driver_path
        options =webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches",['enable-logging'])
        super(Booking,self).__init__(options = options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self,currency=None):

        cur_ele=self.find_element(By.CSS_SELECTOR,'button[data-tooltip-text="Choose your currency"]')
        cur_ele.click()
        sel_cur_ele=self.find_element(By.CSS_SELECTOR,
        f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')

        sel_cur_ele.click()
    def select_place_to_go(self,place):
        search_field=self.find_element(By.ID,'ss')
        search_field.clear()
        search_field.send_keys(place)
        find_res=self.find_element(By.CSS_SELECTOR,'li[data-i="0"]')
        find_res.click()

    def select_dates(self,check_in,check_out):
        check_in_ele=self.find_element(By.CSS_SELECTOR,
                                       f'td[data-date="{check_in}"]')
        check_in_ele.click()
        check_out_ele = self.find_element(By.CSS_SELECTOR,
                                         f'td[data-date="{check_out}"]')
        check_out_ele.click()
    def select_adults(self,count=1):
        sel_ele=self.find_element(By.ID,'xp__guests__toggle')
        sel_ele.click()
        while True:
            dec_adults_ele=self.find_element(By.CSS_SELECTOR,
            'button[aria-label="Decrease number of Adults"]')
            dec_adults_ele.click()
            adults_value_ele=self.find_element(By.ID,'group_adults')
            adults_value=adults_value_ele.get_attribute('value') #Should give back adults count

            if int(adults_value) == 1:
                break

        inc_button_ele=self.find_element(By.CSS_SELECTOR,'button[aria-label="Increase number of Adults"]')
        for _ in range(count-1):
            inc_button_ele.click()

    def click_searh(self):
        search_ele=self.find_element(By.CSS_SELECTOR,'button[type="submit"]')
        search_ele.click()

    def apply_filter(self):
       filteration= BookingFiltration(driver=self)

       filteration.sort_price_asc()
       filteration.apply_star(4, 5)

    def report(self):

        hotel_box=self.find_element(By.ID,'ajaxsrwrap')

        report=BookingReport(hotel_box)
        table = PrettyTable(
           field_names = ["Hotel Name","Hotel Price","Hotel Ratings"]
        )
        table.add_rows(report.pull_titles())
        print(table)

