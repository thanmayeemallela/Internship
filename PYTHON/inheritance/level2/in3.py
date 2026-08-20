class Room:
    def __init__(self, name):
        self.name = name

class House:
    def __init__(self):
        self.rooms = [Room("Bedroom"), Room("Kitchen"), Room("Hall")]

    def show_rooms(self):
        for room in self.rooms:
            print(room.name)

House().show_rooms()
