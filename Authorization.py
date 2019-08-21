from time import sleep
from selenium import webdriver

url = 'https://beautybox.ru/beauty-site'
# Создаем подключение, получаем страницу по урлу
path = 'C:/Users/Обучение/Google Диск/Обучение python/2gisparser/chromedriver_32/chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=path)
driver.get(url)
sleep(2)
# авторизируемся
close_push = driver.find_element_by_xpath('/html/body/div[1]')
close_push.click()
take_button = driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/section[1]/div/div/div/a')
take_button.click()
sleep(2)
login = driver.find_element_by_id('js-main-input-phone')
login.click()
login.send_keys('1113333333')
password = driver.find_element_by_id('js-main-input-password')
password.send_keys('123456')
sleep(2)
button_take_free = driver.find_element_by_id('js-login-account')
button_take_free.click()


