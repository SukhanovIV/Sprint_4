from selenium.webdriver.common.by import By


class AboutRentLocators:

    order = [By.XPATH, "//*[@class='Button_Button__ra12g Button_Middle__1CSJM']"]  # Кнопка "Заказать" финальная
    when_to_bring = [By.XPATH,
                     "//*[@class='Input_Input__1iN_Z Input_Responsible__1jDKN react-datepicker-ignore-onclickoutside']"]  # Поле выбора даты
    december_10th = [By.XPATH,
                     "//*[@class='react-datepicker__day react-datepicker__day--010 react-datepicker__day--weekend']"]  # Дата 10 декабря
    december_24th = [By.XPATH,
                     "//*[@class='react-datepicker__day react-datepicker__day--024 react-datepicker__day--weekend']"]  # Дата 10 декабря
    rental_period = [By.XPATH, "//div[contains(text(),'* Срок аренды')]"]  # Поле срок аренды
    one_day = [By.XPATH, "(//*[@class='Dropdown-option'])[1]"]  # 1 сутки
    three_day = [By.XPATH, "(//*[@class='Dropdown-option'])[3]"]  # 3 суток
    black_color = [By.XPATH, "(//*[@class='Checkbox_Label__3wxSf'])[1]"]  # Чёрный цвет самоката
    grey_color = [By.XPATH, "(//*[@class='Checkbox_Label__3wxSf'])[2]"]  # Серый цвет самоката
