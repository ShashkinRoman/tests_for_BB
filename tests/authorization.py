from config import configuration
from config.decorators import try_execute

@try_execute
def authorization():
    for i in range(1, 4):
        while True:
            try:
                func = configuration.Func()
                func.authorization()
                # нажимаем на раздел инстаграм, чтобы проверить, что страница кабинета прогрузилась
                instagram = func.w_xpath('/html/body/div[1]/div/nav/ul/li[8]')
                instagram.click()
                func.driver.quit()
                print('Test "authorization" number ' + str(i) + ' completed')
            except:
                print('Test "AUTHORIZATION " number ' + str(i) + ' FILED')
                func.driver.quit()
            break


def main():
    authorization()


if __name__ == '__main__':
    main()
