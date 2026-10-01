class Room:
    def __init__(self, name):
        self.name = name

class House:
    def __init__(self):
        # The House CREATES the Rooms inside itself
        self.bedroom = Room("Master Bedroom")
        self.kitchen = Room("Kitchen")

# Creating a house automatically creates its rooms
my_house = House()
print(my_house)
# If we delete the house, the rooms are destroyed too
del my_house 
# 'my_house.bedroom' no longer exists anywhere in memory.
# print(my_house)