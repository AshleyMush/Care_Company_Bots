import pandas as pd
import os
from BirdieBot import BirdieBot


email = os.environ.get("email")
work_email = os.environ.get("work_email")
birdie_password = os.environ.get('birdie_pw')
roundsys_passowrd = os.environ.get('roundsys_pw')
BIRDIE_URL = "https://admin.birdie.care/residents"
DRIVER_PATH = 'C:/Users/Ashley/PycharmProjects/Chrome-driver/chromedriver.exe'


Magic_link = "ENTER MAGIC LINK HERE"

Safeguarding_link = 'https://service.oxfordshire.gov.uk/raisingconcernprofessional'




BB = BirdieBot(email,birdie_password,DRIVER_PATH, Magic_link)
BB.open_birdie()
BB.click_clients()
BB.click_groups_select_all()






