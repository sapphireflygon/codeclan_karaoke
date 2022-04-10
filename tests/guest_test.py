import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Diane Nguyen", 40.00)


    def test_guest_has_name(self):
        self.assertEqual("Diane Nguyen", self.guest1.name)

    def test_guest_has_wallet(self):
        self.assertEqual(40.00, self.guest1.wallet)







