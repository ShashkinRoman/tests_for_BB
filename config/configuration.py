from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC

#todo загрузить webdriver для контейнера
#todo

class Config:
    def __init__(self):
        self.url = 'https://beautybox.ru/'
        self.urlmod = 'beauty-site'
        self.login = '1113333333'
        self.password = '123456'
        self.path = 'C:/Users/Обучение/Google Диск/Обучение python/2gisparser/chromedriver_32/chromedriver.exe'


class Func(Config):
    def __init__(self):
        config = Config()
        # Создаем подключение
        self.driver = webdriver.Chrome(executable_path=config.path)

    def w_xpath(self, *args):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, *args)))

    def w_id(self, *args):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, *args)))

    def authorization(self):
        config = Config()
        url = config.url + config.urlmod
        driver = self.driver
        driver.get(url)
        take_button = self.w_xpath('/html/body/div[1]/div[2]/main/section[1]/div/div/div/a')
        take_button.click()
        # ввод логина и пароля
        login = self.w_id('js-main-input-phone')
        login.send_keys(config.login)
        password = self.w_id('js-main-input-password')
        password.send_keys(config.password)
        sleep(1.5)
        # нажимаем получить бесплатно
        button_take_free = self.w_id('js-login-account')
        button_take_free.click()


