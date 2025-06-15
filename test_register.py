import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import os

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://seleniumdemo.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10.0)


    def testRegistration(self):
        self.driver.find_element(By.XPATH, "//span[@class='nav__title' and contains(text(), 'My account')]").click()
        email = os.environ.get("EMAIL")
        self.driver.find_element(By.ID, "reg_email").send_keys(email)
        # self.driver.find_element(By.ID,"reg_email").send_keys(Faker().email())
        self.driver.find_element(By.ID, "reg_password").send_keys(Faker().password())
        self.driver.find_element(By.XPATH, "//button[@name='register']").click()