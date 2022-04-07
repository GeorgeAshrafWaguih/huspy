from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/georgeashraf/bin/chromedriver")
driver.get('https://the-internet.herokuapp.com/login')


login_username = driver.find_element(By.ID, value='username')
login_username.send_keys("tomsmith")
login_password = driver.find_element(By.ID, value='password')
login_password.send_keys("SuperSecretPassword!")
submit_button = driver.find_element(By.CLASS_NAME, value='radius')
submit_button.click()

#driver.implicitly_wait(5)
#sleep(2)

if driver.current_url == "https://the-internet.herokuapp.com/secure":
    print("login passed")

driver.quit()


#assert login_alert.text=="You logged into a secure area!"
#assert login_alert.text == '''
#            You logged into a secure area!
#            '''

