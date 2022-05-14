from smtplib import SMTP
from email.message import EmailMessage

from src.config.recipients import recipients
from src.config.body import body

sender = "" # Your mail address.
password = "" # The password for your mail address.
smtpURL = "smtp.gmail.com" # The SMTP URL of your mail provider.
smtpPort = "587" # The TLS Port of your mail provider

subject = "Chatkontrolle ist der Untergang der Demokratie" # The subject of the mail

'''
    This class sends mails to all recipients defined in config/mail.txt.
'''
def sendSingleMailInBulk():
    smtpServer = SMTP(smtpURL, smtpPort)
    mail = EmailMessage()
    
    try:
        # Start server/login
        smtpServer.starttls()
        smtpServer.login(sender, password)

        # Setup rough mail
        mail['Subject'] = subject
        mail['From'] = sender
        
        # Iterate over every recipient
        for recipient in cleanseRecipients():
            print('Attempting to send mail to: ' + recipient)
            mail['To'] = recipient
            personalizedMessage = body

            # Replaces [INSERTNAME] with the first word after the first dot, then puts it in Capitalization
            surname = recipient.split(".")[1].split("@")[0].capitalize()
            personalizedMessage.replace("[INSERTNAME]", surname)
            mail.set_content(personalizedMessage)

            # Send mail and delete To-Header, there can only be one!
            smtpServer.sendmail(sender, recipient, mail.as_string())
            del mail['To']
        print('Mail has been sent to all recipients with the message: ' + body)
    finally:
        # Logout
        smtpServer.quit()

'''
    Splits the string of recipients up and only returns their mail address.
'''
def cleanseRecipients():
    # Remove mailto:
    mails = recipients.split('mailto:')
    result = []

    # Iterate, remove ) and add the final product to the result
    for i in range (1, len(mails)):
        result.append(mails[i].split(")")[0])

    return result