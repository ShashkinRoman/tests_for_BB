from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
from random import randint

# Создаем подключение, получаем страницу по урлу
def create_service(url):
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
    # переходим в раздел услуги
    find_button_service = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[1]/div/nav/ul/li[7]')))
    find_button_service.click()
    sleep(1)
    # find and click on button "add service"
    find_button_add_service = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[1]/div/main/div[2]/div[2]/div/div[1]/div[2]/div')))
    find_button_add_service.click()
    find_add_service = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[1]/div/main/div[2]/div[2]/div/div[1]/div[2]/div/div/ul/li[1]')))
    find_add_service.click()
    sleep(1)
    # add service in first category
    find_brow_category = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '//html/body/div[2]/div[1]/div[2]/div/ul/li[1]')))
    find_brow_category.click()
    sleep(1)
    add_yourself_service = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[2]/div[1]/div[2]/div/div[2]/div/div')))
    add_yourself_service.click()
    sleep(1)
    # description yourself service
    find_title_service = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[2]/div[2]/div[1]/div[1]/input')))
    find_title_service.send_keys('test service' + str(randint(1000000, 99999999)))
    find_price = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[2]/div[2]/div[2]/div/div[1]/input')))
    find_price.send_keys('1500')
    click_save = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[2]/div[2]/div[1]/div[2]/button[2]')))
    click_save.click()
    sleep(1)
    remove_at_home = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[1]/div/nav/ul/li[1]/a')))
    remove_at_home.click()
    sleep(2)
    driver.quit()


def main():
    url = 'https://beautybox.ru/beauty-site'
    try:
        create_service(url)
        print('--------------------------------------------------------------------')
        print('Test "create_client" completed')
        print('--------------------------------------------------------------------')
    except:
        print('Test "CREATE_CLIENT" FILED')


if __name__ == '__main__':
    main()