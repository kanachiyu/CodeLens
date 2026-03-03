# test_codelens.py
"""
Tests for CodeLens module.
"""

import unittest
from codelens import CodeLens

class TestCodeLens(unittest.TestCase):
    """Test cases for CodeLens class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CodeLens()
        self.assertIsInstance(instance, CodeLens)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CodeLens()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
