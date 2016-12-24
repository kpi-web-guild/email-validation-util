import email_validation
import unittest


class EmailValidationTest(unittest.TestCase):
    """unit test for EmailValidation"""
    def test_validate_email(self):
        self.assertTrue('123@123.com', email_validation.validate_email())
