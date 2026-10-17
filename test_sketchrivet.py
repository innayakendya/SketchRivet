# test_sketchrivet.py
"""
Tests for SketchRivet module.
"""

import unittest
from sketchrivet import SketchRivet

class TestSketchRivet(unittest.TestCase):
    """Test cases for SketchRivet class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SketchRivet()
        self.assertIsInstance(instance, SketchRivet)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SketchRivet()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
