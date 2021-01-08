# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, stuff = []):
        self.name = name
        self.description = description
        self.stuff = [stuff] # whatever item we pass into the room will be put into a list rather than a single item -- we will be able to append / iterate
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def __repr__(self):             
        return f'{self.stuff}'

    def add_item(self, item):
        self.stuff.append(item)

    def remove_item(self, item):
        self.stuff.remove(item)
        # This doesn't work -->
        # for i in range(0, (len(self.stuff) - 1)): # i will start at 0 and go all the way through the length of self.stuff
        #     if self.stuff[i].name == item.name:
        #         self.stuff.pop(i)

    def print_message(self):
        for item in self.stuff:
            print(f'Items: {item.name}, Description: {item.description}')
