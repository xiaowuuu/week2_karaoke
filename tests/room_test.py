import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song
class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Room("Ying")
        self.guest_2 = Room("Patrick")
        self.room_1 = Room("Room 1")
        self.song = Song("Makeba")

    def test_room_has_name(self):
        self.assertEqual("Room 1", self.room_1.name)

    def test_room_check_in_guest(self):
        self.room_1.check_in_guest(self.guest_1.name)
        self.assertEqual(["Ying"], self.room_1.new_guest)
    
    # def test_room_check_out_guest(self):
    #     self.room_1.check_out_guest(self.guest_2.name)
    #     self.assertEqual(["Patrick"], self.room_1.new_guest)

    def test_has_add_song_to_room(self):
        self.room_1.add_songs(self.song)    
        self.assertEqual(["Makeba"], self.room_1.play_list)
