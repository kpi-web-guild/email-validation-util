"""Test module email_validation."""
from email_validation import validate_email
import unittest


class EmailValidationTest(unittest.TestCase):
    """Unit tests for email validation module."""
    def test_validate_email(self):
        """Check whether validate_email function behaves correctly."""
        self.assertTrue(validate_email('123@123.com'))
