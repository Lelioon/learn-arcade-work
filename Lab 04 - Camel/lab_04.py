"""Lab 04 - Camel Game"""

import random

def main():
    instructions = """
Welcome to Camel!
You have stolen a camel to make your way across the great Mobi desert.
The natives want their camel back and are chasing you down! Survive your
desert trek and out run the natives.
                   """
    
    print(instructions)

    # Variable setup
    miles_travelled = 0
    thirst = 0
    camel_tiredness = 0
    native_distance = -20
    drinks_in_canteen = 3

    done = False

    # Main game loop
    while not done:
        print("""
A. Drink from your canteen.
B. Ahead moderate speed.
C. Ahead full speed.
D. Stop for the night.
E. Status check.
Q. Quit.
            """)
        # Player options
        user_input = input("What is your choice: ").lower()
        if user_input == "q":
            done = True
        elif user_input == "e": # Check status
            print("You have travelled:", miles_travelled, "miles")
            print("You have", drinks_in_canteen, "drinks in the canteen")
            print("The natives are", miles_travelled - native_distance, "miles behind you")
        elif user_input == "d": # Rest for the night
            camel_tiredness = 0
            print("The camel is rested.")
            native_distance += random.randint(7, 14)
        elif user_input == "c": # Move ahead at full speed
            miles_travelled += random.randint(10, 20)
            native_distance += random.randint(7, 14)
            print("You have travelled:", miles_travelled, "miles")
            thirst += 1
            camel_tiredness += 1
            if random.randrange(20) == 8: # 1 in 20 chance of finding an oasis
                print("You have found an oasis! You are replenished")
                camel_tiredness = 0
                drinks_in_canteen = 3
                thirst = 0
        elif user_input == "a": # Give water to camel
            if drinks_in_canteen == 0:
                print("There are no more drinks left")
            else:
                drinks_in_canteen -= 1
                thirst = 0
                print("Your camels thirst is quenched")
        elif user_input == "b": # Move ahead at moderate speed
            miles_travelled += random.randint(5, 12)
            native_distance += random.randint(7, 14)
            thirst += 1
            camel_tiredness += 1
            print("You have travelled:", miles_travelled, "miles")
            if random.randrange(20) == 8: # 1 in 20 chance of finding an oasis
                print("You have found and oasis! You are replenished")
                camel_tiredness = 0
                drinks_in_canteen = 3
                thirst = 0
        
        # Game checks
        # If you have crossed the desert and your camel isn't dead, you win
        if miles_travelled >= 200 and thirst < 7 and camel_tiredness < 9:
            print("You have made it accross the desert. You win!")
            done = True
            break
        
        # If thirst reaches a certain level, either warn the player or tell the player the camel has died and they lose.
        if thirst > 4 and thirst <= 6:
            print("Your camel is thirsty")
        elif thirst > 6:
            print("Your camel died of thirst. Game over")
            done = True
            break
        
        # If camel_tiredness reaches a certain level, either warn the player or tell the player the camel has died and they lose.
        if camel_tiredness > 5 and camel_tiredness <= 8:
            print("Your camel is getting tired")
        elif camel_tiredness > 8:
            print("Your camel has died of exhaustion. Game over")
            done = True
            break
        
        # If the natives have caught up you lose
        if native_distance == miles_travelled:
            print("The natives have caught up. Game over")
            done = True
            break
        elif miles_travelled - native_distance < 15:
            print("The natvies are getting close!")
        
          
main()


# MODULE PRACTICE
# # # a = int(input("Value of A: "))
# # # b = int(input("Value of B: "))

# # # if a < b:
# # #     print("A is less than B")
# # # elif a > b:
# # #     print("B is less than A")
# # # elif a == b:
# # #     print("A and B are equal")

# # # c = a == b

# # # print(c)


# # temperature = input("What is the temperature in Fahrenheit? ")
# # print("You said the temperature was " + temperature + " degrees.")
# # print(int(temperature)*15)

# # user_name = input("What is your name? ")
# # if user_name == "Paul":
# #     print("You have a nice name.")
# # else:
# #     print("Your name is ok.")

# # Sample Python/Pygame Programs
# # Simpson College Computer Science
# # http://programarcadegames.com/
# # http://simpson.edu/computer-science/

# # Explanation video: http://youtu.be/pDpNSck2aXQ

# # Variables used in the example if statements
# a = 4
# b = 5
# c = 6

# # Basic comparisons
# if a < b:
#     print("a is less than b")

# if a > b:
#     print("a is greater than than b")

# if a <= b:
#     print("a is less than or equal to b")

# if a >= b:
#     print("a is greater than or equal to b")

# # NOTE: It is very easy to mix when to use == and =.
# # Use == if you are asking if they are equal, use =
# # if you are assigning a value.
# if a == b:
#     print("a is equal to b")

# # Not equal
# if a != b:
#     print("a and b are not equal")

# # And
# if a < b and a < c:
#     print("a is less than b and c")

# # Non-exclusive or
# if a < b or a < c:
#     print("a is less than either a or b (or both)")


# # Boolean data type. This is legal!
# a = True
# if a:
#     print("a is true")

# if not a:
#     print("a is false")

# a = True
# b = False

# if a and b:
#     print("a and b are both true")

# a = 3
# b = 3
# c = a == b
# print(c)

# # These are also legal and will trigger as being true because
# # the values are not zero:
# if 1:
#     print("1")
# if "A":
#     print("A")

# # This will not trigger as true because it is zero.
# if 0:
#     print("Zero")

# # Comparing variables to multiple values.
# # The first if statement appears to work, but it will always
# # trigger as true even if the variable a is not equal to b.
# # This is because "b" by itself is considered true.
# a = "c"
# if a == "B" or "b":
#     print("a is equal to b. Maybe.")

# # This is the proper way to do the if statement.
# if a == "B" or a == "b":
#     print("a is equal to b.")

# # Example 1: If statement
# temperature = int(input("What is the temperature in Fahrenheit? "))
# if temperature > 90:
#     print("It is hot outside")
# print("Done")

# # Example 2: Else statement
# temperature = int(input("What is the temperature in Fahrenheit? "))
# if temperature > 90:
#     print("It is hot outside")
# else:
#     print("It is not hot outside")
# print("Done")

# # Example 3: Else if statement
# temperature = int(input("What is the temperature in Fahrenheit? "))
# if temperature > 90:
#     print("It is hot outside")
# elif temperature < 30:
#     print("It is cold outside")
# else:
#     print("It is not hot outside")
# print("Done")

# # Example 4: Ordering of statements
# # Something with this is wrong. What?
# temperature = int(input("What is the temperature in Fahrenheit? "))
# if temperature > 90:
#     print("It is hot outside")
# elif temperature > 110:
#     print("Oh man, you could fry eggs on the pavement!")
# elif temperature < 30:
#     print("It is cold outside")
# else:
#     print("It is ok outside")
# print("Done")

# # Comparisons using string/text
# # The input statement will ask the user for input and put it in user_name.
# user_name = input("What is your name? ")
# if user_name == "Paul":
#     print("You have a nice name.")
# else:
#     print("Your name is ok.")