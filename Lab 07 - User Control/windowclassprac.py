import arcade

""" Animation for ball to bounce on the edges"""

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Ball:

    def __init__(self, position_x, position_y, change_x, change_y, radius, color): # Ball(150, 250, -3, -1, 15, arcade.color.FOREST_GREEN)
        """Constructor"""

        # Parameters
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color
    
    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color) 

    def update(self):
        """Code to control the balls movement"""

        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hits the side of the screen
        if self.position_x < self.radius:
            self.change_x *= -1
        
        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1

        if self.position_y < self.radius:
            self.change_y *= -1
        
        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1

class MyGame(arcade.Window):
    """Window class"""

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create a list for the balls
        self.ball_list = []

        # Add three balls to the list
        ball = Ball(50, 50, 3, 3, 15, arcade.color.AUBURN)
        self.ball_list.append(ball)

        ball = Ball(100, 150, 2, 3, 15, arcade.color.PURPLE_MOUNTAIN_MAJESTY)
        self.ball_list.append(ball)

        ball = Ball(150, 250, -3, -1, 15, arcade.color.FOREST_GREEN)
        self.ball_list.append(ball)

    def on_draw(self):
        """Called whenever we need to draw the window"""
        arcade.start_render()
        for ball in self.ball_list:
            ball.draw()


    
    def update(self, delta_time):
        """ Called to update our objects. Happens approximately 60 times per second."""
        for ball in self.ball_list:
            ball.update()

        

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Animation Drawing Example")

    arcade.run()

main()









# Simple Ball Animation
# class MyGame(arcade.Window):
#     def __init__(self, width, height, title):
#         super().__init__(width, height, title)

#         arcade.set_background_color(arcade.color.ASH_GREY)

#         self.ball_x = 50
#         self.ball_y = 50
    
#     def on_draw(self):
#         arcade.start_render()

#         arcade.draw_circle_filled(self.ball_x, self.ball_y, 15, arcade.color.AUBURN)
    
#     def update(self, delta_time):
#         self.ball_x += 10
#         self.ball_y += 10
    

# def main():
#     window = MyGame(640, 480, "Drawing Examples")

#     arcade.run()

# main()

