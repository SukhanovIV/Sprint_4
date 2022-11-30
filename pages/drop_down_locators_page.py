from selenium.webdriver.common.by import By


class Questions:

    question_1 = [By.XPATH, "//div[@id='accordion__heading-0']"]  # "Сколько это стоит? И как оплатить?"
    question_2 = [By.XPATH, "//div[@id='accordion__heading-1']"]  # "Хочу сразу несколько самокатов! Так можно?"
    question_3 = [By.XPATH, "//div[@id='accordion__heading-2']"]  # "Как рассчитывается время аренды?"
    question_4 = [By.XPATH, "//div[@id='accordion__heading-3']"]  # "Можно ли заказать самокат прямо на сегодня?"
    question_5 = [By.XPATH,
                  "//div[@id='accordion__heading-4']"]  # "Можно ли продлить заказ или вернуть самокат раньше?"
    question_6 = [By.XPATH, "//div[@id='accordion__heading-5']"]  # "Вы привозите зарядку вместе с самокатом?"
    question_7 = [By.XPATH, "//div[@id='accordion__heading-6']"]  # "Можно ли отменить заказ?"
    question_8 = [By.XPATH, "//div[@id='accordion__heading-7']"]  # "Я жизу за МКАДом, привезёте?"

    answer_1 = [By.XPATH,
                "//p[contains(text(),'Сутки — 400 рублей. Оплата курьеру — наличными или')]"]  # Ответ на 1 вопрос
    answer_2 = [By.XPATH,
                "//p[contains(text(),'Пока что у нас так: один заказ — один самокат. Есл')]"]  # Ответ на 2 вопрос
    answer_3 = [By.XPATH,
                "//p[contains(text(),'Допустим, вы оформляете заказ на 8 мая. Мы привози')]"]  # Ответ на 3 вопрос
    answer_4 = [By.XPATH,
                "//p[contains(text(),'Только начиная с завтрашнего дня. Но скоро станем ')]"]  # Ответ на 4 вопрос
    answer_5 = [By.XPATH,
                "//p[contains(text(),'Пока что нет! Но если что-то срочное — всегда можн')]"]  # Ответ на 5 вопрос
    answer_6 = [By.XPATH,
                "//p[contains(text(),'Самокат приезжает к вам с полной зарядкой. Этого х')]"]  # Ответ на 6 вопрос
    answer_7 = [By.XPATH,
                "//p[contains(text(),'Да, пока самокат не привезли. Штрафа не будет, объ')]"]  # Ответ на 7 вопрос
    answer_8 = [By.XPATH,
                "//p[contains(text(),'Да, обязательно. Всем самокатов! И Москве, и Моско')]"]  # Ответ на 8 вопрос

    def __init__(self, driver):
        self.driver = driver

    def clicking_question_1(self):
        self.driver.find_element(*self.question_1).click()

    def clicking_question_2(self):
        self.driver.find_element(*self.question_2).click()

    def clicking_question_3(self):
        self.driver.find_element(*self.question_3).click()

    def clicking_question_4(self):
        self.driver.find_element(*self.question_4).click()

    def clicking_question_5(self):
        self.driver.find_element(*self.question_5).click()

    def clicking_question_6(self):
        self.driver.find_element(*self.question_6).click()

    def clicking_question_7(self):
        self.driver.find_element(*self.question_7).click()

    def clicking_question_8(self):
        self.driver.find_element(*self.question_8).click()

    def find_questions(self):
        element = self.driver.find_element(*self.question_8)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
