"""Test module email_validation."""
from email_validation import validate_email
import unittest


class EmailValidationTest(unittest.TestCase):
    """Unit test for EmailValidation."""
    def test_validate_email(self):
        """Test by assertTrue method."""
        self.assertTrue(validate_email('123@123.com'))
