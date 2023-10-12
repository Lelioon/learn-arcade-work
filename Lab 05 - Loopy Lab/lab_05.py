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

def print_about_gum(repetitions):

    # Loop that many times
    for i in range(repetitions):
        print("I will not chew gum in class.")


def main():
    print_about_gum(10)


main()