import email_validation
import unittest


class EmailValidationTest(unittest.TestCase):
    """unit test for EmailValidation"""
    def test_validate_email(self):
        self.assertTrue(email_validation.validate_email('123@123.com'))
