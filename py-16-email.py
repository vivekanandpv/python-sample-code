import smtplib
import ssl

username = input("Your gmail id: ")
password = input("Password: ")
recipient = input('Recipient id: ')

#   this can be the user input as well
#   but take care for multiline message from user input
message = '''Hi there!
I am sending email from Python
Regards,
V
'''

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
    server.login(username, password)
    server.sendmail(username, recipient, message)
