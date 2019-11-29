from selenium import webdriver #Import webdriver from selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome('C:/Users/Ecarvallo/.wdm/drivers/chromedriver/78.0.3904.105/win32/chromedriver.exe') #Inicializate webdriver
driver.get('https://www.starken.cl/SEGUIMIENTO') #Get and open url
codeField= driver.find_element_by_xpath('//*[@id="edit-codigo"]') #create codeField and find element by xpath
# code=input() Manual code input
codeField.send_keys('923090162') #Send code to codeField
sendCodeButton= driver.find_element_by_xpath('//*[@id="edit-submit"]') #Create CodeButton and find button by xpath
sendCodeButton.click()


wait= WebDriverWait(driver, 10)
close= wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/section/div[2]/section/div[3]/div/div/div/div[2]/div[4]/button')))
typeEntr= driver.find_element_by_xpath('/html/body/div[2]/div/section/div[2]/section/div[3]/div/div/div/div[2]/div[3]/div[3]/p').text
origen=driver.find_element_by_xpath('/html/body/div[2]/div/section/div[2]/section/div[3]/div/div/div/div[2]/div[1]/div[2]/div/div[1]').text
destino= driver.find_element_by_xpath('/html/body/div[2]/div/section/div[2]/section/div[3]/div/div/div/div[2]/div[1]/div[2]/div/div[2]').text
print(typeEntr)
print(origen)
print(destino)

driver.quit() #close window
