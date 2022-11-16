from selenium import webdriver
chromedriver_location = "/Users/Downloads/chromedrive"
driver = webdriver.Chrome(chromedriver_location)
driver.get('file:///D:/Projects/Project%2022-11-15(Passport%20reader%20and%20imei%20phone%20ocr%20to%20form%20post%20or%20submit)/HTML/Report1.html')
continueButton = '/html/body/div/form/div[11]/input'
fullName = '//*[@id="fullName"]/input'
passport = '//*[@id="passportNumber"]/input'
driver.find_element("xpath", fullName).send_keys("abc")
driver.find_element("xpath", passport).send_keys("abc1230985")
driver.find_element("xpath", continueButton).click()
