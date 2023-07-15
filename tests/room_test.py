import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest
class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Ying", 100)
        self.guest_2 = Guest("Patrick", 80)
        self.room_1 = Room("Room 1")
        self.song = Song("Makeba")
        

    def test_room_has_name(self):
        self.assertEqual("Room 1", self.room_1.name)

    def test_room_check_in_guest(self):
        self.room_1.check_in_guest(self.guest_1)
        self.assertEqual(["Ying"], self.room_1.new_guest)
    
    def test_room_check_out_guest(self):
        self.room_1.new_guest = ["Ying", "Patrick", "Craig"]
        self.room_1.check_out_guest(self.guest_2.name)
        self.assertEqual(["Ying", "Craig"], self.room_1.new_guest)

    def test_has_add_song_to_room(self):
        self.room_1.add_songs(self.song)    
        self.assertEqual(["Makeba"], self.room_1.play_list)

    