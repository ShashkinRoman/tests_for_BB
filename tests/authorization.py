from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from config import configuration


def authorization():
    func = configuration.Func()
    func.authorization()
    # нажимаем на раздел инстаграм, чтобы проверить, что страница кабинета прогрузилась
    driver = func.driver
    instagram = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                '/html/body/div[1]/div/nav/ul/li[8]')))
    instagram.click()
    func.driver.quit()


def main():
    try:
        authorization()
        print('--------------------------------------------------------------------')
        print('Test "authorization" completed')
        print('--------------------------------------------------------------------')
    except:
        print('Test "AUTHORIZATION" FILED')


if __name__ == '__main__':
    main()
