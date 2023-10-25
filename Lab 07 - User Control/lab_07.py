""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5

class Square:
    def __init__(self, position_x, position_y, change_x, change_y, swidth, sheight, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.swidth = swidth
        self.sheight = sheight
        self.color = color

        self.hit_sound = arcade.load_sound("laser.wav")

    def draw(self):
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.swidth, self.sheight, self.color)
        arcade.draw_rectangle_filled(0, 0, SCREEN_WIDTH*2, 150, arcade.color.AERO_BLUE)
        arcade.draw_rectangle_filled(640, 640, SCREEN_WIDTH*2, 150, arcade.color.AFRICAN_VIOLET)
    
    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y

        if self.position_x < (self.swidth/2):
            self.position_x = self.swidth/2
            arcade.play_sound(self.hit_sound)

        if self.position_x > SCREEN_WIDTH - (self.swidth/2):
            self.position_x = SCREEN_WIDTH - (self.swidth/2)
            arcade.play_sound(self.hit_sound)

        if self.position_y < (self.sheight/2):
            self.position_y = self.sheight/2
            arcade.play_sound(self.hit_sound)

        if self.position_y > SCREEN_HEIGHT - (self.sheight/2):
            self.position_y = SCREEN_HEIGHT - (self.sheight/2)
            arcade.play_sound(self.hit_sound)

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        arcade.set_background_color(arcade.color.GO_GREEN)

        self.square = Square(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 0, 0, 100, 100, arcade.color.WHEAT)

    def on_draw(self):
        arcade.start_render()
        self.square.draw()
        
    def update(self, delta_time):
        self.square.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.square.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.square.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.square.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.square.change_y = -MOVEMENT_SPEED
    
    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.square.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.square.change_y = 0
        

def main():
    window = MyGame()
    arcade.run()


main()