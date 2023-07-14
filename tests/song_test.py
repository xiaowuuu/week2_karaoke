import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("loop")

# this one works
    def test_has_song(self):
        self.assertEqual("loop", self.song_1.name)

    