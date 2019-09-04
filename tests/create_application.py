'''Скрипт: логинится со страницы https://beautybox.ru/beauty-site
нажимает на раздел "заявки", кнопку "создать заявку", нажимает на поле клиента,
выбирает первого клиента, нажимает на поле мастера, нажимает в середину выпадающего
окна выбора мастеров и сохраняет заявку на 06:00 по времени.
'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0


# Создаем подключение, получаем страницу по урлу
def create_app(url):
    path = 'C:/Users/Обучение/Google Диск/Обучение python/2gisparser/chromedriver_32/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path)
    driver.set_window_size(1050, 1024)
    driver.get(url)
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
    sleep(3)
    # нажимаем на раздел заявки
    applications = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                '/html/body/div[1]/div/nav/ul/li[5]')))
    applications.click()
    # нажимаем на кнопку добавить заявку
    add_applications = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                        '//*[@id="jsProfileID"]/div/div/div[4]/div')))
    add_applications.click()
    sleep(1)
    # выбираем поле клиента
    select_master_two = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                        '/html/body/div[2]/div/div/div[2]/div[2]/div[1]/div[1]')))
    select_master_two.click()
    sleep(1)
    # выбираем первого по очереди клиента
    select_first_client = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                          '/html/body/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]')))
    select_first_client.click()
    sleep(1)
    # нажимаем на поле "добавить мастера", находим нажатое поле, нажимаем enter
    select_master_one = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                           '/html/body/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div/span[2]')))
    select_master_one.click()
    select_master_two = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                        '/html/body/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div/span[3]/span/span[1]/input')))
    select_master_two.send_keys('Сергей123')
    select_master_two.send_keys(Keys.ENTER)
    # сохраняем заявку
    sleep(1)
    save_application = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn__title')))
    save_application.click()
    sleep(5)
    driver.quit()


def main():
    url = 'https://beautybox.ru/beauty-site'
    try:
        create_app(url)
        print('--------------------------------------------------------------------')
        print('Test "create_application" completed')
        print('--------------------------------------------------------------------')
        return 2
    except:
        print('Test "CREATE_APPLICATION" FILED')
        return 0



if __name__ == '__main__':
    main()


