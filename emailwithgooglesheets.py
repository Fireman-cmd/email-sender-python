from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account
import os
import re
import pandas as pd
import smtplib
import smtplib
from email.message import EmailMessage
SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# If modifying these scopes, delete the file token.json.
# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1suNGwz8X_qWwxAL5fWwpTOgoJ3YR4sz86F4BNj54NMo'

    
    
service = build('sheets', 'v4', credentials=creds)
# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Sheet1!A:A").execute()
                            

values = result.get('values', [])
print(values)

FROMADDR = "emailnew642@gmail.com"
LOGIN    = FROMADDR
PASSWORD = "Redminote5@123"
TOADDRS  = ["coffuino@gmail.com","emailnew642@gmail.com"]
SUBJECT  = "COWIN SLOTS ALERT"

msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
       % (FROMADDR, ", ".join(TOADDRS), SUBJECT) )
msg += "SLOT VACANCY AT\r\n"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(LOGIN, PASSWORD)
server.sendmail(FROMADDR, TOADDRS, msg)
server.quit()

