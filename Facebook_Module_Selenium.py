#Current Date
#9/17/2016
import time
import os
from selenium import webdriver

##The Initial Setup
#Needed to get rid of the notification popups with Chrome
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--disable-extensions")

#Creates the webdriver for Chrome 
#need the r to convert '/' into '\'
driver = webdriver.Chrome(executable_path=r"C:\Users\Juston\Documents\Computer Languages\chromedriver_win32\chromedriver.exe", 
						  chrome_options=chrome_options)

#Text groups
facebook_groups = {
	'My Test Group' : "https://www.facebook.com/groups/990520237699874/"
	'WICS': 'https://www.facebook.com/groups/women.in.ics/',
	'IEEE': 'https://www.facebook.com/groups/353086428076607/',
    'BIM': 'https://www.facebook.com/groups/353033718081878/',
    'SWE': 'https://www.facebook.com/groups/2200130987/',
    'DATspace': 'https://www.facebook.com/groups/datspace/', #problem
    'ICS': ' https://www.facebook.com/groups/353008418084408/',
    'CS': 'https://www.facebook.com/groups/352925081426075/',
    'ICSSC': 'https://www.facebook.com/groups/323935841652/',
    'ACM': 'https://www.facebook.com/groups/acmuci/',
    'VGDC': 'https://www.facebook.com/groups/vgdcuci/',         #problem
    'UCI Hackers': 'https://www.facebook.com/groups/HackAtUCI/', #problem
    'IN4MATX ': 'https://www.facebook.com/groups/353047451413838/',
    'UCI AppDev': 'https://www.facebook.com/groups/804525909598967/', #problem
    'Class 2019': 'https://www.facebook.com/groups/uciclassof2019/', #problem
    'Class 2018': 'https://www.facebook.com/groups/2018UCI/', #problem
    'Class 2017': 'https://www.facebook.com/groups/UCIClass2017/', #problem
	'Class 2020': 'https://www.facebook.com/groups/1168755996483730/'
	}
group_message = " "


def facebook_login():
	'''
	Function sends the driver to Fackbook and allows the user to login
	'''
	driver.get("http://facebook.com") 

	email = driver.find_element_by_id("email")
	email_input = input("Email: ")
	email.send_keys(email_input)

	password = driver.find_element_by_id("pass")
	password_input = input("Password: ")
	password.send_keys(password_input)

	login_button = driver.find_element_by_id("loginbutton")
	login_button.click();

def regular_group_post(group_url: str):
	'''
	Function sends the driver to the Fackbook group and allows the user to post his message
	'''
	driver.get(group_url)
	
	#Selects the textbox within the group and sends the text
	post_box=driver.find_element_by_tag_name("textarea")
	post_box.click()
	post_box.send_keys("Testing using find_element_by_tag_name not ID.Selenium is easy.")

	#Timer is needed to give the browser time to respond to the input
	time.sleep(3)

	#Finds the Post button and clicks it
	post_it = driver.find_element_by_xpath("//*[@data-testid='react-composer-post-button']")
	post_it.click()


if __name__ == "__main__":
	facebook_login()
	regular_group_post("https://www.facebook.com/groups/990520237699874/")
	'''
	for name,url in facebook_groups.items():
		regular_group_post(url)
	'''