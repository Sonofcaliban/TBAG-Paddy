

class Room:
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms={}
        self.character = None
        self.item = None

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def describe(self):
        print(self.description)

    def set_name(self, room_name):
        self.name = room_name
    
    def get_name(self):
        return self.name
    
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print(f"You are in the {self.name}, {self.description}")
        print("----------------------------------------------------------------")
        
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.get_name()} is to the {direction}")
    
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
                print("You can't do that.")
                return self
   
    def set_character(self, new_character):
     self.character = new_character

    def get_character(self):
        return self.character


    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item    
