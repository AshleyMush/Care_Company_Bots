
from bs4 import BeautifulSoup
import lxml
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import InvalidSelectorException, NoSuchAttributeException, NoSuchFrameException, \
    NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import imaplib
import email
import re
import os
from email.header import decode_header
import webbrowser
import time


# Adding User-Agent to the request headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


# Sending a GET request to the URL
# response = requests.get(url=BIRDIE_URL, headers=headers)

# Creating a BeautifulSoup object with the content of the response
# soup = BeautifulSoup(response.content, "html.parser")
#
# client_names = soup.find_all(name='span', class_='hrYWVq')

class BirdieBot():
    def __init__(self, email, password, driver_path,  BIRDIE_URL):

        self.email = email
        self.password = password
        self.birdie_url = BIRDIE_URL
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

        """
        self.list_of_windows = len(self.driver.window_handles)
        self.base_window = self.driver.window_handles[0]
        """


    def open_birdie(self):
        print("Opening Birdie... 🌐")
        self.driver.get(self.birdie_url)
        print("Birdie opened successfully. ✅")

    def enter_credentials(self):
        print("⛔Entering credentials ")

        email_input = WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located((By.CLASS_NAME,'input')))
        email_input.send_keys(self.email)
        print("Email Entered")



        print("Clicking Button ")

        login_button = WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn"))
        )
        login_button.click()
        print("Credentials entered successfully.✔\nNow waiting for Magic Link")

    def click_clients(self):
        print("⛔Clicking clients ")
        time.sleep(8)

        clients_btn = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/residents"]')
        clients_btn.click()
        print("Clicked Clients.✔\n")

    def click_groups_select_all(self):
        print("Clicking Groups Button ")

        groups_button = WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable((By.ID, "groups-filter-trigger"))
        )
        groups_button.click()
        print("Groups Button clicked Successfully.✔\n")

        print("Clicking Select all Button ")

        select_all_button = WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="groups-filter"]/div[1]'))
        )
        select_all_button.click()
        print("select all button clicked Successfully.✔\n")









    def search_for_user(self, user):
        print(f"⛔Searching for {user}. In birdie  ")


    # def get_magic_link(self):
    #     password = os.environ.get('wrk_email_pw')
    #     email_addr = os.environ.get('wrk_email')
    #
    #     # Login to your email server
    #     mail = imaplib.IMAP4_SSL('my.imap.server.address')
    #     mail.login(email_addr, password)
    #     mail.select('inbox')
    #
    #     # Search for the specific mail
    #     type, data = mail.search(None, 'FROM', 'support+no-reply@birdie.care', 'SUBJECT',
    #                              'Your Birdie admin login link!')
    #     mail_ids = data[0]
    #
    #     id_list = mail_ids.split()
    #     latest_email_id = int(id_list[-1])
    #
    #
    #     type, data = mail.fetch(str(latest_email_id), '(RFC822)')
    #
    #     magic_link = None
    #
    #     # extract the email body
    #     for response_part in data:
    #         if isinstance(response_part, tuple):
    #             msg = email.message_from_bytes(response_part[1])
    #             if msg.is_multipart():
    #                 for part in msg.walk():
    #                     if part.get_content_type() == "text/plain":
    #                         body = part.get_payload(decode=True).decode('utf-8')
    #                         match = re.search(r'https://admin\.birdie\.care/login\?token=[\w-]+', body)
    #                         if match:
    #                             magic_link = match.group(0)
    #                             break  # Stop after finding the first match
    #             else:
    #                 body = msg.get_payload(decode=True).decode('utf-8')
    #                 match = re.search(r'https://admin\.birdie\.care/login\?token=[\w-]+', body)
    #                 if match:
    #                     magic_link = match.group(0)
    #
    #     if magic_link:
    #         print("Magic link found:", magic_link)  # Optional: Print the magic link for verification
    #         # Use Selenium to navigate to the magic link
    #         self.driver.get(magic_link)
    #     else:
    #         print("Magic link not found.")




