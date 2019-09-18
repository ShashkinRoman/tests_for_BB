from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from config.decorators import try_execute
from config import configuration

func = configuration.Func()


@try_execute
def create_client():
    func.authorization()
    func.driver.set_window_size(1050, 1024)

    # нажимаем на раздел клиенты, чтобы проверить, что страница кабинета прогрузилась
    find_client = func.w_xpath('/html/body/div[1]/div/nav/ul/li[6]')
    find_client.click()
    # Находим и нажимаем кнопку добавить клиента
    find_button_add_client = func.w_xpath('/html/body/div[1]/div/main/div[2]/div/div[1]/div[2]')
    find_button_add_client.click()
    sleep(2)
    # Заполнием инфу о клиенте
    find_name_input = func.w_xpath('//*[@id="aplication-info"]/div[2]/div[2]/div[1]/input')
    find_name_input.click()
    find_name_input.send_keys('Test client') #вводим текст в поле "Имя и фамилия"
    # Ищем меню роли клиента
    find_role_client = func.w_xpath('//*[@id="aplication-info"]/div[2]/div[2]/div[2]/span[2]/span[1]/span')
    find_role_client.click()
    sleep(0.5)
    # Выбираем статус VIP
    ActionChains(func.driver).move_to_element(find_role_client).move_by_offset(1, 100).click().perform()
    # Ищем поле номерa, e-mail, скидку, комментарий, пол, дату и вводим
    find_phone_number = func.w_xpath('//*[@id="aplication-info"]/div[2]/div[3]/div[1]/input')
    find_phone_number.send_keys(randint(1111111111, 9999999999))

    find_email_number = func.w_xpath('//*[@id="aplication-info"]/div[2]/div[3]/div[2]/input')
    find_email_number.send_keys('test@mail.ru')
    sleep(1)
    # day
    find_date_of_birth_day = func.w_xpath('//*[@id="aplication-info"]/div[2]/div[4]/div/div/div/div[1]/span/span[1]/span')
    find_date_of_birth_day.click()
    sleep(0.5)
    # Перемещаем мышь относительно выбранного элемента на 100 пикселей вниз and click
    ActionChains(func.driver).move_to_element(find_date_of_birth_day).move_by_offset(1, 100).click().perform()
    # month
    find_date_of_birth_month = func.w_xpath('//*[@id="aplication-info"]/div[2]/div[4]/div/div/div/div[2]/span')
    find_date_of_birth_month.click()
    # Перемещаем мышь относительно выбранного элемента на 100 пикселей вниз and click
    ActionChains(func.driver).move_to_element(find_date_of_birth_month).move_by_offset(1, 100).click().perform()
    # year
    find_date_of_birth_year = func.w_xpath('//*[@id="aplication-info"]/div[2]/div[4]/div/div/div/a')
    find_date_of_birth_year.click()
    find_date_of_birth_year2 = func.w_xpath('//*[@id="aplication-info"]/div[2]/div[4]/div/div/div/div[3]/span')
    find_date_of_birth_year2.click()
    ActionChains(func.driver).move_to_element(find_date_of_birth_year2).move_by_offset(1, 100).click().perform()
    # gender
    find_gender = func.w_xpath('//*[@id="aplication-info"]/div[2]/div[5]/div[1]/span[2]')
    find_gender.click()
    ActionChains(func.driver).move_to_element(find_gender).move_by_offset(1, 100).click().perform()
    # sale
    find_sale = func.w_xpath('//*[@id="aplication-info"]/div[2]/div[5]/div[2]/input')
    find_sale.click()
    find_sale.send_keys('50')
    # comment
    find_comment = func.w_xpath('//*[@id="aplication-info"]/div[2]/div[6]/div/div/textarea')
    find_comment.click()
    find_comment.send_keys('kakioi-to kommentariy, kotoriy vozmojno budet dlinnim ili daje na angliiskom, '
                           'а может и не только на английском')
    # save client
    save_client_button = func.w_xpath('/html/body/div[2]/div/div/div[3]/div/div/button[2]')
    save_client_button.click()
    # delete new client
    sleep(1)
    find_new_client = func.w_xpath('/html/body/div[1]/div[1]/main/div[2]/div/div[2]/div[1]/div[2]')
    find_new_client.click()
    sleep(1)
    delete_new_client = func.w_xpath('/html/body/div[2]/div/div/div[3]/div/div/button[1]')
    delete_new_client.click()
    sleep(1)
    accept_delete_new_client = func.w_xpath('//*[@id="delete"]/div/div/div[2]/button[1]')
    accept_delete_new_client.click()


def main():
    create_client()
    func.driver.quit()


if __name__ == '__main__':
    main()
