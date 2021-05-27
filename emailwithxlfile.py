# import csv
# import email
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders

# email_sender=""#my email
# password=""#myemail
# subject="activated"

# with open('emails.csv','r') as csvfile:
#     reader=csv.reader(csvfile)
#     for line in reader:
#         text="hello" + line[1]+"your"+line[2+"your cowin email alert is activated"]
#         email_send=line[0]
#         msg=MIMEMultipart()
#         msg['From']=email_user
#         msg['To']=email_send 
#         msg['Subject']=subject
#         msg.attach(MIMEText(text,"plain"))
#         text=msg.as_string()

#         server=smtplib.SMTP_SSL("smtp.gmail.com",465)
#         server.login(email_user,email_password)
#         server.sendmail(email_user,email_send,text)
#         server.quit
import pandas as pd
import smtplib

'''
Change these to your credentials and name
'''
your_name = "COWIN_EXTENSION"
your_email = "emailnew642@gmail.com"
your_password = "Redminote5@"

# If you are using something other than gmail
# then change the 'smtp.gmail.com' and 465 in the line below
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(your_email, your_password)

# Read the file
email_list = pd.read_excel("EmailList.xlsx")

# Get all the Names, Email Addreses, Subjects and Messages
all_names = email_list['Name']
all_emails = email_list['Email']
all_subjects = email_list['Subject']
all_messages = email_list['Message']

# Loop through the emails
for idx in range(len(all_emails)):

    # Get each records name, email, subject and message
    name = all_names[idx]
    email = all_emails[idx]
    subject = all_subjects[idx]
    message = all_messages[idx]

    # Create the email to send
    full_email = ("From: {0} <{1}>\n"
                  "To: {2} <{3}>\n"
                  "Subject: {4}\n\n"
                  "{5}"
                  .format(your_name, your_email, name, email, subject, message))

    # In the email field, you can add multiple other emails if you want
    # all of them to receive the same text
    try:
        server.sendmail(your_email, [email], full_email)
        print('Email to {} successfully sent!\n\n'.format(email))
    except Exception as e:
        print('Email to {} could not be sent :( because {}\n\n'.format(email, str(e)))

# Close the smtp server
server.close()


