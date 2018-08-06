import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """ Tests for name.function.py """

    def test_first_last_name(self):
        """ Do names like Janis Joplin work """
        print("*** Start Test ***")
        formatted_name = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last(self):
        """ Do names like Barrack Hussein Obama work """
        print("*** Start Test ***")
        formatted_name = get_formatted_name("Barrack", "Obama", "Hussein")
        self.assertEqual(formatted_name, 'Barrack Hussein Obama')

unittest.main()