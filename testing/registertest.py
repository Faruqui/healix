from selenium import webdriver
from getpass import getpass
from webdriver_manager.chrome import ChromeDriverManager
#usr = input("ID: ")
#pwd = getpass("Pass: ")
usr = 'doctor002'
email = 'doctor002@healix.com'
pwd= 'zaqwsxcdet741852'
#pwd = getpass("Pass: ")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://127.0.0.1:8000/register/')

username_box = driver.find_element_by_id('id_username')
username_box.send_keys(usr)

email_box = driver.find_element_by_id('id_email')
email_box.send_keys(email)

type_account = driver.find_element_by_id('id_is_doctor')
type_account.click()

pwd_box = driver.find_element_by_id('id_password1')
pwd_box.send_keys(pwd)

repwd_box = driver.find_element_by_id('id_password2')
repwd_box.send_keys(pwd)

signup_btn = driver.find_element_by_id('signup')
signup_btn.click()
