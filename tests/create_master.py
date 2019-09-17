from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from config import configuration
from time import sleep
from config.decorators import try_execute


# Создаем подключение, получаем страницу по урлу
@try_execute
def create_master():
    func = configuration.Func()
    func.authorization()
    func.driver.set_window_size(1050, 1024)
    sleep(1)
    find_button_service = func.w_xpath('/html/body/div[1]/div/nav/ul/li[7]')
    find_button_service.click()
    sleep(1)
    find_employees = func.w_xpath('/html/body/div[1]/div/div/header/nav/ul/li[2]')
    find_employees.click()
    sleep(1)
    # find and click button "added employees
    find_button_add_employeed = func.w_xpath('/html/body/div[1]/div/main/div[2]/div/div[1]/div[2]/button')
    find_button_add_employeed.click()
    sleep(1)
    # complete info about employees and save
    find_title = func.w_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div/div[3]/div[1]/input')
    find_title.send_keys('test employees')

    find_phone = func.w_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div/div[3]/div[2]/input')
    find_phone.send_keys(randint(70000000000, 99999999999))

    find_email = func.w_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div/div[4]/div[1]/input')
    find_email.send_keys(str(randint(70000000000, 99999999999)) + "@gmail.com")

    find_checkbox = func.w_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div/label/span[1]')
    find_checkbox.click()

    find_input_category = func.w_xpath('//*[@id="aplication-services"]/div[2]/div[2]/span')
    find_input_category.click()

    # передвигает мышь передвигается от центра элемента вниз к первой услуге
    ActionChains(func.driver).move_to_element(find_input_category).move_by_offset(1, 100).click().perform()

    find_checkbox = func.w_xpath('/html/body/div[2]/div/div/div[3]/div/div/button[2]')
    find_checkbox.click()
    sleep(2)
    # delete new employees
    find_new_employees = WebDriverWait(func.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME,
                                        'jsCrmEmployeesAssociateItem ')))
    find_new_employees.click()
    sleep(2)
    find_button_delete = func.w_xpath('/html/body/div[2]/div/div/div[3]/div/div/button[1]')
    ActionChains(func.driver).move_to_element(find_button_delete).move_by_offset(-70, 0).click().perform()

    sleep(1)
    find_button_delete2 = func.w_xpath('//*[@id="delete"]/div/div/div[2]/button[1]')
    find_button_delete2.click()


def main():
    create_master()


if __name__ == '__main__':
    main()
