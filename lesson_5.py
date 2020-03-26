import unittest, time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class admin_block_admin_access(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://isport.ua/")
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.header__content')))
        click_on_burger_menu= driver.find_element_by_css_selector('.header .header__content .wrapper.nav-wrapper .nav-ul li:nth-child(3) ').click()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()















