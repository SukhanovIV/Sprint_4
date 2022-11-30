from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.for_whom_page import ForWhom


class TestOrder:

    def test_answer_to_1_question(self, driver, example_1):
        ForWhom(driver).clicking_order_top()
        WebDriverWait(driver, 20).until(
            ec.visibility_of_element_located(ForWhom.button_further))
        ForWhom(driver).clicking_order_top()
