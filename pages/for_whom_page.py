from selenium.webdriver.common.by import By


class ForWhom:
    order_top = [By.XPATH, "//*[@class='Button_Button__ra12g']"]  # Кнопка "Заказать" сверху
    order_down = [By.XPATH, "//*[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']"]  # Кнопка "Заказать" снизу
    button_further = [By.XPATH, "//button[contains(text(),'Далее')]"]  # Кнопка "Далее"
    name_input_field = [By.XPATH,
                        "(//*[@class='Input_Input__1iN_Z Input_Error__1Tx5d Input_Responsible__1jDKN'])[1]"]  # Поле ввода "Имя"
    lastname_input_field = [By.XPATH,
                            "(//*[@class='Input_Input__1iN_Z Input_Error__1Tx5d Input_Responsible__1jDKN'])[1]"]  # Поле ввода "Фамилия"
    address_input_field = [By.XPATH,
                           "(//*[@class='Input_Input__1iN_Z Input_Error__1Tx5d Input_Responsible__1jDKN'])[1]"]  # Поле ввода "Адрес"
    station_selection_field = [By.XPATH,
                               "(//*[@class='Input_Input__1iN_Z Input_Error__1Tx5d Input_Responsible__1jDKN'])[1]"]  # Поле выбора станции
    phone_input_field = [By.XPATH,
                         "(//*[@class='Input_Input__1iN_Z Input_Error__1Tx5d Input_Responsible__1jDKN'])[2]"]  # Поле ввода "Телефон"

    def __init__(self, driver):
        self.driver = driver

    def clicking_order_top(self):
        self.driver.find_element(*self.order_top).click()

    def clicking_order_down(self):
        self.driver.find_element(*self.order_down).click()

    def clicking_button_further(self):
        self.driver.find_element(*self.button_further).click()

    def enter_name_1(self, example_1):
        self.driver.find_element(*self.name_input_field).send_keys(example_1.name)
        return example_1

    def enter_name_2(self, example_2):
        self.driver.find_element(*self.name_input_field).send_keys(example_2.name)
        return example_2

    def enter_lastname_1(self, example_1):
        self.driver.find_element(*self.lastname_input_field).send_keys(example_1.lastname)
        return example_1

    def enter_lastname_2(self, example_2):
        self.driver.find_element(*self.lastname_input_field).send_keys(example_2.lastname)
        return example_2

    def enter_address_1(self, example_1):
        self.driver.find_element(*self.address_input_field).send_keys(example_1.address)
        return example_1

    def enter_address_2(self, example_2):
        self.driver.find_element(*self.address_input_field).send_keys(example_2.address)
        return example_2

    def enter_station_1(self, example_1):
        self.driver.find_element(*self.station_selection_field).send_keys(example_1.station)
        return example_1

    def enter_station_2(self, example_2):
        self.driver.find_element(*self.station_selection_field).send_keys(example_2.station)
        return example_2

    def enter_phone_1(self, example_1):
        self.driver.find_element(*self.phone_input_field).send_keys(example_1.phone)
        return example_1

    def enter_phone_2(self, example_2):
        self.driver.find_element(*self.phone_input_field).send_keys(example_2.phone)
        return example_2
