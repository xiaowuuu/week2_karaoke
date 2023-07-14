import unittest
from src.guest import Guest
from src.room import Room
class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Ying", 100)
    
    def test_has_guest_name(self):
        self.assertEqual("Ying", self.guest_1.name)

    # @unittest.skip("delete this line to run the test") 
    def test_guest_has_money(self):
        self.assertEqual(100, self.guest_1.money)
        