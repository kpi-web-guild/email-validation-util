"""Test module email_validation."""
from email_validation import validate_email
import unittest


class EmailValidationTest(unittest.TestCase):
    """Unit tests for email validation module."""
    def test_validate_email_pass(self):
        """Check whether validate_email function pass."""
        self.assertTrue(validate_email('123@123.com'))
        self.assertTrue(validate_email('abc@abc.com'))
        self.assertTrue(validate_email('abc123@abc123.com'))
        self.assertTrue(validate_email('a.bc_123@abc123.com'))


    def test_validate_email_false(self):
        """Check whether validate_email function false."""
        self.assertFalse(validate_email('АБВ123@123.com'))
        self.assertTrue(validate_email('123@абв.com'))
        self.assertTrue(validate_email('1..23@abc.com'))
        self.assertTrue(validate_email('1-23@abc.com'))
        self.assertTrue(validate_email('1/23abc@abc.com'))
        self.assertTrue(validate_email('1+23@abc.com'))
        self.assertTrue(validate_email('1\23@abc.com'))
        self.assertTrue(validate_email('1!23abc@abc.com'))
        self.assertTrue(validate_email('1*23abc@abc.com'))
        self.assertTrue(validate_email('1?23abc@abc.com'))

