from time import sleep
from random import randint
from config import configuration
from config.decorators import try_execute

func = configuration.Func()

@try_execute
def create_service():
    func.authorization()
    func.driver.set_window_size(1050, 1024)
    sleep(1)
    # переходим в раздел услуги
    find_button_service = func.w_xpath('/html/body/div[1]/div/nav/ul/li[7]')
    find_button_service.click()
    sleep(1)
    # find and click on button "add service"
    find_button_add_service = func.w_xpath('/html/body/div[1]/div/main/div[2]/div[2]/div/div[1]/div[2]/div')
    find_button_add_service.click()
    find_add_service = func.w_xpath('/html/body/div[1]/div/main/div[2]/div[2]/div/div[1]/div[2]/div/div/ul/li[1]')
    find_add_service.click()
    sleep(1)
    # add service in first category
    find_brow_category = func.w_xpath('//html/body/div[2]/div[1]/div[2]/div/ul/li[1]')
    find_brow_category.click()
    sleep(1)
    add_yourself_service = func.w_xpath('/html/body/div[2]/div[1]/div[2]/div/div[2]/div/div')
    add_yourself_service.click()
    sleep(1)
    # description yourself service
    find_title_service = func.w_xpath('/html/body/div[2]/div[2]/div[1]/div[1]/input')
    find_title_service.send_keys('test service' + str(randint(1000000, 99999999)))
    find_price = func.w_xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/input')
    find_price.send_keys('1500')
    click_save = func.w_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/button[2]')
    click_save.click()

    sleep(2)
    # delete new servise
    delete_new_servise = func.w_xpath('//*[@id="65938"]/ul')
    delete_new_servise.click()
    sleep(1)
    button_delete_servise = func.w_xpath('/html/body/div[2]/div[4]/div/div[3]/div/div/button[1]')
    button_delete_servise.click()
    sleep(1)
    accept_button_delete_servise = func.w_xpath('//*[@id="delete"]/div/div/div[2]/button[1]')
    accept_button_delete_servise.click()
    sleep(1)
    exit_delete_servise = func.w_xpath('/html/body/div[2]/div[4]/div/div[1]/button')
    exit_delete_servise.click()

    sleep(1)
    remove_at_home = func.w_xpath('/html/body/div[1]/div/nav/ul/li[1]/a')
    remove_at_home.click()


def main():
    create_service()
    func.driver.quit()

if __name__ == '__main__':
    main()
