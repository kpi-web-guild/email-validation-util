"""Test module email_validation."""
from email_validation import validate_email
import unittest


class EmailValidationTest(unittest.TestCase):
    """Unit tests for email validation module. "When True"."""
    def test_validate_email(self):
        """Check whether validate_email function behaves correctly."""
        self.assertTrue(validate_email('123@123.com'))

    def test_validate_email_2(self):
        """Unit tests for email validation module. "When False"."""
        self.assertFalse(validate_email('АБВ123@123.com'))
