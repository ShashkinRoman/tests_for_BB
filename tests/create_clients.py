from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
from random import randint

# Создаем подключение, получаем страницу по урлу
def create_client(url):
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
    # нажимаем на раздел клиенты, чтобы проверить, что страница кабинета прогрузилась
    find_ckient = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                '/html/body/div[1]/div/nav/ul/li[6]')))
    find_ckient.click()
    sleep(2)
    # Находим и нажимаем кнопку добавить клиента
    find_button_add_client = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                  '/html/body/div[1]/div/main/div[2]/div/div[1]/div[2]')))
    find_button_add_client.click()
    # Заполнием инфу о клиенте
    find_name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                      '//*[@id="aplication-info"]/div[2]/div[2]/div[1]/input')))
    find_name_input.click() #кликаем в поле "Имя и фамилия"
    find_name_input.send_keys('Test client') #вводим текст в поле "Имя и фамилия"
    # Ищем меню роли клиента
    find_role_client = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                      '//*[@id="aplication-info"]/div[2]/div[2]/div[2]/span[2]/span[1]/span')))
    find_role_client.click()
    sleep(0.5)
    ActionChains(driver).move_to_element(find_role_client).move_by_offset(1, 100).click().perform()
    # Ищем поле номерa, e-mail, скидку, комментарий, пол, дату и вводим
    find_phone_number = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="aplication-info"]/div[2]/div[3]/div[1]/input')))
    find_phone_number.send_keys(randint(1111111111, 9999999999))
    sleep(0.5)

    find_email_number = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="aplication-info"]/div[2]/div[3]/div[2]/input')))
    find_email_number.send_keys('test@mail.ru')
    sleep(1)
    # day
    find_date_of_birth_day = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="aplication-info"]/div[2]/div[4]/div/div/div/div[1]/span/span[1]/span')))
    find_date_of_birth_day.click()
    sleep(0.5)
    # Перемещаем мышь относительно выбранного элемента на 100 пикселей вниз
    ActionChains(driver).move_to_element(find_date_of_birth_day).move_by_offset(1, 100).click().perform()
    # month
    find_date_of_birth_month = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="aplication-info"]/div[2]/div[4]/div/div/div/div[2]/span')))
    find_date_of_birth_month.click()
    ActionChains(driver).move_to_element(find_date_of_birth_month).move_by_offset(1, 100).click().perform()
    # year
    find_date_of_birth_year = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '//*[@id="aplication-info"]/div[2]/div[4]/div/div/div/a')))
    find_date_of_birth_year.click()
    find_date_of_birth_year2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '//*[@id="aplication-info"]/div[2]/div[4]/div/div/div/div[3]/span')))
    find_date_of_birth_year2.click()
    ActionChains(driver).move_to_element(find_date_of_birth_year2).move_by_offset(1, 100).click().perform()
    # gender
    find_gender = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        '//*[@id="aplication-info"]/div[2]/div[5]/div[1]/span[2]')))
    find_gender.click()
    ActionChains(driver).move_to_element(find_gender).move_by_offset(1, 100).click().perform()
    # sale
    find_sale = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="aplication-info"]/div[2]/div[5]/div[2]/input')))
    find_sale.click()
    find_sale.send_keys('50')
    # comment
    find_comment = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="aplication-info"]/div[2]/div[6]/div/div/textarea')))
    find_comment.click()
    find_comment.send_keys('kakioi-to kommentariy, kotoriy vozmojno budet dlinnim ili daje na angliiskom, '
                           'а может и не только на английском')
    # save client
    save_clien_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/button[2]')))
    save_clien_button.click()

    sleep(2)
    driver.quit()


def main():
    url = 'https://beautybox.ru/beauty-site'
    try:
        create_client(url)
        print('Test "authorization" completed')

    except:
        print('Test "AUTHORIZATION" FILED')


if __name__ == '__main__':
    main()