class AdventureObject:
    """ Class that defines an object in a text adventure game """

    def __init__(self, description, room):
        """ Constructor"""

        # Description
        self.description = description
        # The number of the room that the object is in
        self.room = room
    

def check_if_one_item_is_in_room_v1(my_list, room):
    """
    Return True if at least one item has a property
    """
    i = 0
    while i < len(my_list) and my_list[i].room != room:
        i += 1
    if i < len(my_list):
        return True
    else:
        return False

def check_if_one_item_is_in_room_v2(my_list, room):
    """
    Return true if at least one item has a
    property. Works the same as v1, but less code.
    """
    for item in my_list:
        if item.room == room:
            return True
    return False

def check_if_one_item_has_property(item_list, room):
    for item in item_list:
        if item.room == room:
            return True
    return False

def check_if_all_items_are_in_room(my_list, room):
    for i in my_list:
        if i.room != room:
            return False # Breaks loop if there is no match
    return True


def get_items_in_room(my_list, room):
    """
    Build a brand new list that holds all the items that match our property
    """

    matching_list = []
    for item in my_list:
        if item.room == room:
            matching_list.append(item)
    return matching_list



def check_if_one_item_in_room_v1(my_list, room):
    """
    Return True if at least one item has a property
    """
    for item in my_list:
        if item.room == room:
            return True # Return statement breaks and exits loop (and signals the end of the function)
    
    return False

    # Longer version of the above for loop
    # i = 0

    # while i > len(my_list) and my_list[i].room != room:
    #     i += 1

    # if i < len(my_list):
    #     # Found an item with the property
    #     return True
    # else:
    #     # There is no item with the property
    #     return False
def main():
    object_list = []
    object_list.append(AdventureObject("Key", 5))
    object_list.append(AdventureObject("Bear", 5))
    object_list.append(AdventureObject("Food", 8))
    object_list.append(AdventureObject("Sword", 2))
    object_list.append(AdventureObject("Wand", 10))

    result = check_if_one_item_is_in_room_v1(object_list, 5)
    print("Result of test check_if_one_item_is_in_room_v1:", result)

    result = check_if_one_item_is_in_room_v2(object_list, 5)
    print("Result of test check_if_one_item_is_in_room_v2:", result)

    result = check_if_all_items_are_in_room(object_list, 5)
    print("Result of test check_if_all_items_are_in_room:", result)

    result = get_items_in_room(object_list, 5)
    print("Number of items returned from test get_items_in_room:", len(result))


main()     


# import random


# def create_list(list_size):
#     """ Create a list of random numbers """
#     my_list = []

#     for i in range(list_size):
#         my_list.append(random.randrange(100))

#     return my_list


# def check_if_one_item_has_property_v1(my_list, key):
#     """
#     Return true if at least one item has a
#     property.
#     """
#     list_position = 0
#     while list_position < len(my_list) and my_list[list_position] != key:
#         list_position += 1

#     if list_position < len(my_list):
#         # Found an item with the property
#         return True
#     else:
#         # There is no item with the property
#         return False


# def check_if_one_item_has_property_v2(my_list, key):
#     """
#     Return true if at least one item has a
#     property.
#     """
#     for item in my_list:
#         if item == key:
#             # Found an item that matched. Return True
#             return True

#     # Went through the whole list. Return False.
#     return False


# def check_if_all_items_have_property(my_list, key):
#     """
#     Return true if at ALL items have a property.
#     """
#     for item in my_list:
#         if item != key:
#             # Found an item that didn't match. Return False.
#             return False

#     # Got through the entire list. There were no mis-matches.
#     return True


# def get_matching_items(my_list, key):
#     """
#     Build a brand new list that holds all the items
#     that match our property.
#     """
#     matching_list = []
#     for item in my_list:
#         if item == key:
#             matching_list.append(item)
#     return matching_list


# def main():

#     # Create a list of 50 numbers
#     my_list = create_list(50)
#     print(my_list)

#     # Is at least one item zero?
#     key = 0
#     result = check_if_one_item_has_property_v1(my_list, 0)
#     if result:
#         print("At least one item in the list is", key)
#     else:
#         print("No item in the list is", key)

#     # Get items that match the key
#     matching_list = get_matching_items(my_list, key)
#     print("Matching items:", matching_list)

#     # Are all items matching?
#     result = check_if_all_items_have_property(my_list, key)
#     print("All items in random list matching?", result)

#     other_list = [0, 0, 0, 0, 0]
#     result = check_if_all_items_have_property(other_list, key)
#     print("All items in other list matching?", result)


# main()

# # # 27.5 Variations on the linear search

# # def read_in_file(file_name):
# #     """ Read in lines from a file """
    
# #     # Open file for reading, and store a pointer to it in the new variable "file"
# #     my_file = open(file_name)
    
# #     # Create an empty list to store our names
# #     name_list = []
    
# #     # Loop through each line in the file like you would a list
# #     for line in my_file:
# #         # Remove any line feed, carriage returns or spaces at the end of the line
# #         line = line.strip()

# #         # Add the name to the list
# #         name_list.append(line)

# #     my_file.close()
    
# #     return name_list

# # def linear_search(key, name_list):
# #     """ Linear search """

# #     # Start at the beginning of the list
# #     current_list_position = 0

# #     # Loop until you reach the end of the list, or the value at the current position is equal to the key
# #     while current_list_position < len(name_list) and name_list[current_list_position] != key:

# #         # Advance to the next item in the list
# #         current_list_position += 1

# #     return current_list_position

# # def main():

# #     key = "Cornelius Frostheim"
# #     name_list = read_in_file("super_villains.txt")
# #     list_position = linear_search(key, name_list)

# #     if list_position < len(name_list):
# #         print("The name", key,  "is at position", list_position)
# #     else:
# #         print("The name was not on the list")


# # main()



# # # def main():
# # #     """ Read in lines from a file """
# # #     name_list = []
# # #     # Open file, and automatically close when we exit this block.
# # #     with open("super_villains.txt") as my_file:
# # #         # Loop through each line in the file like a list
# # #         for line in my_file:
# # #             line = line.strip()
# # #             print(line)
# # #             name_list.append(line)
# # #     print(f"name_list is {len(name_list)} names long")
    
# # # main()





# # #def main():
# # #     """ Read in lines from a file """

# # #     # Open the file for reading, and store a pointer to it in the new variable "file"
# # #     my_file = open("super_villains.txt")
    
# # #     #empty_list = []
# # #     # Loop through each line in the file like a list
# # #     for line in my_file:
# # #         line = line.strip()
# # #         #empty_list.append(line)
# # #         print(line)
    
# # #     # for i in empty_list:
# # #     #     print("Line: ", i)
# # #     my_file.close()

# # #     if my_file.closed == True:
# # #         print("File closed")
# # # main()