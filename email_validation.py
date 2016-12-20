import re


def validate_email(a):
    pattern = r'^([a-z]+|[0-9])*@[a-z]+_?[a-z]+\.com$'
    if re.match(pattern, a):
        print('True')
    else:
        print('False')


a = 'vasya@gde-to.ru'