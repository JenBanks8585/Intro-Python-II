# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name = "family room", description = "this is where everyone can hang out"):
        self.name = name 
        self.description = description

    def __str__(self):
        return f"This is the {self.name}, and {self.description}."





room1= Room('bedroom', 'when I am too tired, you\'ll find me here.')
room2= Room('basement', 'this is where all forgotten but treasured stuff stays.')
room3= Room('bathroom', 'this is your own business, other we showe here too.')
room4= Room('kitchen', 'this is where we cook and eat.')

print(room2)