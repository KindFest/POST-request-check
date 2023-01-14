import re
import time


def date_validation(date):
    try:
        validation = bool(time.strptime(date, '%d.%m.%Y'))
    except ValueError:
        try:
            validation = bool(time.strptime(date, '%Y-%m-%d'))
        except:
            validation = False
    return validation


def email_validation(email):
    return bool(re.search(r"^[A-Z0-9._%+-]+%40[A-Z0-9.-]+\.[A-Z]{2,}$", email))


def phone_validation(phone):
    return bool(re.match(r'^(%2B7)\+([0-9]{3})\+([0-9]{3})\+([0-9]{2})\+[0-9]{2}$', phone))


def text_validation(text):
    return bool(text.isascii())
