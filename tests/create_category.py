from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from random import randint
from config import configuration
from config.decorators import try_execute

func = configuration.Func()


@try_execute
def create_category():
    func.authorization()
    func.driver.set_window_size(1050, 1024)
    sleep(1)
    # переходим в раздел услуги
    find_button_service = func.w_xpath('/html/body/div[1]/div/nav/ul/li[7]')
    find_button_service.click()
    sleep(1)
    find_button_add_service = func.w_xpath('/html/body/div[1]/div/main/div[2]/div[2]/div/div[1]/div[2]/div')
    find_button_add_service.click()
    # find and click add category
    add_category = func.w_xpath('/html/body/div[1]/div/main/div[2]/div[2]/div/div[1]/div[2]/div/div/ul/li[2]')
    add_category.click()
    sleep(2)
    # add yourself category
    add_yourself_category = func.w_xpath('/html/body/div[2]/div/div[2]/div/div[1]/div')
    add_yourself_category.click()
    sleep(1)
    # title category and save
    find_title = func.w_xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/input[1]')
    find_title.send_keys('test category ' + str(randint(1000000, 9999999)))
    sleep(1)
    save_category = func.w_xpath('/html/body/div[2]/div[2]/div[3]/button')
    save_category.click()
    sleep(2)
    # delete yorself category
    find_cross = func.w_xpath('/html/body/div[2]/div/div[1]/button[2]')
    find_cross.click()
    find_menu = WebDriverWait(func.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME,
                                        'item-services__controls')))
    find_menu.click()
    sleep(2)
    delete_category = WebDriverWait(func.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME,
                                            'jsCrmCategoriesDeleteItemLink')))
    delete_category.click()
    sleep(2)
    accept_delete = func.w_xpath('//*[@id="delete"]/div/div/div[2]/button[1]')
    accept_delete.click()

    remove_at_home = func.w_xpath('/html/body/div[1]/div/nav/ul/li[1]/a')
    remove_at_home.click()


def main():
    create_category()
    func.driver.quit()


if __name__ == '__main__':
    main()
