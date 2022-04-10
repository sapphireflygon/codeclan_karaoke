import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("70's theme", 6)
        self.room2 = Room("90's theme", 8)

        self.guest1 = Guest("Bojack Horseman", 100.00)
        self.guest2 = Guest("Sarah Lynn", 10.00)
        self.guest3 = Guest("Mr Peanutbutter", 5000.00)
        self.guest4 = Guest("Todd Chavez", 2.50)

        self.room1.song_list = [
            Song("Bohemian Rhapsody", "Queen"),
            Song("Fame", "David Bowie"), 
            Song("My Life", "Billy Joel")
        ]

        self.room2.song_list = [
            Song("Linger", "The Cranberries"),
            Song("Wannabe", "Spice Girls")
        ]

        self.room1.guest_list = []
        self.room2.guest_list = []


    def test_room_has_name(self):
        self.assertEqual("90's theme", self.room2.name)

    def test_room_has_max_guest_count(self):
        self.assertEqual(6, self.room1.max_guests)

    def test_room_has_till(self):
        self.assertEqual(0, self.room1.till)

    def test_room_has_entry_fee(self):
        self.assertEqual(12.00, self.room2.entry_fee)

    def test_remove_money_from_guest_wallet(self):
        self.room1.remove_money_from_guest_wallet(self.guest3, 5)
        self.assertEqual(4995, self.guest3.wallet)

    def test_remove_money_from_guest_wallet__fail(self):
        uh_oh = self.room1.remove_money_from_guest_wallet(self.guest4, 5)
        self.assertEqual(2.50, self.guest4.wallet)
        self.assertEqual("You can't afford this!", uh_oh)

    def test_add_money_to_till(self):
        self.room1.add_money_to_till(self.room1.entry_fee)
        self.assertEqual(12.00, self.room1.till)

    def test_check_in_guest(self):
        self.room1.check_in_guest(self.guest1)
        self.assertEqual(1, len(self.room1.guest_list))

    def test_check_in_guest__room_full(self):
        self.room1.check_in_guest(self.guest3)
        self.room1.check_in_guest(self.guest3)
        self.room1.check_in_guest(self.guest3)
        self.room1.check_in_guest(self.guest3)
        self.room1.check_in_guest(self.guest3)
        self.room1.check_in_guest(self.guest3)
        self.assertEqual(6, len(self.room1.guest_list))
        self.assertEqual("Sorry, this room is full!", self.room1.check_in_guest(self.guest1))

    def test_check_in_guest__cant_afford(self):
        broke_af = self.room1.check_in_guest(self.guest4)
        self.assertEqual("Can't pay the entry fee!", broke_af)
        self.assertEqual(0, len(self.room1.guest_list))

    def test_find_guest_in_room(self):
        self.room1.check_in_guest(self.guest1)
        found_guest = self.room1.find_guest_in_room("Bojack Horseman")
        self.assertEqual("Bojack Horseman", found_guest)

    def test_find_guest_in_room__fail(self):
        no_guest = self.room1.find_guest_in_room("Bojack Horseman")
        self.assertEqual("Bojack Horseman is not in this room", no_guest)

    def test_check_out_guest(self):
        self.room1.check_in_guest(self.guest1)
        self.room1.check_in_guest(self.guest3)
        self.room1.check_out_guest(self.guest1)
        self.assertEqual(1, len(self.room1.guest_list))
        self.assertEqual("Mr Peanutbutter", self.room1.find_guest_in_room("Mr Peanutbutter"))
        self.assertEqual("Bojack Horseman is not in this room", self.room1.find_guest_in_room("Bojack Horseman"))

    def test_room_has_song__true(self):
        found_song = self.room2.find_song_by_title_in_room("Linger")
        self.assertEqual("Linger", found_song)

    def test_room_has_song__false(self):
        no_song = self.room1.find_song_by_title_in_room("Never Gonna Give You Up")
        self.assertEqual("Never Gonna Give You Up is not available in this room", no_song)

    def test_add_song_to_room(self):
        self.room2.add_song_to_room("I Want It That Way", "Backstreet Boys")
        self.assertEqual("I Want It That Way", self.room2.find_song_by_title_in_room("I Want It That Way"))
        self.assertEqual(3, len(self.room2.song_list))

