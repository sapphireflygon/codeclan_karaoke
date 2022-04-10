import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Bohemian Rhapsody", "Queen")
        self.song2 = Song("Fame", "David Bowie")
        self.song3 = Song("Vienna", "Billy Joel")
        self.song4 = Song("Linger", "The Cranberries")


    def test_song_has_title(self):
        self.assertEqual("Fame", self.song2.title)

    def test_song_has_artist(self):
        self.assertEqual("Queen", self.song1.artist)
