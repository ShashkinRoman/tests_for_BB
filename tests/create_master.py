from time import sleep
from selenium import webdriver
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains

# Создаем подключение, получаем страницу по урлу
def create_master(url):
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
    # select "about salon" and click employees
    sleep(2)
    find_button_service = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[1]/div/nav/ul/li[7]')))
    find_button_service.click()
    sleep(1)
    find_employees = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[1]/div/div/header/nav/ul/li[2]')))
    find_employees.click()
    sleep(2)
    # find and click button "added employees
    find_button_add_employeed = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[1]/div/main/div[2]/div/div[1]/div[2]/div')))
    find_button_add_employeed.click()
    sleep(2)
    # complete info about employees and save
    find_title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[2]/div/div/div[2]/div[1]/div/div[3]/div[1]/input')))
    find_title.send_keys('test employees')

    find_phone = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[2]/div/div/div[2]/div[1]/div/div[3]/div[2]/input')))
    find_phone.send_keys(randint(70000000000, 99999999999))

    find_email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[2]/div/div/div[2]/div[1]/div/div[4]/div[1]/input')))
    find_email.send_keys(str(randint(70000000000, 99999999999)) + "@gmail.com")

    find_checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[2]/div/div/div[2]/div[1]/div/label/span[1]')))
    find_checkbox.click()

    find_input_category = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '//*[@id="aplication-services"]/div[2]/div[2]/span')))
    find_input_category.click()
    ActionChains(driver).move_to_element(find_input_category).move_by_offset(1, 100).click().perform()

    find_checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[2]/div/div/div[3]/div/div/button[2]')))
    find_checkbox.click()
    sleep(2)
    # delete new employees
    find_new_employees= WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME,
                                        'jsCrmEmployeesAssociateItem ')))
    find_new_employees.click()

    find_button_delete = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/div[2]/div/div/div[3]/div/div/button[1]')))
    find_button_delete.click()

    find_button_delete2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '//*[@id="delete"]/div/div/div[2]/button[1]')))
    find_button_delete2.click()
    sleep(2)
    driver.quit()


def main():
    url = 'https://beautybox.ru/beauty-site'
    try:
        create_master(url)
        print('--------------------------------------------------------------------')
        print('Test "create_master" completed')
        print('--------------------------------------------------------------------')
    except:
        print('Test "CREATE_MASTER" FILED')


if __name__ == '__main__':
    main()