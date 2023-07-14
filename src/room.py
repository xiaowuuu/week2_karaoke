class Room:
    def __init__(self, name):
        self.name = name
        self.new_guest = []
        self.play_list = []
        self.entry = 20

    def check_in_guest(self, guest):
        self.new_guest.append(guest)
        return self.new_guest
    
    def check_out_guest(self, guest):
        self.new_guest.remove(guest)
        return self.new_guest
    
    def add_songs(self, song):
        self.play_list.append(song.name)