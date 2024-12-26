from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time
import pandas as pd


class Link:
    data = {}

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def land_first_page(self, u):
        self.driver.get(url=u)
        self.driver.implicitly_wait(5)

    def get_links(self, cate):
        links = self.driver.find_elements(By.XPATH, '//div/section/h2/a')
        for l in links:
            print(l.get_attribute('href'))
            self.data['Link'] = l.get_attribute('href')
            p = pd.DataFrame([self.data])
            p.to_csv(f"path to save/{cate.lower()}.csv", mode='a', header=not os.path.exists(f"path to save/{cate.lower()}.csv"), index=False)

f_name = str(input("Enter City: "))
url = str(input("Enter Page Url: "))
bot = Link()
bot.land_first_page(url)
bot.get_links(f_name)
