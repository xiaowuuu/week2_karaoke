class Room:
    def __init__(self, name):
        self.name = name
        self.new_guest = []
        self.play_list = []
        self.entry = 20
        self.capacity = 10

    def check_in_guest(self, guest):
        self.new_guest.append(guest.name)
    
    def check_out_guest(self, guest):
        if guest in self.new_guest:
            self.new_guest.remove(guest)
    
    def add_songs(self, song):
        self.play_list.append(song.name)

    def room_capacity(self):
        left_space = self.capacity - len(self.new_guest)
        if self.capacity > len(self.new_guest):
            return (f"There has {left_space} left.")
        else:
            return (f"There's no space left.")
