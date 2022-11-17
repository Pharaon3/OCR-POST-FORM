# import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
from selenium.webdriver.common.action_chains import ActionChains
chromedriver_location = "/Users/Downloads/chromedrive"
driver = webdriver.Chrome(chromedriver_location)
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
emailPath = '/html/body/app-root/div/app-wna-registration/div/div[2]/div/form/div[3]/div[4]/shared-basic-input/div/div[2]/input'
dateOfBirthPath = '/html/body/app-root/div/app-wna-registration/div/div[2]/div/form/div[3]/div[3]/shared-date-picker/div[2]/input'
EMEI1Path = '/html/body/app-root/div/app-wna-registration/div/div[2]/div/form/div[3]/div[6]/shared-number-input/div/div[2]/input'
EMEI2Path = '/html/body/app-root/div/app-wna-registration/div/div[2]/div/form/div[3]/div[7]/shared-number-input/div/div[2]/input'
capturedIMEIChooseButtonPath = '/html/body/app-root/div/app-wna-registration/div/div[2]/div/form/div[3]/div[5]/shared-file-input/div[2]/input[2]'
dateOfBirthDivPath = '/html/body/app-root/div/app-wna-registration/div/div[2]/div/form/div[3]/div[3]/shared-date-picker/div[2]'
datePickerPath = '//*[@id="mat-datepicker-0"]/div/mat-month-view/table/tbody/tr/td'

# fullNameValue = sys.argv[1]
# passportValue = sys.argv[2]
fullNameValue = 'abc'
passportValue = 'abcd123486'
nationalityValue = 'Afghanistan'
emailValue = 'email@mail.com'
EMEI1Value = '1230987654321'
EMEI2Value = '1230987654321'

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
driver.find_element("xpath", nationalityPath).send_keys(nationalityValue)
actions.send_keys(Keys.ENTER)
actions.perform()
driver.find_element("xpath", capturedIMEIChooseButtonPath).send_keys("C:/Users/Pharaon/Pictures/passport/EMEI1.jpg")
driver.find_element("xpath", dateOfBirthDivPath).click()
m = driver.find_element("xpath", datePickerPath)
for i in m:
#verify required date then click
   if i.text == '3':
      i.click()
   break
# driver.find_element("xpath", dateOfBirthPath).send_keys('01012011')
# driver.find_element("xpath", passportFrontPagePath).click()
# driver.find_element("xpath", passportFrontPageContinueButtonPath).click()
time.sleep(20)

# driver.find_element("xpath", htmlBodyPath).click()
# altString1 = driver.find_element("xpath", passportStringPath).get_attribute("alt")
# print(fullNameValue)
# print(altString2)
# print(altString1)
