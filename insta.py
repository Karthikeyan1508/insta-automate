# pip install selenium beautifulsoup4 webdriver-manager

from bs4 import BeautifulSoup as bs
import selenium.common.exceptions
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# User credentials and URLs
username = "karthikeyan.1508"
password = "Karthi@369#keyan"
url = "https://www.instagram.com/"

def setup_browser():
    global chrome
    exe_path = r"C:\Users\This PC\Downloads\chromedriver_win32\chromedriver.exe"  # Update the path to your ChromeDriver
    service = Service(executable_path=exe_path)
    chrome = webdriver.Chrome(service=service)

def url_name(url):  
    # Open the web page
    chrome.get(url) 
    time.sleep(4)  # Wait for the page to load

def login(username, your_password):
    # Find and fill the username field
    usern = chrome.find_element(By.NAME, "username") 
    usern.send_keys(username) 

    # Find and fill the password field
    passw = chrome.find_element(By.NAME, "password") 
    passw.send_keys(your_password)	 
    passw.send_keys(Keys.RETURN)

    time.sleep(10)  # Wait for login to complete

    # Handle popups for 'Save Info' and 'Turn on Notifications'
    try:
        notn = chrome.find_element(By.CLASS_NAME, "x1i10hfl")  # Don't save info button
        notn.click()
        time.sleep(10)

        no = chrome.find_element(By.CLASS_NAME, "_a9_1")  # Don't turn on notifications button
        no.click()
        time.sleep(5)
    except selenium.common.exceptions.NoSuchElementException:
        pass

def first_picture():
    pictures = chrome.find_elements(By.CLASS_NAME, '_aagw')  # Find pictures
    for picture in pictures:
        picture.click()  # Click the first picture
        print("Clicked the picture")
        time.sleep(2)
        break  # Remove this break to click all pictures

def like_pic():
    time.sleep(2)
    try:
        like = chrome.find_element(By.XPATH, "//span[@aria-label='Like']")
        soup = bs(like.get_attribute('innerHTML'), 'html.parser')
        if soup.find('svg')['aria-label'] == 'Like':
            like.click()  # Like the post
            print("Liked the post!")
        else:
            print("Post already liked or like button not found.")
    except selenium.common.exceptions.NoSuchElementException:
        print("Like button not found.")

def next_picture():
    time.sleep(2)
    try:
        nex = chrome.find_element(By.CLASS_NAME, "coreSpriteRightPaginationArrow")  # Next button
        return nex
    except selenium.common.exceptions.NoSuchElementException:
        return None

def continue_liking():
    while True:
        next_el = next_picture()
        if next_el is not None:  # Check if next button is found
            next_el.click()  # Click the next button
            time.sleep(2)
            like_pic()  # Like the picture
            time.sleep(2)
        else:
            print("No more pictures to like.")
            break

# Main execution starts here
if __name__ == "__main__":
    setup_browser()
    time.sleep(1)
    url_name(url)
    login(username, password)
    first_picture()
    continue_liking()
    
    # Close browser after task completion
    chrome.quit()
