from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from geopy.geocoders import ArcGIS
import pandas as pd
import time
import os

class CanadianDentistData:
    data_dict = {}
    options = Options()
    options.add_argument('--headless')

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def land_required_page(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(5)

    def get_name(self):
        try:
            name = self.driver.find_element(By.XPATH, '//header/h1').text
            self.driver.implicitly_wait(5)
            print("Name: "+name)
            self.data_dict['Name'] = name
        except:
            self.data_dict['Name'] = 'N/A'

    def get_full_name(self):
        try:
            full_name = self.driver.find_element(By.XPATH, '//header/dl/dd[1]').text
            self.driver.implicitly_wait(5)
            print("Full Name: "+full_name)
            self.data_dict['Full Name'] = full_name
        except:
            self.data_dict['Full Name'] = 'N/A'

    def get_Registration_number(self):
        try:
            r_num = self.driver.find_element(By.XPATH, '//header/dl/dd[2]').text
            self.driver.implicitly_wait(5)
            print("Registration Number: "+r_num)
            self.data_dict['Registration_Number'] = r_num
        except:
            self.data_dict['Registration Number'] = 'N/A'

    def current_Status(self):
        try:
            c_status = self.driver.find_element(By.XPATH, '//header/dl/dd[3]').text
            self.driver.implicitly_wait(5)
            print("Current Status: "+c_status)
            self.data_dict['Current Status'] = c_status
        except:
            self.data_dict['Current Status'] = 'N/A'

    def get_Type(self, type):
        self.data_dict['City'] = type

    def get_primary_practice_information(self):
        try:
            p_uni = self.driver.find_element(By.XPATH, '//div[@class="row"]/h4').text
            self.driver.implicitly_wait(15)
            print("Primary University: "+p_uni)
            self.data_dict['Primary University'] = p_uni
        except:
            self.data_dict['Primary University'] = 'N/A'

        try:
            p_add = self.driver.find_element(By.XPATH, '//div[@class="col-md-6"]/address').text.replace('\n', ', ')
            self.driver.implicitly_wait(5)
            print("Primary Address: "+p_add)
            self.data_dict['Primary Address'] = p_add
            nom = ArcGIS()
            coor = nom.geocode(p_add)
            print("Primary Address Latitude: "+str(coor.latitude))
            self.data_dict['Primary Address Latitude'] = str(coor.latitude)
            print("Primary Address Longitude: "+str(coor.longitude))
            self.data_dict['Primary Address Longitude'] = str(coor.longitude)
        except:
            self.data_dict['Primary Address'] = 'N/A'
            self.data_dict['Primary Address Latitude'] = 'N/A'
            self.data_dict['Primary Address Longitude'] = 'N/A'

        try:
            p_phone = self.driver.find_element(By.XPATH, '//div[@class="col-md-6"]/dl/dd/a').text
            self.driver.implicitly_wait(5)
            print("Primary Phone: "+p_phone)
            self.data_dict['Primary Phone'] = p_phone
        except:
            self.data_dict['Primary Phone'] = 'N/A'

    def get_other_information(self):
        body = self.driver.find_element(By.TAG_NAME, 'body')
        self.driver.implicitly_wait(5)
        for _ in range(0, 16):
            body.send_keys(Keys.ARROW_DOWN)
        try:
            click_on = self.driver.find_element(By.XPATH, '//section[@id="OtherPractices"]/div[1]')
            self.driver.implicitly_wait(15)
            click_on.click()
            time.sleep(5)
            try:
                o_uni_1 = self.driver.find_element(By.XPATH, '//section[@id="OtherPractices"]/div/div/ul/li/h6').text
                self.driver.implicitly_wait(15)
                print("Other University/Clinic 1: "+o_uni_1)
                self.data_dict['Other University/Clinic 1'] = o_uni_1
            except:
                self.data_dict['Other University/Clinic 1'] = 'N/A'

            try:
                o_add_1 = self.driver.find_element(By.XPATH, '//section[@id="OtherPractices"]/div/div/ul/li[1]/div/address').text.replace('\n', ', ')
                self.driver.implicitly_wait(15)
                print("Other Address 1: "+o_add_1)
                self.data_dict['Other Address 1'] = o_add_1
                nom = ArcGIS()
                coor = nom.geocode(o_add_1)
                print("Other Address 1 Latitude: " + str(coor.latitude))
                self.data_dict['Other Address 1 Latitude'] = str(coor.latitude)
                print("Other Address 1 Longitude: " + str(coor.longitude))
                self.data_dict['Other Address 1 Longitude'] = str(coor.longitude)
            except:
                self.data_dict['Other Address 1'] = 'N/A'
                self.data_dict['Other Address 1 Latitude'] = 'N/A'
                self.data_dict['Other Address 1 Longitude'] = 'N/A'

            try:
                o_p_1 = self.driver.find_element(By.XPATH, '//section[@id="OtherPractices"]/div/div/ul/li[1]/div/dl/dd/a').text
                self.driver.implicitly_wait(15)
                print("Other Phone 1: "+o_p_1)
                self.data_dict['Other Phone 1'] = o_p_1
            except:
                self.data_dict['Other Phone 1'] = 'N/A'

            try:
                o_uni_2 = self.driver.find_element(By.XPATH, '//section[@id="OtherPractices"]/div/div/ul/li[2]/h6').text
                self.driver.implicitly_wait(15)
                print("Other University/Clinic 2: " + o_uni_2)
                self.data_dict['Other University/Clinic 2'] = o_uni_2
            except:
                self.data_dict['Other University/Clinic 2'] = 'N/A'

            try:
                o_add_2 = self.driver.find_element(By.XPATH, '//section[@id="OtherPractices"]/div/div/ul/li[2]/div/address').text.replace('\n', ', ')
                self.driver.implicitly_wait(15)
                print("Other Address 2: "+o_add_2)
                self.data_dict['Other Address 2'] = o_add_2
                nom = ArcGIS()
                coor = nom.geocode(o_add_2)
                print("Other Address 2 Latitude: " + str(coor.latitude))
                self.data_dict['Other Address 2 Latitude'] = str(coor.latitude)
                print("Other Address 2 Longitude: " + str(coor.longitude))
                self.data_dict['Other Address 2 Longitude'] = str(coor.longitude)
            except:
                self.data_dict['Other Address 2'] = 'N/A'
                self.data_dict['Other Address 2 Latitude'] = 'N/A'
                self.data_dict['Other Address 2 Longitude'] = 'N/A'

            try:
                o_p_2 = self.driver.find_element(By.XPATH, '//section[@id="OtherPractices"]/div/div/ul/li[2]/div/dl/dd/a').text
                self.driver.implicitly_wait(15)
                print("Other Phone 2: "+o_p_2)
                self.data_dict['Other Phone 2'] = o_p_2
            except:
                self.data_dict['Other Phone 2'] = 'N/A'

        except:
            self.data_dict['Other University/Clinic 1'] = 'N/A'
            self.data_dict['Other Address 1'] = 'N/A'
            self.data_dict['Other Address 1 Latitude'] = 'N/A'
            self.data_dict['Other Address 1 Longitude'] = 'N/A'
            self.data_dict['Other Phone 1'] = 'N/A'
            self.data_dict['Other University/Clinic 2'] = 'N/A'
            self.data_dict['Other Address 2'] = 'N/A'
            self.data_dict['Other Address 2 Latitude'] = 'N/A'
            self.data_dict['Other Address 2 Longitude'] = 'N/A'
            self.data_dict['Other Phone 2'] = 'N/A'


    def get_other_professional_information(self):
        body = self.driver.find_element(By.TAG_NAME, 'body')
        self.driver.implicitly_wait(5)
        for _ in range(0, 12):
            body.send_keys(Keys.ARROW_DOWN)
        try:
            p_info_btn = self.driver.find_element(By.XPATH, '//section[@id="OtherPractices"]/div[2]')
            self.driver.implicitly_wait(5)
            p_info_btn.click()
            time.sleep(3)
            try:
                coop_name = self.driver.find_element(By.XPATH, '//div[@class="professionalCorpInfo open"]//div/ul/li/address/strong').text
                self.driver.implicitly_wait(15)
                print("Corporation Name: "+coop_name)
                self.data_dict['Corporation Name'] = coop_name

            except:
                self.data_dict['Corporation Name'] = 'N/A'

            try:
                address = []
                coop_add = self.driver.find_elements(By.XPATH, '//div[@class="professionalCorpInfo open"]//div/ul/li/address/span')
                self.driver.implicitly_wait(5)
                for c in coop_add:
                    address.append(c.text.replace('\n', ', '))
                add = str(address)
                print("Corporation Address: "+add.removeprefix("['").removesuffix("']").replace("'", ''))
                self.data_dict['Corporation Address'] = add.removeprefix("['").removesuffix("']").replace("'", '')
                nom = ArcGIS()
                coor = nom.geocode(add.removeprefix("['").removesuffix("']").replace("'", ''))
                print("Corporation Latitude: "+str(coor.latitude))
                self.data_dict['Corporation Latitude'] = str(coor.latitude)
                print("Corporation Longitude: "+str(coor.longitude))
                self.data_dict['Corporation Longitude'] = str(coor.longitude)
                address.clear()
            except:
                self.data_dict['Corporation Address'] = 'N/A'
                self.data_dict['Corporation Latitude'] = 'N/A'
                self.data_dict['Corporation Longitude'] = 'N/A'

            try:
                coor_p = self.driver.find_element(By.XPATH, '//section[@id="OtherPractices"]/div[2]/div/ul/li/address/span/a').text
                self.driver.implicitly_wait(5)
                print("Corporation Phone: "+coor_p)
                self.data_dict['Corporation Phone'] = coor_p
            except:
                self.data_dict['Corporation Phone'] = 'N/A'

            try:
                certificate = self.driver.find_element(By.XPATH, '//section[@id="OtherPractices"]/div[2]/div/ul/li/dl/dd[1]').text
                self.driver.implicitly_wait(5)
                print('Certificate of Authorization Status: '+certificate)
                self.data_dict['Certificate of Authorization Status'] = certificate
            except:
                self.data_dict['Certificate of Authorization Status'] = 'N/A'

            try:
                certificate1 = self.driver.find_element(By.XPATH, '//section[@id="OtherPractices"]/div[2]/div/ul/li/dl/dd[2]').text
                self.driver.implicitly_wait(5)
                print('Certificate of Authorization Issuance: ' + certificate1)
                self.data_dict['Certificate of Authorization Issuance'] = certificate1
            except:
                self.data_dict['Certificate of Authorization Issuance'] = 'N/A'
        except:
            self.data_dict['Corporation Name'] = 'N/A'
            self.data_dict['Corporation Address'] = 'N/A'
            self.data_dict['Corporation Latitude'] = 'N/A'
            self.data_dict['Corporation Longitude'] = 'N/A'
            self.data_dict['Corporation Phone'] = 'N/A'
            self.data_dict['Certificate of Authorization Status'] = 'N/A'
            self.data_dict['Certificate of Authorization Issuance'] = 'N/A'

    def get_academic_information(self):
        try:
            dental_deg = self.driver.find_element(By.XPATH, '//section[@id="Academic"]/div/dl[2]/dd').text
            self.driver.implicitly_wait(5)
            print("Dental Degree: "+dental_deg)
            self.data_dict['Dental Degree'] = dental_deg
        except:
            self.data_dict['Dental Degree'] = 'N/A'

        try:
            dental_deg_year = self.driver.find_element(By.XPATH, '//section[@id="Academic"]/div/dl[2]/dt').text
            self.driver.implicitly_wait(5)
            print("Dental Degree Year: "+dental_deg_year)
            self.data_dict['Dental Degree Year'] = dental_deg_year
        except:
            self.data_dict['Dental Degree Year'] = 'N/A'

        try:
            spec_training = self.driver.find_element(By.XPATH, '//section[@id="Academic"]/div/dl[1]/dd').text
            self.driver.implicitly_wait(5)
            print("Speciality Training: "+spec_training)
            self.data_dict['Speciality Training'] = spec_training
        except:
            self.data_dict['Speciality Training'] = 'N/A'

        try:
            spec_train_year = self.driver.find_element(By.XPATH, '//section[@id="Academic"]/div/dl[1]/dt').text
            self.driver.implicitly_wait(5)
            print("Speciality Training Year: "+spec_train_year)
            self.data_dict['Speciality Training Year'] = spec_train_year
        except:
            self.data_dict['Speciality Training Year'] = 'N/A'

    def get_certificates(self):
        try:
            cs = self.driver.find_element(By.XPATH, '//section[@id="Membership"]/div/dl/dd/time').text
            self.driver.implicitly_wait(5)
            print("Current Certificate(s) of Registration and Date(s) of Issuance: "+cs)
            self.data_dict['Current Certificate(s) of Registration and Date(s) of Issuance'] = cs
        except:
            self.data_dict['Current Certificate(s) of Registration and Date(s) of Issuance'] = 'N/A'

        try:
            ind = self.driver.find_element(By.XPATH, '//section[@id="Membership"]/div/time').text
            self.driver.implicitly_wait(5)
            print("Initial Date of Registration: "+ind)
            self.data_dict['Initial Date of Registration'] = ind
        except:
            self.data_dict['Initial Date of Registration'] = 'N/A'

    def add_url(self, u):
        print("Url: "+str(u))
        self.data_dict['Listing Url'] = u

    def mov_into_file(self, n):
        p = pd.DataFrame([self.data_dict])
        p.to_csv(f"path to save/{n}.csv", mode='a', header=not os.path.exists(f"path to save/{n}.csv"), index=False)


links = []
name = str(input("Enter Name: "))
bot = CanadianDentistData()
with open(f"path to file/{name}.csv") as file:
    for f in file:
        links.append(f)

for l in links:
    try:
        bot.land_required_page(l)
        bot.get_name()
        bot.get_full_name()
        bot.get_Registration_number()
        bot.current_Status()
        bot.get_Type(name)
        bot.get_primary_practice_information()
        bot.get_other_information()
        bot.get_other_professional_information()
        bot.get_academic_information()
        bot.get_certificates()
        bot.add_url(l)
        bot.mov_into_file(name)
    except:
        time.sleep(600)
        print("Error Produce Somewhere!!!!!!!!!")


