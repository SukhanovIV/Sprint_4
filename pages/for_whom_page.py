from locators.for_whom_locators import ForWhomLocators


class ForWhomPage:

    def __init__(self, driver):
        self.driver = driver

    def clicking_order_top(self):
        self.driver.find_element(*ForWhomLocators.order_top).click()

    def clicking_order_down(self):
        self.driver.find_element(*ForWhomLocators.order_down).click()

    def clicking_button_further(self):
        self.driver.find_element(*ForWhomLocators.button_further).click()

    def enter_name_1(self, example_1):
        self.driver.find_element(*ForWhomLocators.name_input_field).send_keys(example_1.name)
        return example_1

    def enter_name_2(self, example_2):
        self.driver.find_element(*ForWhomLocators.name_input_field).send_keys(example_2.name)
        return example_2

    def enter_lastname_1(self, example_1):
        self.driver.find_element(*ForWhomLocators.lastname_input_field).send_keys(example_1.lastname)
        return example_1

    def enter_lastname_2(self, example_2):
        self.driver.find_element(*ForWhomLocators.lastname_input_field).send_keys(example_2.lastname)
        return example_2

    def enter_address_1(self, example_1):
        self.driver.find_element(*ForWhomLocators.address_input_field).send_keys(example_1.address)
        return example_1

    def enter_address_2(self, example_2):
        self.driver.find_element(*ForWhomLocators.address_input_field).send_keys(example_2.address)
        return example_2

    def clicking_station_selection_field(self):
        self.driver.find_element(*ForWhomLocators.station_selection_field).click()

    def enter_phone_1(self, example_1):
        self.driver.find_element(*ForWhomLocators.phone_input_field).send_keys(example_1.phone)
        return example_1

    def enter_phone_2(self, example_2):
        self.driver.find_element(*ForWhomLocators.phone_input_field).send_keys(example_2.phone)
        return example_2
