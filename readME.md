In order to protect democracy, I wrote this script. Not sure that the politicians will care, but regardless, I wanted to send them a message. They wanted to abolish the encryption of chat messages for the like 5th time in 3 years, so now I need to automate my mail sending.

# How to use

Feel free to use it for whatever. Just install Python3 and then type

> python run.py

Potentially you'll need to specify your Python version like so

> python3 run.py

In the src/service/mail.py file you'll need to adjust a few parameters (sender, password, smtpURL, smtpPort, subject) and also the body/recipients files in src/config.