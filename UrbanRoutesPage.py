import self
from matplotlib.testing.widgets import click_and_drag
from mpl_toolkits.axisartist.angle_helper import select_step_degree

import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    taxi_button = (By.CLASS_NAME, 'auth_select__button')
    comfort_button = (By.CLASS_NAME, 'auth_select__button')
    phone_number_field = (By.ID, 'phone_number')
    card_number_field = (By.CLASS_NAME, 'card_input')
    card_code_field = (By.ID, 'code')
    message_driver_field = (By.ID, 'message')
    toggle_button_1 = (By.CLASS_NAME, 'auth_toggle__button')
    helado_button = (By.CLASS_NAME, 'auth_increment__button')
    book_taxi = (By.CLASS_NAME, 'auth_select_button')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_taxi_button(self):
        self.driver.find_element(By.CLASS_NAME, "auth_select__button").click('Pedir un taxi')
        return self.driver.find_element(*self.taxi_button).get_property('value')

    def click_comfort_button(self):
        self.driver.find_element(By.CLASS_NAME, "auth_select__button").click('Comfort $10')
        return self.driver.find_element(*self.comfort_button).get_property('value')

    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_number_field).get_property('value')

    def set_card_input(self, card_number):
        self.driver.find_element(*self.card_number_field).send_keys(card_number)

    def set_code(self, card_code):
        self.driver.find_element(*self.card_code_field).send_keys(card_code)

    def get_card_input(self):
        return self.driver.find_element(*self.card_number_field).get_property('value')

    def get_code(self):
        return self.driver.find_element(*self.card_code_field).get_property('value')

    def set_message(self, message_for_driver):
        self.driver.find_element(*self.message_driver_field).send_keys(message_for_driver)

    def get_message(self):
        return self.driver.find_element(*self.message_driver_field).get_property('value')

    def click_toggle_button_1(self):
        self.driver.find_element(*self.toggle_button_1).click()

    def click_helado_button(self):
        self.driver.find_element(*self.helado_button).click(2)

    def click_book_taxi(self):
        self.driver.find_element(By.CLASS_NAME, "auth_select__button").click('Reservar')
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "buscar__automovil")))

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
