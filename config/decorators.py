from config import configuration
import traceback
# import logging


func = configuration.Func()


def try_execute(fn):

    def dec():
        for i in range(1, 4):
            while True:
                try:
                    fn()
                    print('Test ' + fn.__name__ + ' number ' + str(i) + ' completed')
                    func.driver.quit()
                except Exception as e:
                    print('Test ' + fn.__name__ + ' number ' + str(i) + ' FILED')
                    print('Ошибка:\n', traceback.format_exc())
                    func.driver.quit()
                    # logging.error(e)
                break
    return dec
