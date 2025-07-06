import self
from matplotlib.testing.widgets import click_and_drag
from mpl_toolkits.axisartist.angle_helper import select_step_degree

import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


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

    class TestUrbanRoutes:
        driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_click_taxi_button(self, taxi_button ='Pedir un taxi'):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_taxi_button()
        assert taxi_button.select('Pedir un taxi')

    def test_click_comfort_button(self, comfort_button ='Comfort $10'):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_comfort_button()
        assert comfort_button.select('Comfort $10')

    def test_set_phone_number(self):
            self.driver.get(data.urban_routes_url)
            routes_page = UrbanRoutesPage(self.driver)
            phone_number = data.phone_number
            routes_page.set_phone_number()
            assert routes_page.get_phone_number() == phone_number

    def test_add_card(self):
            self.click_add_card_button()
            self.driver.get(data.urban_routes_url)
            routes_page = UrbanRoutesPage(self.driver)
            card_number = data.card_number
            card_code = data.card_code
            routes_page.set_card(card_number, card_code)
            assert routes_page.get_card_input() == card_number
            assert routes_page.get_code() == card_code

    def test_set_message(self):
            self.driver.get(data.urban_routes_url)
            routes_page = UrbanRoutesPage(self.driver)
            message_for_driver = data.message_for_driver
            routes_page.set_message()
            assert routes_page.get_message() == message_for_driver

    def test_click_toggle_button_1(self, toggle_button_1 ='Manta y pañuelos'):
            self.driver.get(data.urban_routes_url)
            routes_page = UrbanRoutesPage(self.driver)
            self.click_toggle_button_1()

    def test_click_helado_button(self, span = 2):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_helado_button()
        assert increment__button in helado_button == 2


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
