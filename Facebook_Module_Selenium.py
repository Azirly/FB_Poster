#Current Date
#6/14/2016
import os
from selenium import webdriver

#Needed to get rid of the notification popups with Chrome
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--disable-extensions")

#Creates the webdriver for Chrome
driver = webdriver.Chrome(executable_path=r"C:\Users\Juston\Documents\Computer Languages\chromedriver_win32\chromedriver.exe", 
						  chrome_options=chrome_options)
#need the r to convert '/' into '\'
driver.get("http://facebook.com") 

email = driver.find_element_by_id("email")
email_input = input("Email: ")
email.send_keys(email_input)

password = driver.find_element_by_id("pass")
password_input = input("Password: ")
password.send_keys(password_input)

login_button = driver.find_element_by_id("loginbutton")
login_button.click();


driver.get("https://www.facebook.com/groups/990520237699874/")



post_box=driver.find_element_by_tag_name("textarea")
#post_box=driver.find_element_by_xpath("//div[@id='u_0_1v']/div/div/div/div/div/div/div/div/div/div/div/div/div")
post_box.click()
post_box.send_keys("Testing using find_element_by_tag_name not ID.Selenium is easy.")

# post_box=driver.find_element_by_xpath("//div[@id='u_0_1v']") # just this will work
# post_box=driver.find_element_by_class_name("_1p1t")
# post_box.send_keys("Testing using Name not ID.Selenium is easy.")

post_it = driver.find_element_by_class_name("_1mf7 _4jy0 _4jy3 _4jy1 _51sy selected _42ft")
post_it.click()



