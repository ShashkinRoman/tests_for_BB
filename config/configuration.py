import os
import environ
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False))

environ.Env.read_env()


class Config(object):
    def __init__(self):
        self.url = environ.Env('URL')
        self.url_mod = environ.Env('URL_MODE')
        self.login = environ.Env('LOGIN')
        self.password = environ.Env('PASSWORD')
        self.webdr = environ.Env('PATH')


class Func(Config):
    def __init__(self):
        config = Config()
        # self.webdr = 'D:\Python project\Beautybox_tests\chromedriver\chromedriver'
        # Создаем подключение
        self.driver = webdriver.Chrome(executable_path=config.webdr)

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


