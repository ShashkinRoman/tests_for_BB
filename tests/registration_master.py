from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0


# Создаем подключение, получаем страницу по урлу
def registration(url):
    path = 'C:/Users/Обучение/Google Диск/Обучение python/2gisparser/chromedriver_32/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path)
    driver.get(url)
    # закрываем пуш
    sleep(1)
    # кнопка получтьб бесплатно
    take_button = driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/section[1]/div/div/div/a')
    take_button.click()
    sleep(1)
    # ввод логина и пароля
    login = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'js-main-input-phone')))
    login.send_keys('1117777777')
    password = driver.find_element_by_id('js-main-input-password')
    password.send_keys('123456')
    sleep(1)
    # нажимаем получить бесплатно
    button_take_free = driver.find_element_by_id('js-login-account')
    button_take_free.click()
    sleep(2)
    # Находим и выбираем роль мастера, кликаем "далее"
    select_role_master = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/main/div/div/div[2]/div/label[1]')))
    select_role_master.click()
    select_button_next = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/main/div/div/div[1]/a')))
    select_button_next.click()
    sleep(3)
    # step-one Находим поле имени и телефона, вводим данные, нажимаем далее
    find_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/main/div/div/div[2]/div/div[1]/input')))
    find_name.click()
    find_name.send_key('automatic test account')
    find_phone = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/main/div/div/div[2]/div/div[2]/input')))
    find_phone.click()
    find_phone.send_keys('1117777777')
    sleep(0.5)
    select_button_next2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div/div/div[1]/a')))
    select_button_next2.click()
    # Выбираем оба мессенджера, и нажимаем "Далее"
    select_whatsapp = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/main/div/div/div[2]/div/div[1]/div[1]/label/span[1]')))
    select_whatsapp.click()
    select_viber = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/main/div/div/div[2]/div/div[2]/div[1]/label/span[1]')))
    select_viber.click()
    select_button_next3 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/main/div/div/div[1]/p')))
    select_button_next3.click()
    # step-three Выбираем категории все категории, потом оставляем только маникюр и нажимаем далее
    select_man = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/main/div/div/div[2]/div/label[1]/span[1]')))
    select_man.click()
    select_ped = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/main/div/div/div[2]/div/label[2]/span[1]')))
    select_ped.click()
    select_dis_nails = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/main/div/div/div[2]/div/label[3]/span[1]')))
    select_dis_nails.click()
    select_nar_nails = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/main/div/div/div[2]/div/label[4]/span[1]')))
    select_nar_nails.click()
    select_make = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/main/div/div/div[2]/div/label[5]/span[1]')))
    select_make.click()
    select_brow = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/main/div/div/div[2]/div/label[6]/span[1]')))
    select_brow.click()
    select_lash = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/main/div/div/div[2]/div/label[7]/span[1]')))
    select_lash.click()
    select_hair = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/main/div/div/div[2]/div/label[8]/span[1]')))
    select_hair.click()
    select_epil = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/main/div/div/div[2]/div/label[9]/span[1]')))
    select_epil.click()
    select_kosm = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/main/div/div/div[2]/div/label[10]/span[1]')))
    select_kosm.click()
    select_pirs = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/main/div/div/div[2]/div/label[11]/span[1]')))
    select_pirs.click()
    select_tatu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/main/div/div/div[2]/div/label[12]/span[1]')))
    select_tatu.click()
    select_fitnes = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/main/div/div/div[2]/div/label[13]/span[1]')))
    select_fitnes.click()
    select_massaj = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/main/div/div/div[2]/div/label[14]/span[1]')))
    select_massaj.click()
    select_barber = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/main/div/div/div[2]/div/label[15]/span[1]')))
    select_barber.click()
    select_barber.click()
    select_massaj.click()
    select_fitnes.click()
    select_tatu.click()
    select_pirs.click()
    select_kosm.click()
    select_epil.click()
    select_hair.click()
    select_lash.click()
    select_brow.click()
    select_make.click()
    select_nar_nails.click()
    select_dis_nails.click()
    select_ped.click()
    select_button_next4 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/main/div/div/div[1]/a[2]')))
    select_button_next4.click()
    close_triumf = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'close')))
    close_triumf.click()


    driver.quit()


def main():
    url = 'https://beautybox.ru/beauty-site'
    try:
        registration(url)
        print('--------------------------------------------------------------------')
        print('Test "registration" completed')
        print('--------------------------------------------------------------------')
    except:
        print('Test "REGISTRATION" FILED')




if __name__ == '__main__':
    main()