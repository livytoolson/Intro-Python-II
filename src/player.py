# Write a class to hold player information, e.g. what room they are in
# currently.
# pep8online.com --> copy and paste code from file to check if it complies with pep8
# always have an extra blank line at the end of your code

class Player:
    def __init__(self, name, current_room, stuff = []):
        self.name = name
        self.current_room = current_room
        self.stuff = stuff


    def __repr__(self): # pass in self on every method, repr is explicit for development. str is to make it human readable.
        return f'{self.stuff}'


    def grab(self, item): # item is a parameter, we don't need the class
        self.stuff.append(item)
        print('You\'ve picked up the item!')
        print('Your inventory:', self.stuff) # could also use an f string


    def drop(self, item):
        print(f'You are removing: {item}')
        self.stuff.remove(item)
