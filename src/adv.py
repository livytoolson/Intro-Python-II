from player import Player # import player
from item import Item
from room import Room
import random

# install bracket pair colorizer

stuff = {
    'map': Item('map', 'This will guide you throughout the game.'),
    'sword': Item('sword', 'This will defend you.'),
    'flashlight': Item('flashlight', 'This will give you light in darkness.'),
    'armor': Item('armor', 'This will protect you from the enemy.'),
    'potions': Item('potion', 'You can drink it.'),
    'wand': Item('wand', 'Brings magic.'),
    'dagger': Item('dagger', 'Brings protection.'),
    'food': Item('food', 'Gives you energy.'),
    'water': Item('water', 'Hyrdates you.')
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", 
                     stuff[random.choice(list(stuff.keys()))]),
                    #  stuff['map']), # room is always available outside

    'foyer':    Room("Foyer", 
"""Dim light filters in from the south. Dusty passages run north and east.""", # pay attention to docstrings
                    stuff[random.choice(list(stuff.keys()))]), # creates a random selection of items from stuff for the player to use

    'overlook': Room("Grand Overlook", 
"""A steep cliff appears before you, falling into the darkness. Ahead to the north, 
a light flickers in the distance, but there is no way across the chasm.""", 
                    stuff[random.choice(list(stuff.keys()))]),

    'narrow':   Room("Narrow Passage", 
"""The narrow passage bends here from west to north. The smell of gold permeates the air.""", 
                    stuff[random.choice(list(stuff.keys()))]),

    'treasure': Room("Treasure Chamber", 
"""You've found the long-lost treasure chamber! Sadly, it has already been completely 
emptied by earlier adventurers. The only exit is to the south.""", 
                    stuff[random.choice(list(stuff.keys()))]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = Player("Player One", room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# if you can define or describe the length of your input us a for loop (similar to for each in JS)
# if you don't know how long your input is use a while loop, a while loop keeps running until you hit the exit condition
# recursion

direction = ''
while direction != 'q':
    print(f'You are in {new_player.current_room.name}')
    if len(new_player.current_room.stuff) > 0:
        new_player.current_room.print_message()
    else:
        print('There is nothing here!')

    # print(f'There is a {new_player.current_room.stuff.name} in the room!')
    # print(f'{new_player.current_room.description}')
    # print(f'You are holding: {new_player.stuff}')

    inventory = ''
    while inventory != 'x':
        print(f'You are holding: {new_player.stuff}.')
        inventory = input(f"""
        To get an item type 'get [ITEM_NAME]'.
        To drop an item type 'drop [ITEM_NAME]'.
        Or type 'x' to stop adding and removing from your inventory.
    """)

        choice = inventory.split(' ') # this will split it by every space
        if len(choice) >= 2:
            active_item = choice[1].lower().strip() # strip takes care of extra spaces (& maybe extra apostraphes?)
        if choice[0].lower() == 'get':
            new_player.grab(stuff[active_item]) 
            new_player.current_room.remove_item(stuff[active_item])
        elif choice[0].lower() == 'drop':
            new_player.drop(stuff[active_item])
            new_player.current_room.add_item(stuff[active_item])
        elif choice[0].lower() == 'x':
            print('You decided not to add or remove from your inventory.')
        else:
            print('This command is not supported. Try again.')

    # pickup_item = input(f'Do you want to take the {new_player.current_room.stuff.name}? Y/N?')
    # pickup_item = pickup_item.lower()
    # if pickup_item == 'y':
    #     new_player.grab(new_player.current_room.stuff)
    #     new_player.current_room.remove_item(new_player.current_room.stuff.name)  
    # else:
    #     print(f'You chose not to pick up {new_player.current_room.stuff.name}.') # only want to print out the name of the item

    # drop_item = input('Would you like to drop an item? Y/N?')
    # drop_item = drop_item.lower()
    # if drop_item == 'y':
    #     item_to_drop = str(input(f'What would you like to drop? {new_player.stuff}:')) # add a colon or space at the end of each input for readability in the terminal
    #     new_player.drop(item_to_drop.lower().strip())

    direction = input('Where do you want to go? N, S, E, W or q to quit the game?') # this will always store in put as a string, can change it into an integer, float, etc.
    direction = direction.lower()
    if direction == 'n':
        if new_player.current_room.n_to == None:
            print('There is no room to the north.')
        else:
            new_player.current_room = new_player.current_room.n_to
    elif direction == 'e':
        if new_player.current_room.e_to == None:
            print('There is no room to the east.')
        else: 
            new_player.current_room = new_player.current_room.e_to # reassigning variable with singe =
    elif direction == 's':
        if new_player.current_room.s_to == None:
            print('There is no room to the south.')
        else:
            new_player.current_room = new_player.current_room.s_to
    elif direction == 'w':
        if new_player.current_room.w_to == None: # check to see if the room is equal to None
            print('There is no room to the west.')
        else: 
            new_player.current_room = new_player.current_room.w_to
    elif direction == 'q':
        print('Thanks for playing!')
    else:
        print('This movement is not allowed.')
