class Room:
    def __init__(self, description, north, east, south, west):
        """ This class represents the rooms"""
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
    
def main():
    room_list = []
    room = Room("Bedroom 2", 3, 1, None, None)
    room_list.append(room)
    room = Room("South Hall", 4, 4, None, 0)
    room_list.append(room)
    room = Room("Dining Room", 5, None, None, 1)
    room_list.append(room)
    room = Room("Bedroom 1", None, 4, 0, None)
    room_list.append(room)
    room = Room("North Hall", 6, 5, 1, 3)
    room_list.append(room)
    room = Room("Kitchen", None, None, 2, 4)
    room_list.append(room)
    room = Room("Balcony", None, None, 4, None)
    room_list.append(room)
    
    current_room = 0
    done = False
    
    # Game loop
    while not done:
        print(room_list[current_room].description)
        user_input = input("Where would you like to go? ").lower()
        # North
        if user_input == "n" or user_input == "north":
            next_room = room_list[current_room].north
            if next_room == None:
                print()
                print("You cannot go that way")
            else:
                current_room = next_room
        # East
        elif user_input == "e" or user_input == "east":
            next_room = room_list[current_room].east
            if next_room == None:
                print("You cannot go that way")
            else:
                current_room = next_room
        # South
        elif user_input == "s" or user_input == "south":
            next_room = room_list[current_room].south
            if next_room == None:
                print("You cannot go that way")
            else:
                current_room = next_room
        # West
        elif user_input == "w" or user_input == "west":
            next_room = room_list[current_room].west
            if next_room == None:
                print("You cannot go that way")
                print()
            else:
                current_room = next_room
        # For unhandled input
        elif user_input == "quit":
            done = True
        else:
            print("I do not understand")


main()