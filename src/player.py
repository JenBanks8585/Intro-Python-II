# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player:
    def __init__(self, name , description , current_room):
        self.name = name 
        self.description = description
        self.current_room = current_room

    def __str__(self):
        return f"My name is {self.name}, and I am {self.description}, and right now, I am in the {self.current_room}."


    def move_player(self, direction):
        new_room = self.current_room.other_rooms(direction)

        if new_room is not None:
            self.current_room = new_room
        else:
            print ('You cant go there')





player1= Player('Marcus', 'the maker', 'outside')
player2= Player('Janice', 'the jumping girl', 'foyer')
player3= Player('Bob', 'the burger lover', 'overlook')
player4= Player('Sandy', 'the dancing queen', 'narrow')
