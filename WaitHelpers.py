import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import self

class WaitHelpers:
    driver = None

    def __init__(self, driver):
         self.driver = driver

# Agregar una espera explícita para que se cargue el feed
         WebDriverWait(self.driver, 3).until(
    expected_conditions.visibility_of_element_located((By.CLASS_NAME, "auth_select__button").click('Pedir un taxi')))


