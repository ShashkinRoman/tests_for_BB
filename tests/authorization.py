from config import configuration
from config.decorators import try_execute

func = configuration.Func()


# декоратор, который прогоняет тест трижды и если были ошибки, выводит текст
@try_execute
def authorization():

    func.authorization()
    # нажимаем на раздел инстаграм, чтобы проверить, что страница кабинета прогрузилась
    instagram = func.w_xpath('/html/body/div[1]/div/nav/ul/li[8]')
    instagram.click()

def main():
    authorization()
    func.driver.quit()

if __name__ == '__main__':
    main()
