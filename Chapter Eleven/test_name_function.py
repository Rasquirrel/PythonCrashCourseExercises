import unittest
from name_function import get_formatted_name

class TestNameFunction(unittest.TestCase):
    """Test the get_formatted_name function"""
    def test_first_last_name(self):
        formatted_name = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name("jose", "moncao", "isac araujo")
        self.assertEqual(formatted_name, "Jose Isac Araujo Moncao")

unittest.main()

