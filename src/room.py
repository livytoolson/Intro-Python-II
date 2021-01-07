# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, stuff = []):
        self.name = name
        self.description = description
        self.stuff = stuff
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def __repr__(self):             
        return f'{self.stuff}'

    def add_item(self, item):
        self.stuff.append(item.name)
