from selenium import webdriver
import time
import unittest

def fill_form(link):
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath("//div[label[contains(., 'First name*')]]/input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//div[label[contains(., 'Last name*')]]/input")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("//div[label[contains(., 'Email*')]]/input")
    input3.send_keys("mail@mail.com")
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    return browser.find_element_by_tag_name("h1").text
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    browser.quit

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual("Congratulations! You have successfully registered!", fill_form("http://suninjuly.github.io/registration1.html"), 'Should be Message')

    def test_abs2(self):
        self.assertEqual("Congratulations! You have successfully registered!", fill_form("http://suninjuly.github.io/registration2.html"), 'Should be Message')

if __name__ == "__main__":
    unittest.main()
