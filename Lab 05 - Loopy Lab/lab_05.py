
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

import random

# for i in range(20):
#     rand_num = random.randrange(5)
#     if rand_num == 0:
#         print("DRAGON!!!!")
#     else:
#         print("No dragon")

# Number guesser

