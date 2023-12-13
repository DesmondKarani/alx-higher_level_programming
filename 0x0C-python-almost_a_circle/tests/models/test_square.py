import unittest
from models.square import Square
from models.base import Base

class TestSquare(unittest.TestCase):
    
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square_creation(self):
        """Test for correct creation of square."""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(3, 1, 2, 99)
        self.assertEqual(s2.size, 3)
        self.assertEqual(s2.x, 1)
        self.assertEqual(s2.y, 2)
        self.assertEqual(s2.id, 99)

    def test_area(self):
        """Test the area method of square."""
        s1 = Square(4)
        self.assertEqual(s1.area(), 16)

    def test_size_setter(self):
        """Test the size setter of square."""
        s1 = Square(5)
        s1.size = 10
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.size, 10)

    def test_invalid_types(self):
        """Test for type validation."""
        with self.assertRaises(TypeError):
            Square("5")

    def test_invalid_values(self):
        """Test for value validation."""
        with self.assertRaises(ValueError):
            Square(-5)
        with self.assertRaises(ValueError):
            Square(0)

    def test_update_method(self):
        """Test the update method."""
        s1 = Square(5)
        s1.update(89, 2, 3, 4)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        s1 = Square(3, 1, 2, 89)
        s1_dict = s1.to_dictionary()
        expected = {'id': 89, 'size': 3, 'x': 1, 'y': 2}
        self.assertDictEqual(s1_dict, expected)

if __name__ == "__main__":
    unittest.main()

