import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_assignment(self):
        """Test for id assignment."""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        """Test conversion of dictionary to JSON string."""
        dict_list = [{'id': 12}, {'id': 34}]
        json_str = Base.to_json_string(dict_list)
        self.assertEqual(json_str, '[{"id": 12}, {"id": 34}]')

    def test_from_json_string(self):
        """Test conversion of JSON string to dictionary."""
        json_str = '[{"id": 12}, {"id": 34}]'
        dict_list = Base.from_json_string(json_str)
        self.assertEqual(dict_list, [{'id': 12}, {'id': 34}])

    def test_save_to_file(self):
        """Test saving to file."""
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])
        with open("Base.json", "r") as file:
            content = file.read()
            self.assertIn('{"id": 1}', content)
            self.assertIn('{"id": 2}', content)

    def test_load_from_file(self):
        """Test loading from file."""
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])
        objects = Base.load_from_file()
        self.assertIsInstance(objects[0], Base)
        self.assertIsInstance(objects[1], Base)
        self.assertEqual(objects[0].id, 1)
        self.assertEqual(objects[1].id, 2)

    def test_create(self):
        """Test the create method."""
        b1 = Base.create(**{'id': 89})
        self.assertEqual(b1.id, 89)

if __name__ == "__main__":
    unittest.main()
