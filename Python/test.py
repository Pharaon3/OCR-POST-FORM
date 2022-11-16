# import sys
from selenium import webdriver
chromedriver_location = "/Users/Downloads/chromedrive"
driver = webdriver.Chrome(chromedriver_location)
driver.get('https://www.telkomsel.com/shops/preorder-wna/form?utm_source=wec&utm_medium=web&utm_campaign=prabayar-tourist')

continueButton = '//*[@id="mat-dialog-0"]/app-wnaregistration-popup/div/div/div[4]/div/button'
fullNamePath = '/html/body/app-root/div/app-wna-registration/div/div[2]/div/form/div[1]/shared-basic-input/div/div[2]/input'
passportPath = '/html/body/app-root/div/app-wna-registration/div/div[2]/div/form/div[2]/shared-basic-input/div/div[2]/input'
htmlBodyPath = '/html/body/app-root/div/app-wna-registration/div'
bodyPath = '/html/body/app-root/div/app-wna-registration/div/div[2]'
passportFrontPagePath = '/html/body/app-root/div/app-wna-registration/div/div[2]/div/form/div[3]/div[1]/shared-file-input/div[3]'
passportFrontPageContinueButtonPath = '/html/body/div[2]/div[2]/div/mat-dialog-container/shared-popup-info/div/div/div[3]/div/button'
# passportFrontPageContinueButtonPath = '/html/body/div[2]/div[2]/div/mat-dialog-container/shared-popup-info/div/div/div[3]/div/button'
passportFrontPageChooseButtonPath = '/html/body/app-root/div/app-wna-registration/div/div[2]/div/form/div[3]/div[1]/shared-file-input/div[2]/input[2]'


# fullNameValue = sys.argv[1]
# passportValue = sys.argv[2]
fullNameValue = 'abc'
passportValue = 'abcd123486'

driver.find_element("xpath", continueButton).click()
driver.find_element("xpath", fullNamePath).send_keys(fullNameValue)
driver.find_element("xpath", passportPath).send_keys(passportValue)
driver.find_element("xpath", bodyPath).click()
driver.find_element("xpath", passportFrontPagePath).click()
driver.find_element("xpath", passportFrontPageContinueButtonPath).click()
driver.find_element(
    "xpath", passportFrontPageChooseButtonPath).send_keys("C:\Users\Pharaon\Pictures\avatar\106703.jpg")


# driver.find_element("xpath", htmlBodyPath).click()
# altString1 = driver.find_element("xpath", passportStringPath).get_attribute("alt")
# print(fullNameValue)
# print(altString2)
# print(altString1)
