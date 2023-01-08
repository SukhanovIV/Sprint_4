from locators.about_rent_locators import AboutRentLocators


class AboutRentPage:

    def __init__(self, driver):
        self.driver = driver

    def clicking_order(self):
        self.driver.find_element(*AboutRentLocators.order).click()

    def clicking_when_to_bring(self):
        self.driver.find_element(*AboutRentLocators.when_to_bring).click()

    def clicking_december_10th(self):
        self.driver.find_element(*AboutRentLocators.december_10th).click()

    def clicking_december_24th(self):
        self.driver.find_element(*AboutRentLocators.december_24th).click()

    def clicking_rental_period(self):
        self.driver.find_element(*AboutRentLocators.rental_period).click()

    def choice_one_day(self):
        self.driver.find_element(*AboutRentLocators.one_day).click()

    def choice_three__day(self):
        self.driver.find_element(*AboutRentLocators.three_day).click()

    def clicking_black_color(self):
        self.driver.find_element(*AboutRentLocators.black_color).click()

    def clicking_grey_color(self):
        self.driver.find_element(*AboutRentLocators.grey_color).click()
