# Imports
from selenium import webdriver
from selenium.common import exceptions
import time

# Variables
username = input("Enter your username: ")
password = input("Enter your password: ")
profile = input("Enter target username: ")
url = f"https://www.instagram.com/accounts/login/?next=%2F{profile}%2F&source=desktop_nav"
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\lenovo\Desktop\EXTRA\chromedriver.exe")


# Solver
driver.get(url)

time.sleep(5)
username_box = driver.find_element_by_xpath(
	r"/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[1]/div/label/input")
password_box = driver.find_element_by_xpath(
	r"/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[2]/div/label/input")
log_in = driver.find_element_by_xpath(
	r"/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[3]/button"
)
username_box.send_keys(username)
password_box.send_keys(password)
log_in.click()

time.sleep(5)
not_now = driver.find_element_by_xpath(r"/html/body/div[1]/section/main/div/div/div/div/button")
not_now.click()

time.sleep(5)
try:
	name = driver.find_element_by_xpath(r"/html/body/div[1]/section/main/div/header/section/div[2]/h1")
	print(f"This profile belongs to: {name.text}")
except exceptions.NoSuchElementException:
	print("This profile belongs to: N/A")
try:
	posts = driver.find_element_by_xpath(r"/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span")
	print(f"No. of posts: {posts.text}")
except exceptions.NoSuchElementException:
	print("No. of posts: N/A")
try:
	followers = driver.find_element_by_xpath(r"/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span")
	print(f"No. of followers: {followers.text}")
except exceptions.NoSuchElementException:
	print("No. of followers: N/A")
try:
	following = driver.find_element_by_xpath(r"/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span")
	print(f"Currently following: {following.text} accounts")
except exceptions.NoSuchElementException:
	print("Currently following: N/A")
try:
	description = driver.find_element_by_xpath(r"/html/body/div[1]/section/main/div/header/section/div[2]/span")
	print("Description: \n" + description.text)
except exceptions.NoSuchElementException:
	print("Description: \nN/A")
