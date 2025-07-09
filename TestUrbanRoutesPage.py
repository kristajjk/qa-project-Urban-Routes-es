import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from UrbanRoutesPage import UrbanRoutesPage
import self

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
        assert taxi_button.click('Pedir un taxi')

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
            assert 'Manta y pañuelos' in toggle_button_1

    def test_click_helado_button(self, span = 2):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_helado_button()
        assert increment__button in helado_button == 2

    def test_click_book_taxi(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_book_taxi()
        assert WebDriverWait(self.driver, 20) if click_book_taxi else None

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()