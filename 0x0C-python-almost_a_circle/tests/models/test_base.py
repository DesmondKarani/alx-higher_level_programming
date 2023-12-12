import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_id_auto_increment(self):
        """Test if id is auto-assigned correctly."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_manual_assignment(self):
        """Test if id is manually assigned correctly."""
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_id_mixed_assignment(self):
        """Test mixed id assignment."""
        b4 = Base()
        b5 = Base(7)
        b6 = Base()
        self.assertEqual(b4.id, 3)  # Assuming no other instances are created before this
        self.assertEqual(b5.id, 7)
        self.assertEqual(b6.id, 4)

if __name__ == '__main__':
    unittest.main()
