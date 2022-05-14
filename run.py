' The main file of the project, only starts the mailsendingtons. '
from src.service.mail import sendSingleMailInBulk

if __name__=='__main__':
    sendSingleMailInBulk()