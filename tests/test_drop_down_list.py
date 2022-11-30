from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.drop_down_locators_page import Questions


class TestQuestions:

    def test_answer_to_1_question(self, driver):
        Questions(driver).find_questions()
        WebDriverWait(driver, 20).until(
            ec.visibility_of_element_located(Questions.question_8))
        Questions(driver).clicking_question_1()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            Questions.answer_1))

    def test_answer_to_2_question(self, driver):
        Questions(driver).find_questions()
        WebDriverWait(driver, 20).until(
            ec.visibility_of_element_located(Questions.question_8))
        Questions(driver).clicking_question_2()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            Questions.answer_2))

    def test_answer_to_3_question(self, driver):
        Questions(driver).find_questions()
        WebDriverWait(driver, 20).until(
            ec.visibility_of_element_located(Questions.question_8))
        Questions(driver).clicking_question_3()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            Questions.answer_3))

    def test_answer_to_4_question(self, driver):
        Questions(driver).find_questions()
        WebDriverWait(driver, 20).until(
            ec.visibility_of_element_located(Questions.question_8))
        Questions(driver).clicking_question_4()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            Questions.answer_4))

    def test_answer_to_5_question(self, driver):
        Questions(driver).find_questions()
        WebDriverWait(driver, 20).until(
            ec.visibility_of_element_located(Questions.question_8))
        Questions(driver).clicking_question_5()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            Questions.answer_5))

    def test_answer_to_6_question(self, driver):
        Questions(driver).find_questions()
        WebDriverWait(driver, 20).until(
            ec.visibility_of_element_located(Questions.question_8))
        Questions(driver).clicking_question_6()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            Questions.answer_6))

    def test_answer_to_7_question(self, driver):
        Questions(driver).find_questions()
        WebDriverWait(driver, 20).until(
            ec.visibility_of_element_located(Questions.question_8))
        Questions(driver).clicking_question_7()
        assert WebDriverWait(driver, 20).until(ec.visibility_of_element_located(
            Questions.answer_7))
