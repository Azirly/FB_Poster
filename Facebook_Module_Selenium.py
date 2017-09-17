#Current Date
#11/5/2016
import time
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
##The Initial Setup

'''Needed to get rid of the notification popups with Chrome'''
chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2,
			"credentials_enable_service": False,
			"profile.password_manager_enabled": False}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--disable-extensions")

'''Creates the webdriver for Chrome '''
driver = webdriver.Chrome(chrome_options=chromeOptions)
driver.implicitly_wait(5)

'''List of Text Groups'''
facebook_groups = {
	# 'My Test Group' : "https://www.facebook.com/groups/990520237699874/",
	# 'Buy Sell Group' : "https://www.facebook.com/groups/581264068726629",
	'WICS': 'https://www.facebook.com/groups/women.in.ics/',
	'IEEE': 'https://www.facebook.com/groups/353086428076607/',
    'BIM': 'https://www.facebook.com/groups/353033718081878/',
    'SWE': 'https://www.facebook.com/groups/2200130987/',
    'DATspace': 'https://www.facebook.com/groups/datspace/', 
    'ICS': ' https://www.facebook.com/groups/353008418084408/',
    'CS': 'https://www.facebook.com/groups/352925081426075/',
    'ICSSC': 'https://www.facebook.com/groups/323935841652/',
    'ACM': 'https://www.facebook.com/groups/acmuci/',
    'VGDC': 'https://www.facebook.com/groups/vgdcuci/',         
    # 'UCI Hackers': 'https://www.facebook.com/groups/HackAtUCI/', 
    'IN4MATX ': 'https://www.facebook.com/groups/353047451413838/',
    'UCI AppDev': 'https://www.facebook.com/groups/804525909598967/', 
    'Class 2019': 'https://www.facebook.com/groups/uciclassof2019/', 
    # 'Class 2018': 'https://www.facebook.com/groups/2018UCI/', 
    'Class 2017': 'https://www.facebook.com/groups/UCIClass2017/', 
	# 'Class 2020': 'https://www.facebook.com/groups/1168755996483730/',	
    'Class 2021': 'https://www.facebook.com/groups/UCIrvine2021/'
	}

'''Accessing the group_message to post'''
text_file = open('message_to_send.txt', 'r')
group_message = text_file.read()


#the Find functions are used for the WebDriverWait function.
def FindFirstPartBox(driver):
    '''
    Checks if the textbox is located and returns it, else return False
    '''
    first_item = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@data-tooltip-content='Add Photo/Video']")))
    if first_item:
        return first_item
    else:
        return False

def FindRegularBox(driver):
	'''
	Checks if the textbox is located and returns it, else return False
	'''
	element_write_post = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@data-tooltip-content='Write Post']")))
	if element_write_post:
		return element_write_post
	else:
		return False

def FindBuyBox(driver):
    '''
    Checks if the textbox is located and returns it,, else return False
    '''
    element_start_discussion = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@data-tooltip-content='Start Discussion']")))
    if element_start_discussion:
        return element_start_discussion
    else:
        return False
		
def FindPostButton(driver):
	'''
	Checks if the post buttom is located, else return False
	'''
	post_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='react-composer-post-button']")))
	if post_button:
		return post_button
	else:
		return False

def FindTextBox(driver):
	'''
	Checks if the textbox is located, else return False
	'''
	textbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@role='textbox']")))
	if textbox:
		return textbox
	else:
		return False


def TextToInput(string_input):
    '''
    Function finds the writing section of the box and pastes in the string_input.
    '''
    textbox = FindTextBox(driver)
    textbox.click()
    actions = ActionChains(driver)
    actions.move_to_element(textbox)
    actions.click(textbox)
    actions.send_keys(string_input)
    actions.perform()
    # time.sleep(5)
    
    FindPostButton(driver).click()
    time.sleep(5)
    
def GroupPosting(group_url):

    '''First try if it is a regular group post'''
    driver.get(group_url)
    try:
        FindFirstPartBox(driver).click()
        FindRegularBox(driver).click()
        TextToInput(group_message)
            
    except:
        '''Then try if it is a buy group post'''
        FindBuyBox(driver).click()
        TextToInput(group_message)
        
def FacebookLogin():
	'''
	Function sends the driver to Facebook and allows the user to login
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

    
# def regular_group_post(group_url: str):
	# '''
	# Function sends the driver to the Facebook group and allows the user to post his message
	# '''
	# driver.get(group_url)
	
	# post_to_regular_box(group_message)

# def buy_sell_group_post(group_url: str): #issue here
	# error here!
	# '''
	# Function sends the driver to the Facebook group 
	# and allows the user to post his message
	# '''
	# driver.get(group_url)

	# Select the correct icon to choose
	# click_start_discussion = driver.find_element_by_xpath("//*[@data-tooltip-content='Start Discussion']")
	# click_start_discussion.click()
	# post_to_buy_box(group_message)

# def post_to_regular_box(post_info: str):
	# '''
	# Function accesses the post box and sends the information
	# '''
	# Selects the textbox within the group and sends the text 
	# post_box= WebDriverWait(driver, 10).until(find_text_box)
	
	# post_box.click()
	
	# post_box.send_keys(post_info)
	
	# time.sleep(5)
	# Finds the Post button and clicks it
	# post_it = driver.find_element_by_xpath("//*[@data-testid='react-composer-post-button']")
	# post_it.click()
	# time.sleep(5)
	

# def post_to_buy_box(post_info: str):
	# '''
	# Function accesses the post box and sends the information
	# '''
	# Selects the textbox within the group and sends the text

	# post_box= WebDriverWait(driver, 10).until(FindBuyBox)
	
	# post_box.click()
	# post_box.send_keys(post_info)

	# Finds the Post button and clicks it
	# post_it = WebDriverWait(driver, 10).until(FindPostButton)
	# post_it.click()
	# time.sleep(5)
	

if __name__ == "__main__":
    try:
        FacebookLogin()
        
        counter = 0
        while (counter < 5):
            GroupPosting("https://www.facebook.com/groups/581264068726629")
            GroupPosting("https://www.facebook.com/groups/990520237699874/")
            counter += 1
            print(counter)
        
        # print(facebook_groups.items())
        # for name,url in facebook_groups.items():
            # print(name)
            # GroupPosting(url)
    except:
        driver.quit()
    driver.quit()
	
	