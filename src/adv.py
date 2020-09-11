from room import Room
from player import Player
from item import Item
import sys

## Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}



room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


directions = {'n', 'e', 's', 'w'}


print("################################################")
print("################################################")
print("  ")
print("Welcome to Adventure Game!")
print("All you need to do is find the Treasure Room!")
print("  ")
print("################################################")
print("################################################")
print("  ")


playing_game = True

player = str(input('What is your name? \n'))

print("  ")
print("################################################")
print("################################################")
print("  ")

player1= Player(player, 'the maker', room['outside'])
print(f'Hey {player1.name}, {player1.current_room}')

print("  ")
print("################################################")
print("################################################")
print("  ")

while playing_game:    
    
    print("  ")
    print("################################################")
    print("################################################")
    print("  ")
    
    direc = (input("Where do you want to go? \n [n] North  [e] East   [s] South    [w] West \n"))

    if direc in directions:
        player1.move_player(direc)
        
        print("  ")
        print("################################################")
        print("################################################")
        print("  ")
        print(player1.current_room)

    

    elif direc == 'q':
        print( 'Thanks for playing')
        sys.exit()

    