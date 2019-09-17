'''Скрипт: логинится со страницы https://beautybox.ru/beauty-site
нажимает на раздел "заявки", кнопку "создать заявку", нажимает на поле клиента,
выбирает первого клиента, нажимает на поле мастера, нажимает в середину выпадающего
окна выбора мастеров и сохраняет заявку на 06:00 по времени.
'''
from selenium.webdriver.common.keys import Keys
from config import configuration
from time import sleep
from config.decorators import try_execute

@try_execute
def create_app():
    func = configuration.Func()
    func.authorization()
    func.driver.set_window_size(1050, 1024)
    # нажимаем на раздел заявки
    applications = func.w_xpath('/html/body/div[1]/div/nav/ul/li[5]')
    applications.click()
    # нажимаем на кнопку добавить заявку
    add_applications = func.w_xpath('//*[@id="jsProfileID"]/div/div/div[4]/div')
    add_applications.click()
    sleep(1)
    # выбираем поле клиента
    select_master_two = func.w_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div[1]/div[1]')
    select_master_two.click()
    sleep(1)
    # выбираем первого по очереди клиента
    select_first_client = func.w_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]')
    select_first_client.click()
    sleep(1)
    # нажимаем на поле "добавить мастера", находим нажатое поле, нажимаем enter
    select_master_one = func.w_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div/span[2]')
    select_master_one.click()
    select_master_two = func.w_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div/span[3]/span/span[1]/input')
    select_master_two.send_keys('Сергей123')
    select_master_two.send_keys(Keys.ENTER)
    # сохраняем заявку
    sleep(1)
    save_application = func.w_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div[3]/div/button[2]')
    save_application.click()


def main():
    create_app()


if __name__ == '__main__':
    main()


