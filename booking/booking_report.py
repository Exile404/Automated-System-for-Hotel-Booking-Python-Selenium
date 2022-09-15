


from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.by import By

class BookingReport:
    def __init__(self,box_sec_ele:WebElement):
        self.box_sec_ele=box_sec_ele
        self.deal_boxes=self.pull_deal_box()

    def pull_deal_box(self):
        return self.box_sec_ele.find_elements(
            By.CSS_SELECTOR,'.a826ba81c4.fe821aea6c.fa2f36ad22.afd256fc79.d08f526e0d.ed11e24d01.ef9845d4b3.da89aeb942')

    def pull_titles(self):
        collections = []
        i=2
        for deal_box in self.deal_boxes:

            #Hotel name
            hotel_name=deal_box.find_element(By.CSS_SELECTOR,
                                  '.fcab3ed991.a23c043802').get_attribute('innerHTML').strip()
            #print(hotel_name)
            hotel_price = deal_box.find_element(By.CSS_SELECTOR,
                                                '.fcab3ed991.bd73d13072').get_attribute('innerHTML').strip()
            s=f'div[{str(i)}]'
            hotel_score = deal_box.find_element(By.CSS_SELECTOR,'.b5cd09854e.d10a6220b4').get_attribute('innerHTML').strip()

            collections.append([hotel_name,hotel_price,hotel_score])
            i+=2
        return collections

