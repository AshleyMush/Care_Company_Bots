import imaplib
import email
from email.header import decode_header
import webbrowser
import os

password = os.environ.get('wrk_email_pw')
email_addr = os.environ.get('wrk_email')




# Login to your email server
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('ashley.tanaka@angelcare-group.co.uk', 'yourpassword')
mail.select('inbox')

# Search for the specific mail
type, data = mail.search(None, 'FROM', '"support+no-reply@birdie.care"', 'SUBJECT', '"Your Birdie admin login link!"')
mail_ids = data[0]

id_list = mail_ids.split()
latest_email_id = int(id_list[-1])

# Fetch the email body (RFC822) for the latest email
type, data = mail.fetch(latest_email_id, '(RFC822)')

# extract the email body
for response_part in data:
    if isinstance(response_part, tuple):
        msg = email.message_from_bytes(response_part[1])
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                magic_link = # Extract the magic link from the email body using regex or string manipulation

# Use Selenium to navigate to the magic link
driver.get(magic_link)
