from config import configuration


def authorization():
    func = configuration.Func()
    func.authorization()
    # нажимаем на раздел инстаграм, чтобы проверить, что страница кабинета прогрузилась
    instagram = func.w_xpath('/html/body/div[1]/div/nav/ul/li[8]')
    instagram.click()
    func.driver.quit()


def main():
    try:
        authorization()
        print('Test "authorization" completed')
    except:
        print('Test "AUTHORIZATION" FILED')


if __name__ == '__main__':
    main()
