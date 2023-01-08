from selenium.webdriver.common.by import By


class ForWhomLocators:

    order_top = [By.XPATH, "//*[@class='Button_Button__ra12g']"]  # Кнопка "Заказать" сверху
    order_down = [By.XPATH, "//*[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']"]  # Кнопка "Заказать" снизу
    button_further = [By.XPATH, "//button[contains(text(),'Далее')]"]  # Кнопка "Далее"
    name_input_field = [By.XPATH,
                        "(//*[@class='Input_Input__1iN_Z Input_Error__1Tx5d Input_Responsible__1jDKN'])[1]"]  # Поле ввода "Имя"
    lastname_input_field = [By.XPATH,
                            "(//*[@class='Input_Input__1iN_Z Input_Error__1Tx5d Input_Responsible__1jDKN'])[2]"]  # Поле ввода "Фамилия"
    address_input_field = [By.XPATH,
                           "((//*[@class='Input_Input__1iN_Z Input_Filled__1rDxs Input_Responsible__1jDKN'])[1]"]  # Поле ввода "Адрес"
    station_selection_field = [By.XPATH, "//*[@class='select-search__input']"]  # Поле выбора станции
    phone_input_field = [By.XPATH,
                         "((//*[@class='Input_Input__1iN_Z Input_Filled__1rDxs Input_Responsible__1jDKN'])[2]"]  # Поле ввода "Телефон"
