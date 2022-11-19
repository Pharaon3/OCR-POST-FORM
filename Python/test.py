# import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

import time 
from selenium.webdriver.common.action_chains import ActionChains
# chromedriver_location = r"D:/Projects/Project 22-11-15(Passport reader and imei phone ocr to form post or submit)/OCR-POST-FORM/chromedrive/chromedriver.exe"
# driver = webdriver.Chrome(chromedriver_location)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



driver.get('https://www.telkomsel.com/shops/preorder-wna/form?utm_source=wec&utm_medium=web&utm_campaign=prabayar-tourist')

continueButton = '//*[@id="mat-dialog-0"]/app-wnaregistration-popup/div/div/div[4]/div/button'
fullNamePath = '/html/body/app-root/div/app-wna-registration/div/div[2]/div/form/div[1]/shared-basic-input/div/div[2]/input'
passportPath = '/html/body/app-root/div/app-wna-registration/div/div[2]/div/form/div[2]/shared-basic-input/div/div[2]/input'
htmlBodyPath = '/html/body/app-root/div/app-wna-registration/div'
bodyPath = '/html/body/app-root/div/app-wna-registration/div/div[1]'
passportFrontPagePath = '/html/body/app-root/div/app-wna-registration/div/div[2]/div/form/div[3]/div[1]/shared-file-input/div[3]'
passportFrontPageContinueButtonPath = '/html/body/div[2]/div[2]/div/mat-dialog-container/shared-popup-info/div/div/div[3]/div/button'
# passportFrontPageContinueButtonPath = '/html/body/div[2]/div[2]/div/mat-dialog-container/shared-popup-info/div/div/div[3]/div/button'
passportFrontPageChooseButtonPath = '/html/body/app-root/div/app-wna-registration/div/div[2]/div/form/div[3]/div[1]/shared-file-input/div[2]/input[2]'
nationalityPath = '/html/body/app-root/div/app-wna-registration/div/div[2]/div/form/div[3]/div[2]/div[2]/shared-dropdown/div/div[1]/div[1]/input'
nationalityDropdownPath = '/html/body/app-root/div/app-wna-registration/div/div[2]/div/form/div[3]/div[2]/div[2]/shared-dropdown/div/div[1]/div[2]'
nationalityAfganPath = '/html/body/app-root/div/app-wna-registration/div/div[2]/div/form/div[3]/div[2]/div[2]/shared-dropdown/div/div[2]/ul/li[1]'
emailPath = '/html/body/app-root/div/app-wna-registration/div/div[2]/div/form/div[3]/div[4]/shared-basic-input/div/div[2]/input'
dateOfBirthPath = '/html/body/app-root/div/app-wna-registration/div/div[2]/div/form/div[3]/div[3]/shared-date-picker/div[2]/input'
EMEI1Path = '/html/body/app-root/div/app-wna-registration/div/div[2]/div/form/div[3]/div[6]/shared-number-input/div/div[2]/input'
EMEI2Path = '/html/body/app-root/div/app-wna-registration/div/div[2]/div/form/div[3]/div[7]/shared-number-input/div/div[2]/input'
capturedIMEIChooseButtonPath = '/html/body/app-root/div/app-wna-registration/div/div[2]/div/form/div[3]/div[5]/shared-file-input/div[2]/input[2]'
dateOfBirthDivPath = '/html/body/app-root/div/app-wna-registration/div/div[2]/div/form/div[3]/div[3]/shared-date-picker/div[2]'
datePickerPath = '//*[@id="mat-datepicker-0"]/div/mat-month-view/table/tbody/tr/td'
datePickerClass = 'mat-calendar-body-cell-content mat-focus-indicator'
datePickerDivPath = '//*[@id="mat-datepicker-0"]/div/mat-month-view/table/tbody/tr[3]/td[6]/div[1]'
datePickerChoosePath = '/html/body/div[2]/div[2]/div/mat-datepicker-content/div[2]/div/button[2]'
submitPath = '/html/body/app-root/div/app-wna-registration/div/div[2]/div/form/div[4]/button'
payNowButtonPath = '/html/body/app-root/div/app-summary/div/div[2]/div[2]/button'
orderIdPath = '/html/body/app-root/div/app-card-invoice/div/shared-invoice/div/div[4]/div[1]/div[2]'

# fullNameValue = sys.argv[1]
# passportValue = sys.argv[2]
fullNameValue = 'anbc'
passportValue = 'abcd123486'
nationalityValue = 'Afghanistan'
emailValue = 'email@mail.com'
EMEI1Value = '123098765432115'
EMEI2Value = '123098765432215'

driver.find_element("xpath", continueButton).click()
driver.find_element("xpath", fullNamePath).send_keys(fullNameValue)
driver.find_element("xpath", passportPath).send_keys(passportValue)
# driver.find_element("xpath", bodyPath).click()
actions = ActionChains(driver) 
actions.send_keys(Keys.TAB)
actions.perform()
time.sleep(5)
driver.find_element("xpath", passportFrontPageChooseButtonPath).send_keys("C:/Users/Pharaon/Pictures/passport/passport (1).png")
driver.find_element("xpath", emailPath).send_keys(emailValue)
driver.find_element("xpath", EMEI1Path).send_keys(EMEI1Value)
driver.find_element("xpath", EMEI2Path).send_keys(EMEI2Value)
driver.find_element("xpath", nationalityPath).click()
# driver.find_element("xpath", nationalityPath).send_keys(nationalityValue)
# driver.find_element("xpath", nationalityDropdownPath).click()
driver.find_element("xpath", nationalityAfganPath).click()
actions.send_keys(Keys.ENTER)
actions.perform()
driver.find_element("xpath", capturedIMEIChooseButtonPath).send_keys("C:/Users/Pharaon/Pictures/passport/EMEI1.jpg")
driver.find_element("xpath", dateOfBirthDivPath).click()
driver.find_element("xpath", datePickerDivPath).click()
driver.find_element("xpath", datePickerChoosePath).click()
driver.find_element("xpath", submitPath).click()
time.sleep(10)
driver.find_element("xpath", payNowButtonPath).click()
time.sleep(10)
orderId = driver.find_element("xpath", orderIdPath).text
print(orderId)
# m = driver.find_element("xpath", datePickerPath)
# m = driver.find_element("class name", datePickerClass)
# print(m);
# for i in m:
# #verify required date then click
#    if i.text == '3':
#       i.click()
#    break
# driver.find_element("xpath", dateOfBirthPath).send_keys('01012011')
# driver.find_element("xpath", passportFrontPagePath).click()
# driver.find_element("xpath", passportFrontPageContinueButtonPath).click()
time.sleep(20)

# driver.find_element("xpath", htmlBodyPath).click()
# altString1 = driver.find_element("xpath", passportStringPath).get_attribute("alt")
# print(fullNameValue)
# print(altString2)
# print(altString1)
