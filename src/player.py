# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name = "Finney", description = "Mr funny guy", current_room = 'family room'):
        self.name = name 
        self.description = description
        self.current_room = current_room

    def __str__(self):
        return f"My name is {self.name}, and I am {self.description}, and right now, I am in the {self.current_room}."





player1= Player('Marcus', 'the maker', 'outside')
player2= Player('Janice', 'the jumping girl', 'foyer')
player3= Player('Bob', 'the burger lover', 'overlook')
player4= Player('Sandy', 'the dancing queen', 'narrow')

#print(player1)