# # 14.2.1 - Problem 1

# for i in range(11):
#     print("*", end=" ")

# # 14.2.2 - Problem 2
# for j in range(10):
#     print("*", end=" ")
# print()
# for k in range(5):
#     print("*", end=" ")
# print()
# for l in range(20):
#     print("*", end=" ")

# # 14.2.3 - Problem 3
# for i in range(8):
#     for j in range(10):
#         print("*", end = " ")
#     print()

# # 14.2.4 - Problem 4
# for i in range(10):
#     for j in range(5):
#         print("*", end = " ")
#     print()

# # 14.2.5 - Problem 5
# for i in range(5):
#     for j in range(20):
#         print("*", end = " ")
#     print()

# # 14.2.6 - Problem 6
# for i in range(10):
#     for j in range(10):
#         print(j, end = " ")
#     print()

# # 14.2.7 - Problem 7
# for i in range(10):
#     for j in range(10):
#         print(i, end = " ")
#     print()


# 14.2.8 - Problem 8
for i in range(11):
    for j in range(i):
        print(j, end = " ")
    print()


""" Look at mudball example """
# import random

# new_num = random.randrange(50)

# #print(new_num)
# guess_1 = 0
# counter = 1

# while guess_1 != new_num:
#     new_guess = int(input("Choose a number: "))
#     guess_1 = new_guess
#     if guess_1 == new_num:
#         print("Congrats!, You guessed right")  
#     elif guess_1 > new_num:
#         print("--- Attempt ", counter)
#         print("Too high.")
#         counter += 1
#     else:
#         print("--- Attempt ", counter)
#         print("Too low.")
#         counter += 1

# a, *b, c =  'Python'

# print(a)
# print(b)
# print(c)

# for i in range(1, 101):
#    print(i)



# for i in range(5):
#     print("I will not chew gum in class.")

# def print_about_gum(repetitions):

#     # Loop that many times
#     for i in range(repetitions):
#         print("I will not chew gum in class.")


# def main():
#     print_about_gum(10)


# main()

# for i in [1,2,3,4,5,6,7,8,9,0]:
#     print(i)

# # What does this print? Why?
# for i in range(3):
#     print("a")
#     for j in range(3):
#         print("b")

# import time
# # Loop from 1:00 to 12:59
# for minute in range(1, 60):
#     for second in range(60):
#         if second >= 10:
#             time.sleep(1)
#             print("0" + str(minute) + ":" + str(second))
#         else:
#             time.sleep(1)
#             print("0" + str(minute) + ":0" + str(second))

# total = 0
# for i in range(5):
#     new_number = int(input( "Enter a number: "))
#     if new_number == 0:
#         total += 1
# print("You entered a total of", total, "zeros")

# # 1. Print "Hi" 10 times.
# for i in range(1, 11):
#     print("Hi")

# # 2. Print "Hello" 5 times and 'There' once
# for i in range(1, 6):
#     print("Hello")
# print("There")

# # 3. Print "Hello" and "There" 5 times, on different lines
# for i in range(1, 6):
#     print("Hello" + "\n" + "There")

# # 4. Print the numbers 0 to 9
# for i in range(0, 10):
#     print(i)

# # 5. Two ways to print the numbers 1 to 10
# for i in range(1, 11):
#     print(i)

# for i in range(0, 10):
#     i += 1
#     print(i)

# # 6. Two ways to print the even numbers 2 to 10
# for i in range(2, 11, 2):
#     print(i)

# for i in range(2, 11):
#     if i % 2 == 0:
#         print(i)

# # 7. Count down from 10 down to 1 (not zero)
# for i in range(10, 0, -1):
#     print(i)

# import time
# def countdown(n):
#     if n == 1:
#         time.sleep(1)
#         print(n)
#         time.sleep(1)
#         print("Blastoff!")
#         time.sleep(1)
#     else:
#         time.sleep(1)
#         print(n)
#         countdown(n-1)
    
# countdown(10)  

# # 8. Print numbers out of a list
# new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in new_list:
#     print(i)

# # or
# hello_ = ""
# for i in ["H", "e", "l", "l", "o"]:
#     print(i)
#     hello_ += i
# print(hello_)

# a = 0
# for i in range(10):
#     a = a + 1
#     for j in range(10):
#         a = a + 1
# print(a)

