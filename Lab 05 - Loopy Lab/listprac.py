# list_of_names = ["Bryan", "Keegan", "Alec", "Dean", "Kerry"]
# # n = 2 - 1
# # print(list_of_names)
# # print(list_of_names[n])
# # print(list_of_names[-1])
# # list_of_names[-1] = "Russel"
# # print(list_of_names[-1])

# # for index, value in enumerate(list_of_names):
# #     print(index, value)

# list_of_names.append("Harry")
# print(list_of_names)

# a_list = []
# running_total = 0

# var_bool= False

# while not var_bool:
#     user_input = input("Choose a num to append: ")
#     if user_input == "":
#         var_bool = True
#     else:
#         user_input = int(user_input)
#         a_list.append(user_input)
#     print(a_list)

# for i in range(len(a_list)):
#     running_total += a_list[i]

# print(running_total)

# a_list = [0] * 100

# print(a_list)

# Copy of the array to modify
# my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

# # Loop through each element in myArray
# for item in my_list:
#     # This doubles item, but does not change the array
#     # because item is a copy of a single element.
#     item = item * 2

# # Print the result
# print(my_list)

# list_num = len(my_list)
# print(list_num)
# for i in range(list_num):
#     my_list[i] *=2

# print(my_list)

# a = "Hi"
# b = "There"
# c = "!"
# print(a + b)
# print(a + b + c)
# print(3 * a)
# print(a * 3)
# print((a * 2) + (b * 2))

# # List exercise
# """Print the three month abbreviation for the month number that the user enters. 
# (Calculate the start position in the string, then use the info we just learned to print out the correct substring.)"""
# # Starting code - My code
# months = "JanFebMarAprMayJunJulAugSepOctNovDec"

# while True:
#     n = input("Enter a month number(1-12): ")
#     if n == "":
#         break
#     else:
#         n = int(n)

#     end_ = (n * 3)
#     # Using the end index, we know the start_ will be 3 less than end_
#     start_ = end_ - 3

#     # Handling numbers less than 1 and greater than 12
#     if n <= 0 or n > 12:
#         print()
#         print("Number cannot be less than 1 or greater than 12")
       
#     print(months[start_:end_])

# plain_text = "This is a test. ABC abc"

# for c in plain_text:
#     print(c, end=" ")

# plain_text = "This is a test. ABC abc"

# for c in plain_text:
#     print(ord(c), end=" ")

# plain_text = "This is a test. ABC abc"

# for c in plain_text:
#     x = ord(c)
#     x = x + 1
#     c2 = chr(x)
#     print(c2, end="")


# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/

# Explanation video: http://youtu.be/sxFIxD8Gd3A

# encrypted_text = "Uijt!jt!b!uftu/!BCD!bcd"

# plain_text = ""
# for c in encrypted_text:
#     x = ord(c)
#     x = x - 1
#     c2 = chr(x)
#     plain_text = plain_text + c2
# print(plain_text)

# Create an empty associative array
# (Note the curly braces.)
# x = {}

# # Add some stuff to it
# x["fred"] = 2
# x["scooby"] = 8
# x["wilma"] = 1

# # Fetch and print an item
# print(x["fred"])

class Dog():
    def __init__(self, new_name):
        """ Constructor """
        self.name = new_name
        print("A new dog is born!")


def main():
    # This creates the dog
    my_dog = Dog("Scruffy")
    print(f"The dog's name is: {my_dog.name}")

main()

# 16.6 https://learn.arcade.academy/en/latest/chapters/16_classes/classes.html#creating-objects