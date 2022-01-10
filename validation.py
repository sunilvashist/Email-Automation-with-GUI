

import  requests
import smtplib
from variables import __API__


def validateEmail(MAC, passw):
    email_from_database = requests.get( __API__ + MAC).text
    email_from_database = email_from_database.replace(r'\r\n', '')
    email_from_database = email_from_database.replace(MAC, '')
    email_from_database = email_from_database.replace(r'"', '')
    email_from_database = email_from_database.replace(':', '')
    email_from_database = email_from_database.replace('{', '')
    email_from_database = email_from_database.replace('}', '')
    email_from_database = email_from_database.strip()


    try:
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(email_from_database, passw)
        return True
    except:
        return False

def extract_email(MAC):
    email_from_database = requests.get( __API__ + MAC).text
    email_from_database = email_from_database.replace(r'\r\n', '')
    email_from_database = email_from_database.replace(MAC, '')
    email_from_database = email_from_database.replace(r'"', '')
    email_from_database = email_from_database.replace(':', '')
    email_from_database = email_from_database.replace('{', '')
    email_from_database = email_from_database.replace('}', '')
    email_from_database = email_from_database.replace(r'\"','')
    email_from_database = email_from_database.replace(r'\'','')
    email_from_database = email_from_database.strip()

    return  email_from_database

