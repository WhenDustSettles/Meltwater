from selenium import webdriver
driver = webdriver.Chrome('chromedriver')
driver.get('https://www.linkedin.com')

Signin_button = driver.find_element_by_class_name('nav__button-secondary')
Signin_button.click()
Email = driver.find_element_by_id('username')
Password = driver.find_element_by_id('password')
Email.send_keys('animesh.r18a@gmail.com')
Password.send_keys('animeshsingh.123')
LogIn = driver.find_element_by_xpath('//*[@type = "submit"]')
LogIn.click()