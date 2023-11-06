"""
Sprite Move With Walls

Simple program to show basic sprite usage.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_walls
"""

import arcade
import random

SPRITE_SCALING = 0.5
COIN_SCALING = 0.2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Walls Example"

MOVEMENT_SPEED = 5
COIN_COUNT = 50


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Sprite lists
        self.coin_list = None
        self.wall_list = None
        self.player_list = None
        self.coin_list = None
        self.background_music  = None

        # Set up the player
        self.player_sprite = None
        self.physics_engine = None

        self.score = 0
        self.coin_sound = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.coin_sound = arcade.load_sound("collectcoin-6075.mp3")
        #self.background_music = arcade.load_sound("1. All The World Is Mad.mp3")
        # Set up the player
        self.player_sprite = arcade.Sprite("character.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)


        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.wall_list)

        for x in range(48, 768, 64):
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 460

            self.wall_list.append(wall)
        
        for x in range(80, 384, 64):
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 230

            self.wall_list.append(wall)
        
        for y in range(80, 384, 64):
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING)
            wall.center_x = 600
            wall.center_y = y

            self.wall_list.append(wall)

        for coins in range(COIN_COUNT):
            coin = arcade.Sprite("coin_01.png", COIN_SCALING)

            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            self.coin_list.append(coin)
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()

        #arcade.play_sound(self.background_music)

        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.BLACK, 12)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()
    
    def update(self, delta_time):
        self.coin_list.update()
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        for coin in hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.coin_sound)



def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()