from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0


# Создаем подключение, получаем страницу по урлу
def authorization(url):
    path = 'C:/Users/Обучение/Google Диск/Обучение python/2gisparser/chromedriver_32/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path)
    driver.get(url)
    # закрываем пуш
    sleep(1)
    close_push = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]')))
    close_push.click()
    sleep(1)
    # кнопка получтьб бесплатно
    take_button = driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/section[1]/div/div/div/a')
    take_button.click()
    sleep(1)
    # ввод логина и пароля
    login = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'js-main-input-phone')))
    login.send_keys('1113333333')
    password = driver.find_element_by_id('js-main-input-password')
    password.send_keys('123456')
    sleep(1)
    # нажимаем получить бесплатно
    button_take_free = driver.find_element_by_id('js-login-account')
    button_take_free.click()
    sleep(2)
    # закрываем пуш
    close_push2 = driver.find_element_by_xpath('/html/body/div[1]')
    close_push2.click()
    # нажимаем на раздел инстаграм, чтобы проверить, что страница кабинета прогрузилась
    instagram = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                '/html/body/div[1]/div/nav/ul/li[8]')))
    instagram.click()
    sleep(2)
    driver.quit()


def main():
    url = 'https://beautybox.ru/beauty-site'
    try:
        authorization(url)
        print('--------------------------------------------------------------------')
        print('Test "authorization" completed')
        print('--------------------------------------------------------------------')
    except:
        print('Test "AUTHORIZATION" FILED')


if __name__ == '__main__':
    main()