from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import getpass


options = Options()

# broswer without GUI, for faster performance
options.add_argument('--headless')
options.add_argument('--nosandbox')

options.add_argument("--remote-debugging-port=9220")

DRIVER_PATH = 'C:/Users/lollo/Desktop/chromedriver.exe'
try:
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get('https://www.gostudent.org/login/?lng=it')

    tel = input("Inserisci il numero: ")

    key = getpass.getpass('Password: ')

    wait = WebDriverWait(driver, 20)  # wait max 20 seconds before continuing
    login = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, 'dZa-Dsc'))).click()  # wait until the element with the specified class is loaded successfully

    drop = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'down'))).click()

    italy = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '+39')]")))

    # execute a particular script beacuse there are overlapping parts in the window
    driver.execute_script("arguments[0].click();", italy)

    tel_ = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input"))).send_keys(tel)  # type the telephone number in the input field

    submit = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "login-button"))).click()

    key_ = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "digit-1"))).send_keys(key)
    # insert the personal key

    submit_final = driver.find_element_by_class_name('dZa-Dsc').click()

    menu = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "menu"))).click()

    profit = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "PROFIT"))).click()
    # check for the visibility of element by the id = 'PROFIT'

    b = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "kYQmLZ")))

    # get a list of elements with the specified class name
    balance = driver.find_elements_by_class_name('kYQmLZ')

    print('Mese corrente: {}'.format(balance[1].get_attribute('innerHTML')))
    print('Totale: {}'.format(balance[3].get_attribute('innerHTML')))
finally:
    driver.stop_client()
    driver.close()
    driver.quit()
