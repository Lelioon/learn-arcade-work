# class Dog:
#     def __init__(self, new_name):
#         """Constructor"""
#         self.name = new_name
#         print("A new dog is born")

# def main():
#     dog1 = Dog("Scruffy")
#     print(f"The dog's name is {dog1.name}")
#     dog2 = Dog("Rover")
#     print(f"This dog's name is {dog2.name}")

# main()

# x = "pspspsps"
# plain_t = ""
# for i in x:
#     x = ord(i)
#     x = x - 1
#     x2 = chr(x)
#     plain_t = plain_t + x2

# print(plain_t)
# print(ord("a"))
# print(ord("b"))
# print(ord("a") + ord("b"))

# import mypy
# class Person:
#     def __init__(self):
#         self.name: str = "A"


# mary = Person()
# mary.name = "A"
# print(mary.name)

class Cat:
    population = 0

    def __init__(self, name):
        self.name = name
        Cat.population += 1

def main():
    cat1 = Cat("Pat")
    cat2 = Cat("Pepper")
    cat3 = Cat("Pouncy")
    cat4 = Cat("Trinity")

    Cat.population = 4
    cat3.population = 5
    print("The cat population is:", Cat.population)
    print("The cat population is:", cat1.population)
    print("The cat population is:", cat2.population)
    print("The cat population is:", cat3.population)

main()