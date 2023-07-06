import unittest

import self
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import time

from Demo1 import driver


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        print("setup called")

    def tearDown(self):
        print("Tear down called")
        self.driver.quit()

    def test_testLoginTC1(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        time.sleep(10)

        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(10)

        dashboard = self.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[1]/header/div[1]/div[1]/span/h6")

        self.assertEqual(True, dashboard.is_displayed())

        self.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
        time.sleep(7)

        username = self.driver.find_element(By.NAME, "username")
        self.assertEqual(True, username.is_displayed())

        def PIM_01(self):
            self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
            self.driver.maximize_window()
            time.sleep(10)
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_elements(By.XPATH, "//*[@id=\"app\"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        # Navigate to the Add Employee page
        self.driver.find_element(By.class_name, "oxd-main-menu-item active").click()
        self.driver.find_element(By.class_name, "(oxd-button oxd-button--medium oxd-button--secondary").click()

        # Fill in the employee details
        first_name = driver.find_element_by_id("firstName")
        last_name = driver.find_element_by_id("lastName")
        employee_id = driver.find_element_by_id("employeeId")
        first_name.send_keys("John")
        last_name.send_keys("Doe")
        employee_id.send_keys("12345")
        dashboard = self.driver.find_element(By.XPATH,"//*[@id=\"app\"]/div[1]/div[1]/header/div[1]/div[1]/span/h6")

        self.assertEqual(True,dashboard.is_displayed())

        self.driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
        time.sleep(7)

        username = self.driver.find_element(By.NAME, "username")
        self.assertEqual(True, username.is_displayed())

        self.driver.close()

if __name__ == '__main__':
    unittest.main()