# i = 1
# while i <= 2 ** 32:
#     print(i)
#     i *= 2


# i = 10
# while i != 0:
#     print(i)
#     i -= 1

# i = 1
# while i < 10:
#     print(i)
#     i += 1

# quit = True

# while quit:
#     user_input = input("Do you want to quit? ")
#     if user_input == "y" or user_input == "Y":
#         quit = False

# done = False
# while not done:
#     quit = input("Do you want to quit? ")
#     if quit == "y":
#         done = True
#     else:
#         attack = input("Does your elf attack the dragon? ")
#         if attack == "y":
#             print("Bad choice, you died.")
#             done = True

# # 1
# i = 0
# while i < 10:
#     print(i)
#     i += 1

# 2 Question
# 1, 2, 4, 8, 16...

# # 3
# question = True
# while question:
#     user_input = input("Do you want to continue? Yes/No: ").lower()
#     if user_input == "no":
#         question = False

# # 4
# # Fix
# # i = 10
# # while i == 0:
# #     print(i)
# #     i -= 1

# i = 10
# while i != 0:
#     print(i)
#     i -= 1

# Fix
# i = 1
# while i < 10:
#     print(i)

# i = 1
# while i < 10:
#     print(i)
#     i += 1
# #              0        1         2       3           
# num_list = ["Alec", "Keegan", "Bryan", "Carol"]
# print(num_list[0])

#import random

# for i in range(20):
#     rand_num = random.randrange(5)
#     if rand_num == 0:
#         print("DRAGON!!!!")
#     else:
#         print("No dragon")

# Number guesser

# """
# This is a sample text-only game that demonstrates the use of functions.
# The game is called "Mudball" and the players take turns lobbing mudballs
# at each other until someone gets hit.
# """

# a = print("Hello world")

# import math
# import random


# def print_instructions():
#     """ This function prints the instructions. """

#     # You can use the triple-quote string in a print statement to
#     # print multiple lines.
#     print("""
# Welcome to Mudball! The idea is to hit the other player with a mudball.
# Enter your angle (in degrees) and the amount of PSI to charge your gun
# with.
#         """)


# def calculate_distance(psi, angle_in_degrees):
#     """ Calculate the distance the mudball flies. """
#     angle_in_radians = math.radians(angle_in_degrees)
#     distance = .5 * psi ** 2 * math.sin(angle_in_radians) * math.cos(angle_in_radians)
#     return distance


# def get_user_input(name):
#     """ Get the user input for psi and angle. Return as a list of two
#     numbers. """
#     # Later on in the 'exceptions' chapter, we will learn how to modify
#     # this code to not crash the game if the user types in something that
#     # isn't a valid number.
#     psi = float(input(name + " charge the gun with how many psi? "))
#     angle = float(input(name + " move the gun at what angle? "))
#     return psi, angle


# def get_player_names():
#     """ Get a list of names from the players. """
#     print("Enter player names. Enter as many players as you like.")
#     done = False
#     players = []
#     while not done:
#         player = input("Enter player (hit enter to quit): ")
#         if len(player) > 0:
#             players.append(player)
#         else:
#             done = True

#     print()
#     return players


# def process_player_turn(player_name, distance_apart):
#     """ The code runs the turn for each player.
#     If it returns False, keep going with the game.
#     If it returns True, someone has won, so stop. """
#     psi, angle = get_user_input(player_name)

#     distance_mudball = calculate_distance(psi, angle)
#     difference = distance_mudball - distance_apart

#     # By looking ahead to the chapter on print formatting, these
#     # lines could be made to print the numbers is a nice formatted
#     # manner.
#     if difference > 1:
#         print("You went", difference, "yards too far!")
#     elif difference < -1:
#         print("You were", difference * -1, "yards too short!")
#     else:
#         print("Hit!", player_name, "wins!")
#         return True

#     print()
#     return False


# def main():
#     """ Main program. """

#     # Get the game started.
#     print_instructions()
#     player_names = get_player_names()
#     distance_apart = random.randrange(50, 150)

#     # Keep looking until someone wins
#     done = False
#     while not done:
#         # Loop for each player
#         for player_name in player_names:
#             # Process their turn
#             done = process_player_turn(player_name, distance_apart)
#             # If someone won, 'break' out of this loop and end the game.
#             if done:
#                 break

# if __name__ == "__main__":
#     main()