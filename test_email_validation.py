
import re
import unittest


class EmailValidationTest(unittest.TestCase):
    """unit test for EmailValidation"""
    def test_validate_email(self):
        self.assertTrue(e_mail, validate_email())


def validate_email(a):
    pattern = r'^([a-z]+|[0-9])*@[a-z]+_?[a-z]+\.com$'
    if re.match(pattern, a):
        print('True')
    else:
        print('False')


e_mail = 'vasya@gde-to.ru'
