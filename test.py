from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0


ff = webdriver.Firefox()
ff.get("http://somedomain/url_that_delays_loading")
try:
# Создаем подключение, получаем страницу по урлу
def authorization(url):
    path = 'C:/Users/Обучение/Google Диск/Обучение python/2gisparser/chromedriver_32/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path)
    driver.get(url)
    sleep(2)
    close_push_test = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]')))
    # закрываем пуш
    close_push = driver.find_element_by_xpath('/html/body/div[1]')
    close_push.click()
    # кнопка получтьб бесплатно
    take_button = driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/section[1]/div/div/div/a')
    take_button.click()
    sleep(2)
    # ввод логина и пароля
    login = driver.find_element_by_id('js-main-input-phone')
    login.click()
    login.send_keys('1113333333')
    password = driver.find_element_by_id('js-main-input-password')
    password.send_keys('123456')
    sleep(2)
    # нажимаем получить бесплатно
    button_take_free = driver.find_element_by_id('js-login-account')
    button_take_free.click()
    sleep(2)
    # закрываем пуш
    close_push2 = driver.find_element_by_xpath('/html/body/div[1]')
    close_push2.click()
    sleep(1)
    # нажимаем на раздел инстаграм
    instagram = driver.find_element_by_xpath('/html/body/div[1]/div/nav/ul/li[8]')
    instagram.click()
    sleep(2)
    driver.quit()


def main():
    url = 'https://beautybox.ru/beauty-site'
    try:
        authorization(url)
    except:
        print('Test autheorization failed')


if __name__ == '__main__':
    main()