#!/usr/bin/python3
"""Test for console"""

import unittest
import pep8
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """this will test the console"""

    @classmethod
    def setUpClass(cls):
        """Setup test"""
        cls.consol = HBNBCommand()

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_emptyline(self):
        """Test empty line input console"""
        with patch('sys.stdout', new=StringIO()) as mock_consol:
            self.consol.onecmd("\n")
            self.assertEqual('', mock_consol.getvalue())

if __name__ == "__main__":
    unittest.main()
