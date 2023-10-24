# class Dog():
#     def __init__(self):
#         self.age = 0
#         self.name = ""
#         self.weight = 0

#     def bark(self):
#         print(self.name,"says woof!")

# my_dog = Dog()

# my_dog.name = "Spot"
# my_dog.weight = 20
# my_dog.age = 3

# my_dog.bark()
# import arcade

# class Ball():
#     def __init__(self):
#         # --Class attributes--
#         # Ball position
#         self.x = 0
#         self.y = 0

#         # Balls vector
#         self.change_x = 0
#         self.change_y = 0

#         # Ball size
#         self.size = 10

#         # Ball colour
#         self.color = [255,255,255]

#         # --Class methods
#         def move(self):
#             self.x += self.change_x
#             self.y += self.change_y
        
#         def draw(self):
#             arcade.draw_circle_filled(self.x, self.y, self.size, self.color)

# the_ball = Ball()
# the_ball.x = 100
# the_ball.y = 100
# the_ball.change_x = 2
# the_ball.change_y = 1
# the_ball.color = [255, 0, 0]

# def main():
#     done = False
#     while not done:
#         the_ball.move()
#         the_ball.draw()

# main()

# class Person():
#     def __init__(self):
#         self.name = ""
#         self.money = 0


# def main():
#     bob = Person()
#     bob.name = "Bob"
#     bob.money = 100

#     nancy = bob
#     nancy.name = "Nancy"

#     print(bob.name, "has", bob.money, "dollars.")
#     print(nancy.name, "has", nancy.money, "dollars.")


# main()

# def give_money1(money):
#     money += 100


# class Person():
#     def __init__(self):
#         self.name = ""
#         self.money = 0


# def main():
#     bob = Person()
#     bob.name = "Bob"
#     bob.money = 100


#     give_money1(bob.money)
#     print(bob.money)

# main()

# a = [1, 2, 3]
# b = a

# print(a)
# print(b)

# a.append(4)

# print(a)
# print(b)

# class Cat:
#     def __init__(self):
#         self.name = ""
#         self.color = [255, 255, 255]
#         self.weight = 0
    
#     def meow(self):
#         print("Meow")

# cat = Cat()
# cat.name = "Charlie"
# cat.color = [100, 100, 100]
# cat.weight = 2
# cat.meow()


# class Monster:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
    
#     def decrease_health(self, decrease):
#         self.health -= decrease
#         print("Health decreased by", decrease, "points")
#         print("Health is now", self.health, "hit points")
#         if self.health == 0:
#             print("Your monster has died")

# mon1 = Monster("Scruffy", 100)
# mon1.decrease_health(50)
# mon1.decrease_health(50)

# class Star:
#     def __init__(self):
#         print("A new star is born")

# star1 = Star()

# class Monster:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health

class Boat:
    def __init__(self):
        self.tonnage = 0
        self.name = ""
        self.is_docked = True

    def dock(self):
        if self.is_docked:
            print(self.name, "is already docked")
        else:
            self.is_docked = True
            print("Docking")
            
    def undock(self):
        if not self.is_docked:
            print("You aren't docked")
        else:
            self.is_docked = False
            print("Undocking")

class Submarine(Boat):
    # def __init__(self):
    #     self.is_submerged = True

    def submerge(self):
        
        print("You are already submerged")
        
b = Boat()
b.name = "SS Unsinkable"
s = Submarine()
s.name = "SS Always Sinkable"

b.dock()
b.undock()
b.undock()
b.dock()
b.dock()
s.submerge()
s.dock()


