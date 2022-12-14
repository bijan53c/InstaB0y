import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys





# Setting firefox as browser

firefox_options = Options()
firefox_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
browser = webdriver.Firefox(options=firefox_options)


# Opening instagram website to log in
browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher")






## Finding required elements

### Username field
usernameField = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input")

###Password field
passwordField = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input")


#login Button (When it is Clickable)
loginButton = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button/div")
#########find_element(by=By.XPATH, value="/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button/div")




# Read user data (Username and Password to log in to instagram)
### Not ready yet
username = "Username"
password = "password"





# Log in process
### Entering credentials into fields
usernameField.send_keys(username)
passwordField.send_keys(password)
#### Wait so login button is clickable and ready
time.sleep(2)
###clicking 
loginButton.click()

# wait to check the popups
time.sleep(5)
#Save account info popup , bypass
try :
	##Check if the pop up is there
	notNow_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
	time.sleep(2)
	##Bypassing
	notNow_button.click()
except:
	pass

time.sleep(5)
#TurnON notification popup
try :
	#check if pop up is there
	notNowNotif = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]")
	time.sleep(1)
	##Bypass
	notNowNotif.click()
except :
	pass

time.sleep(5)

# Process of logging out of account (used when the main bot process is done)
def logout():
	time.sleep(5)
	try:
		browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[1]").click()
		time.sleep(2)
		browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/div[6]/div/div/div/div/div").click()
	except:
		print(">>> failed to logout")

#liking new posts
def likeActionPOST():
	#Like the post you just opened and go for the next.
	time.sleep(5)
	try :
		browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button").click()
	except NoSuchElementException:
		print(">>>  Failed to like.")


	time.sleep(5)
	try :
		browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button").click()
	except NoSuchElementException:
		print(">>> Failed to switch to next one.")


# Post opening function
def open_first_post() :
	# first scroll to recent posts
	print("Scrolling ...")
	recent_Xpath = browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/h2')
	recent_Xpath.location_once_scrolled_into_view

	# Then open the first post 
	post_xpath = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div/div[1]/div[1]'

	print ("POSTXPATH =  ",post_xpath)
	try:
		browser.find_element_by_xpath(post_xpath).click()
	except NoSuchElementException:
		print(">>> Failed to open post")
	time.sleep(5)



# This function closes any open post from the x button on top right of screen
# Can be used before logout function
def close_POST():
	try:
		browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div").click()
	except:
		print(">>> Failed to close post")


PostAmount = 10
#finding hashtags and liking posts
##hashtags to look for
hashtag_list = ["instagram"]
#explore
for hashtag in hashtag_list :
	LikedPosts = 0
	searchbar = browser.get('https://www.instagram.com/explore/tags/'+ hashtag + '/')
	time.sleep(10)
	open_first_post()

	while LikedPosts < PostAmount :
		likeActionPOST()
		LikedPosts += 1
		print ("Posts liked so far: ",LikedPosts ," __Hashtag: ",hashtag)
		if LikedPosts == PostAmount :
			print ("All done")
			print("Closing current post")
			close_POST()
			print ("Logging out...")
			logout()
			break


