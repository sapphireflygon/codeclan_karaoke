from classes.song import Song

class Room:
    def __init__(self, input_name, input_max_guests):
        self.name = input_name
        self.max_guests = input_max_guests
        self.till = 0
        self.entry_fee = 12.00
        self.song_list = []
        self.guest_list = []

    def remove_money_from_guest_wallet(self, guest, amount):
        if guest.wallet >= amount:
            guest.wallet -= amount
        return "You can't afford this!"

    def add_money_to_till(self, amount_to_add):
        self.till += amount_to_add

    def check_in_guest(self, guest_to_add):
        if len(self.guest_list) < self.max_guests:
            if guest_to_add.wallet >= self.entry_fee:
                self.remove_money_from_guest_wallet(guest_to_add, self.entry_fee)
                self.add_money_to_till(self.entry_fee)
                self.guest_list.append(guest_to_add)
            return "Can't pay the entry fee!"
        return "Sorry, this room is full!"

    def find_guest_in_room(self, guest_name):
        for guest in self.guest_list:
            if guest_name == guest.name:
                return guest_name
        return f"{guest_name} is not in this room"

    def check_out_guest(self, guest_leaving):
        self.guest_list.remove(guest_leaving)

    def find_song_by_title_in_room(self, song_title):
        for song in self.song_list:
            if song_title == song.title:
                return song_title
        return f"{song_title} is not available in this room"

    def add_song_to_room(self, song_title, song_artist):
        song = Song(song_title, song_artist)
        self.song_list.append(song)

