import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class Config(object):
    url = os.environ.get('url')
    url_mod = os.environ.get('url_mode')
    login = os.environ.get('login')
    password = os.environ.get('password')
    webdr = os.environ.get('webdr')

class Func(Config):
    def __init__(self):
        config = Config()
        options = Options()
        options.add_argument('--headless')
        # Создаем подключение
        self.driver = webdriver.Chrome(executable_path=config.webdr, chrome_options=options)

    def w_xpath(self, *args):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, *args)))

    def w_id(self, *args):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, *args)))

    def authorization(self):
        config = Config()
        url = config.url + config.url_mod
        self.driver.get(url)
        sleep(2)
        take_button = self.w_xpath('/html/body/div[1]/div[2]/main/section[1]/div/div/div/a')
        take_button.click()
        sleep(1)
        # ввод логина и пароля
        login = self.w_id('js-main-input-phone')
        login.send_keys(config.login)
        password = self.w_id('js-main-input-password')
        password.send_keys(config.password)
        sleep(1)
        # нажимаем получить бесплатно
        button_take_free = self.w_id('js-login-account')
        button_take_free.click()