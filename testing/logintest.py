from selenium import webdriver
from getpass import getpass
from webdriver_manager.chrome import ChromeDriverManager
#usr = input("ID: ")
#pwd = getpass("Pass: ")
usr = 'doctor00'
pwd= 'zaqwsxcde741852'
#pwd = getpass("Pass: ")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://127.0.0.1:8000/login/')

username_box = driver.find_element_by_id('id_username')
username_box.send_keys(usr)
pwd_box = driver.find_element_by_id('id_password')
pwd_box.send_keys(pwd)
# elem = driver.find_element_by_xpath("//input[@class='btn btn-outline-info'][@type='submit']")
# elem.click()
login_btn = driver.find_element_by_id('login')
login_btn.click()
