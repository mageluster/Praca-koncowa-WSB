#!/usr/bin/python
#coding=utf8
import unittest
from selenium import webdriver
import time
from faker import Faker
fake = Faker('pl_PL')

name = fake.name()
pesel = fake.ssn()
adress1 = fake.street_address()
adress2 = fake.building_number()
city = fake.city()
postcode = fake.postcode()
email = fake.email()
login = fake.user_name()
first_name = fake.first_name()
surname = fake.last_name()
job = fake.job()
phone = fake.phone_number()



class TauronRegistaration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()


    def test_registration_valid_user(self):
        driver = self.driver
        driver.get("https://swoz.tauron.pl/app/HomeServlet")
        login_btn = driver.find_element_by_xpath('//*[@id="header"]/ul/li/a')
        login_btn.click()
        register_btn = driver.find_element_by_xpath('//*[@id="loginForm"]/table/tbody/tr[3]/td/a/span').click()
        person_radio_btn = driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/table/tbody/tr[1]/td/table/tbody/tr[2]/td[1]/input')
        person_radio_btn.click()
        name_field = driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/table/tbody/tr[2]/td/input')
        name_field.send_keys(name)
        pesel_field = driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/table/tbody/tr[4]/td/input')
        pesel_field.send_keys(pesel)
        adress1_field = driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/table/tbody/tr[6]/td/input')
        adress1_field.send_keys(adress1)
        adress2_field = driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/table/tbody/tr[7]/td/input')
        adress2_field.send_keys(adress2)
        city_field = driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/table/tbody/tr[10]/td/input')
        city_field.send_keys(city)
        postcode_field = driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/table/tbody/tr[11]/td/input')
        postcode_field.send_keys(postcode)
        region_field = driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/table/tbody/tr[12]/td/select/option[13]')
        region_field.location_once_scrolled_into_view
        region_field.click()
        region_field_select = driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/table/tbody/tr[12]/td/select')
        select = webdriver.support.select.Select(region_field_select)
        region_field_selected_option = select.first_selected_option
        region_field_selected_option_value = region_field_selected_option.get_attribute("value")
        country_field = driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/table/tbody/tr[13]/td/select/option[13]')
        country_field.location_once_scrolled_into_view
        country_field.click()
        country_field_select = driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/table/tbody/tr[13]/td/select')
        select = webdriver.support.select.Select(country_field_select)
        country_field_selected_option = select.first_selected_option
        country_field_selected_option_value = country_field_selected_option.get_attribute("value")
        email_field = driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/table/tbody/tr[16]/td/input')
        email_field.send_keys(email)
        leading_category_button = driver.find_element_by_xpath('//a[contains(@href,"CategoryLeadingCategory")]').click()
        driver.switch_to.window(driver.window_handles[1])
        leading_category_chose = driver.find_element_by_xpath('//*[@id="000001000005"]/div[1]/img').click()
        leading_category_chose1 = driver.find_element_by_xpath('//*[@id="checkbox_000001000005000004_name"]').click()
        driver.switch_to.window(driver.window_handles[0])
        leading_category_selected_value = driver.find_element_by_xpath('//*[@id="common-category__CategoryLeadingCategory"]').get_attribute("value")
        user_login_field = driver.find_element_by_xpath('//*[@id="content"]/form/div[6]/table/tbody/tr[1]/td/input')
        user_login_field.send_keys(login)
        name_field1 = driver.find_element_by_xpath('//*[@id="content"]/form/div[6]/table/tbody/tr[2]/td/input')
        name_field1.send_keys(first_name)
        surname_field = driver.find_element_by_xpath('//*[@id="content"]/form/div[6]/table/tbody/tr[3]/td/input')
        surname_field.send_keys(surname)
        job_field = driver.find_element_by_xpath('//*[@id="content"]/form/div[6]/table/tbody/tr[4]/td/input')
        job_field.send_keys(job)
        email_field1 = driver.find_element_by_xpath('//*[@id="content"]/form/div[6]/table/tbody/tr[5]/td/input')
        email_field1.send_keys(email)
        phone_field = driver.find_element_by_xpath('//*[@id="content"]/form/div[6]/table/tbody/tr[6]/td/input')
        phone_field.send_keys(phone)
        regulation_checkbox = driver.find_element_by_xpath('//*[@id="content"]/form/div[8]/table/tbody/tr[1]/td[1]/input')
        regulation_checkbox.click()
        acceptinf_checkbox = driver.find_element_by_xpath('//*[@id="content"]/form/div[8]/table/tbody/tr[2]/td[1]/input')
        acceptinf_checkbox.click()
        consent_checkbox = driver.find_element_by_xpath('//*[@id="content"]/form/div[8]/table/tbody/tr[3]/td[1]/input')
        consent_checkbox.click()
        next_btn = driver.find_element_by_xpath('//*[@id="content"]/form/center/input[1]')
        next_btn.click()
        # Sprawdzenie poprawności wprowadzonych danych
        contractorType_radio_button = driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/table/tbody/tr[1]/td/table/tbody/tr[2]/td[1]/input')
        contractorType_radio_button_selected = contractorType_radio_button.get_attribute("checked")
        self.assertEqual(contractorType_radio_button_selected, 'true', 'Invalid contractor type selected')
        name_field_value = driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/table/tbody/tr[2]/td/input').get_attribute("value")
        self.assertEqual(name_field_value, name)
        pesel_field_value = driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/table/tbody/tr[4]/td/input').get_attribute("value")
        self.assertEqual(pesel_field_value, pesel)
        address1_field_value = driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/table/tbody/tr[6]/td/input').get_attribute("value")
        self.assertEqual(address1_field_value, adress1)
        adress2_field_value = driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/table/tbody/tr[7]/td/input').get_attribute("value")
        self.assertEqual(adress2_field_value, adress2)
        city_field_value = driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/table/tbody/tr[10]/td/input').get_attribute("value")
        self.assertEqual(city_field_value, city)
        postcode_field_value = driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/table/tbody/tr[11]/td/input').get_attribute("value")
        self.assertEqual(postcode_field_value, postcode)
        region_field_value = driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/table/tbody/tr[12]/td/input').get_attribute("value")
        self.assertEqual(region_field_value, region_field_selected_option_value)
        country_field_value = driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/table/tbody/tr[13]/td/input').get_attribute("value")
        self.assertEqual(country_field_value, country_field_selected_option_value)
        email_field_value = driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/table/tbody/tr[16]/td/input').get_attribute("value")
        self.assertEqual(email_field_value, email)
        leading_category_value = driver.find_element_by_xpath('//*[@id="common-category__CategoryLeadingCategory"]').get_attribute("value")
        self.assertEqual(leading_category_value, leading_category_selected_value)
        user_login_field_value = driver.find_element_by_xpath('//*[@id="content"]/form/div[6]/table/tbody/tr[1]/td/input').get_attribute("value")
        self.assertEqual(user_login_field_value, login)
        name_field1_value = driver.find_element_by_xpath('//*[@id="content"]/form/div[6]/table/tbody/tr[2]/td/input').get_attribute("value")
        self.assertEqual(name_field1_value, first_name)
        surname_field_value = driver.find_element_by_xpath('//*[@id="content"]/form/div[6]/table/tbody/tr[3]/td/input').get_attribute("value")
        self.assertEqual(surname_field_value, surname)
        job_field_value = driver.find_element_by_xpath('//*[@id="content"]/form/div[6]/table/tbody/tr[4]/td/input').get_attribute("value")
        self.assertEqual(job_field_value, job)
        email_field1_value = driver.find_element_by_xpath('//*[@id="content"]/form/div[6]/table/tbody/tr[5]/td/input').get_attribute("value")
        self.assertEqual(email_field1_value, email)
        phone_field_value = driver.find_element_by_xpath('//*[@id="content"]/form/div[6]/table/tbody/tr[6]/td/input').get_attribute("value")
        self.assertEqual(phone_field_value, phone)
        regulation_checkbox_value = driver.find_element_by_xpath('//*[@id="content"]/form/div[8]/table/tbody/tr[1]/td[1]/input').get_attribute("value")
        self.assertEqual(regulation_checkbox_value, 'true')
        acceptinf_checkbox_value = driver.find_element_by_xpath('//*[@id="content"]/form/div[8]/table/tbody/tr[2]/td[1]/input').get_attribute("value")
        self.assertEqual(acceptinf_checkbox_value, 'true')
        consent_checkbox_value = driver.find_element_by_xpath('//*[@id="content"]/form/div[8]/table/tbody/tr[3]/td[1]/input').get_attribute("value")
        self.assertEqual(consent_checkbox_value, 'true')

        #Nie klikam "Zapisz" żeby nie zakładać konta
        #save_btn = driver.find_element_by_xpath('//*[@id="content"]/form/center/input[2]').click()

        time.sleep(3)


if __name__ == "__main__":
    unittest.main()