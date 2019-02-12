'''
Created on Feb 11, 2019

@author: sehhar
'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common import keys



driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://dev.workmarket.com/register/campaign/10081C503B209A0C8E7F05FDCC1AA98D4C904DEEF5F73265CAE38C744E7EAD3E")

driver.implicitly_wait(7)

#join as an individual


driver.find_element_by_xpath("//span[contains(text(),'Join as an individual')]").click()

driver.implicitly_wait(7)


#Sign up first name

driver.find_element_by_xpath("//input[@id='firstname']").click()
driver.find_element_by_xpath("//input[@id='firstname']").send_keys("Mohammed")


#Sign up last name

driver.find_element_by_xpath("//input[@id='lastname']").click()
driver.find_element_by_xpath("//input[@id='lastname']").send_keys("Sehhar")


#Sign up Email

driver.find_element_by_xpath("//input[@id='email']").click()
driver.find_element_by_xpath("//input[@id='email']").send_keys("Mohammed.Sehhar@gmail.com")


#Sign up Password

driver.find_element_by_xpath("//input[@id='password']").click()
driver.find_element_by_xpath("//input[@id='password']").send_keys("Test-36912ABC")


#Sign up Checkbox

driver.find_element_by_xpath("//input[@value='on']").click()


#Sign up Register

driver.find_element_by_xpath("//span[contains(text(),'Register')]").click()


driver.implicitly_wait(15)

driver.get("https://dev.workmarket.com/login")

driver.implicitly_wait(7)


#Sign in (Email)

driver.find_element_by_xpath("//input[@name='userEmail']").click()
driver.find_element_by_xpath("//input[@name='userEmail']").send_keys("qa+candidatetest@workmarket.com")

#Sign in (Password)

driver.find_element_by_xpath("//input[@id='login-password']").click()
driver.find_element_by_xpath("//input[@id='login-password']").send_keys("candidate123")


#Sign in (Login button)

driver.find_element_by_xpath("//span[@class='jss405']").click()


#Search (Find talent)

driver.find_element_by_xpath("//a[@role='menuitem']//div//div//div[contains(text(),'Find Talent')]").click()

driver.implicitly_wait(7)


#Search field

#driver.find_element_by_xpath("//input[@id='input-text']").click()
#driver.find_element_by_xpath("//input[@id='input-text']").send_keys("test")
#driver.find_element_by_xpath("//input[@id='input-text']").send_keys(keys.RETURN)

driver.find_element_by_id("input-text").send_keys("test")

driver.find_element_by_id("input-text").send_keys(u'\ue007')


#Search verification
driver.find_element_by_xpath("//div[@id='search_results']", 'test')







