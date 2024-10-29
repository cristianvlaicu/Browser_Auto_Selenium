from selenium import webdriver  # Import the webdriver module from Selenium
from selenium.webdriver.chrome.service import Service  # Import the Service class for managing the ChromeDriver service
from selenium.webdriver.chrome.options import Options  # Import the Options class for customizing Chrome options
from selenium.webdriver.support.ui import WebDriverWait  # Import the WebDriverWait class for explicit waits
from selenium.webdriver.support import expected_conditions as EC  # Import the expected_conditions module for wait conditions
from selenium.webdriver.common.by import By  # Import the By class for locating elements
import os

class WebAutomation:
    def __init__(self):
        chrome_options = Options()  # Create an instance of the Chrome options
        chrome_options.add_argument("--disable-search-engine-choice-screen")  # Add an argument to disable the search engine choice screen

        download_path = os.getcwd()  # Get the current working directory
        prefs = {'download.default_directory': download_path}  # Set download directory preference
        chrome_options.add_experimental_option('prefs', prefs)  # Add download preference to Chrome options

        service = Service('chromedriver-win64/chromedriver.exe')  # Create a Service object with the path to the ChromeDriver executable
        self.driver = webdriver.Chrome(options=chrome_options, service=service)  # Create a Chrome webdriver instance with the specified options and service

    def login(self, username, password):
        self.driver.get('https://demoqa.com/login')  # Navigate to the login page

        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))  # Wait for the username field to be visible
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))  # Wait for the password field to be visible
        login_button = self.driver.find_element(By.ID, 'login')  # Find the login button

        username_field.send_keys(username)  # Enter the username
        password_field.send_keys(password)  # Enter the password
        self.driver.execute_script("arguments[0].click();", login_button)  # Click the login button using JavaScript

    def fill_form(self, fullname, email, current_address, permanent_address):
        # Wait for the element with the specified XPATH to be visible and store it in elements
        elements = (WebDriverWait(self.driver, 10).
                    until(EC.visibility_of_element_located((By.XPATH,
                    '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div'))))
        # Click the element
        elements.click()

        # Wait for the text box element with the ID 'item-0' to be visible and store it in text_box
        text_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
        # Click the text box
        text_box.click()

        # Wait for the fullname field with the ID 'userName' to be visible and store it in fullname_field
        fullname_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        # Wait for the email field with the ID 'userEmail' to be visible and store it in email_field
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
        # Wait for the current address field with the ID 'currentAdress' to be visible and store it in current_adress_field
        current_address_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
        # Wait for the permanent address field with the ID 'permanentAdress' to be visible and store it in permanent_adress_field
        permanent_address_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))
        # Find the 'submit' button with the ID 'submit' and store it in submit_button
        submit_button = self.driver.find_element(By.ID, 'submit')

        # Enter 'John Smith' into the fullname field
        fullname_field.send_keys(fullname)
        # Enter 'john@gmail.com' into the email field
        email_field.send_keys(email)
        # Enter 'John Street 100, New York, USA' into the current address field
        current_address_field.send_keys(current_address)
        # Enter 'John Street 100, New York, USA' into the permanent address field
        permanent_address_field.send_keys(permanent_address)
        # Click the 'submit' button using JavaScript
        self.driver.execute_script("arguments[0].click();", submit_button)

    def download(self):
        # Wait for 'upload/download element' to be visible
        upload_download = (WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-7'))))
        # Click the upload/download element
        upload_download.click()
        # Find the download button element
        download_button = self.driver.find_element(By.ID, 'downloadButton')
        # Click the download button using JavaScript
        self.driver.execute_script("arguments[0].click();", download_button)

    def close(self):
        self.driver.quit()  # Close the browser and quit the driver

if __name__ == "__main__":
    webautomation = WebAutomation()
    webautomation.login('pythonstudent', 'PythonStudent123$')
    webautomation.fill_form('John Smith', 'john@gmail.com', 'John Street 100, New York, USA', 'John Street 100, New York, USA')
    webautomation.download()
    webautomation.close()

