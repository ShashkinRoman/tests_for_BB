from config.configuration import Func


func = Func


def try_execute(fn):
    def dec():
        for i in range(1, 4):
            while True:
                try:
                    fn()
                    print('Test' + fn.__name__ + 'number ' + str(i) + ' completed')
                    func.driver.quit()
                except:
                    print('Test' + fn.__name__ + 'number ' + str(i) + ' FILED')
                    func.driver.quit()
    return dec