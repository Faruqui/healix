from selenium import webdriver
from getpass import getpass
from webdriver_manager.chrome import ChromeDriverManager

usr = 'doctor00'
pwd= 'zaqwsxcde741852'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://127.0.0.1:8000/login/')

username_box = driver.find_element_by_id('id_username')
username_box.send_keys(usr)
pwd_box = driver.find_element_by_id('id_password')
pwd_box.send_keys(pwd)
login_btn=driver.find_element_by_id('login')
login_btn.click()
driver.get('http://127.0.0.1:8000/post/new/')
title = "I am selenium , for testing"
blog = "test test test,wowooowowoowdsks wowow"

title_box = driver.find_element_by_id('id_title')
title_box.send_keys(title)
blog_box = driver.find_element_by_id('id_content')
blog_box.send_keys(blog)
post_btn=driver.find_element_by_id('post')
post_btn.click()
