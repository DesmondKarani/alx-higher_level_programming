import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):
    
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_rectangle_creation(self):
        """Test for correct creation of rectangle."""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(4, 5, 1, 2, 99)
        self.assertEqual(r2.width, 4)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 2)
        self.assertEqual(r2.id, 99)

    def test_area(self):
        """Test the area method of rectangle."""
        r1 = Rectangle(3, 4)
        self.assertEqual(r1.area(), 12)

    def test_invalid_types(self):
        """Test for type validation."""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_invalid_values(self):
        """Test for value validation."""
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_update_method(self):
        """Test the update method."""
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dict = r1.to_dictionary()
        expected = {'id': r1.id, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertDictEqual(r1_dict, expected)


if __name__ == "__main__":
    unittest.main()
