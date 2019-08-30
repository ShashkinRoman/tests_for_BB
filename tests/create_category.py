from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
from random import randint


# Создаем подключение, получаем страницу по урлу
def create_category(url):
    path = 'C:/Users/Обучение/Google Диск/Обучение python/2gisparser/chromedriver_32/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path)
    driver.get(url)
    # закрываем пуш
    sleep(2)
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
    find_button_add_service = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[1]/div/main/div[2]/div[2]/div/div[1]/div[2]/div')))
    find_button_add_service.click()
    # find and click add category
    add_category = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[1]/div/main/div[2]/div[2]/div/div[1]/div[2]/div/div/ul/li[2]')))
    add_category.click()
    sleep(2)
    # add yourself category
    add_yourself_category = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[2]/div/div[2]/div/div[1]/div')))
    add_yourself_category.click()
    sleep(1)
    # title category and save
    find_title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[2]/div[1]/div[2]/div/div[1]/input')))
    find_title.send_keys('test category ' + str(randint(1000000, 9999999)))
    sleep(1)
    save_category = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[2]/div[1]/div[3]/button')))
    save_category.click()
    sleep(2)
    # delete yorself category
    # find_menu = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CLASS_NAME,
    #                                     'item-services__controls')))
    # find_menu.click()
    # sleep(2)
    # delete_category = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CLASS_NAME,
    #                                     'jsCrmCategoriesDeleteItemLink')))
    # delete_category.click()
    # sleep(2)
    # accept_delete = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH,
    #                                     '//*[@id="delete"]/div/div/div[2]/button[1]')))
    # accept_delete.click()

    remove_at_home = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[1]/div/nav/ul/li[1]/a')))
    remove_at_home.click()
    sleep(2)
    driver.quit()

def main():
    url = 'https://beautybox.ru/beauty-site'
    try:
        create_category(url)
        print('--------------------------------------------------------------------')
        print('Test "create_client" completed')
        print('--------------------------------------------------------------------')
    except:
        print('Test "CREATE_CLIENT" FILED')


if __name__ == '__main__':
    main()