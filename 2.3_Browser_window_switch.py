from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_xpath("//button[@type='submit']").click()

    browser.switch_to.window(browser.window_handles[1])

    element = browser.find_element_by_id("input_value")
    x = element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer").send_keys(y)

    button = browser.find_element_by_xpath("//button[@type='submit']").click()

finally:
    ## успеваем скопировать код за 30 секунд
    time.sleep(10)
    ## закрываем браузер после всех манипуляций
    browser.quit()
