"""
  Background Music Example
  
  If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.background_music
"""
import arcade
import time
 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 300
SCREEN_TITLE = "Starting Template Simple"
MUSIC_VOLUME = 0.5
 
 
class MyGame(arcade.Window):
    """ Main application class. """
 
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
 
        arcade.set_background_color(arcade.color.WHITE)
 
        # Variables used to manage our music. See setup() for giving them
        # values.
        self.music_list = []
        self.current_song_index = 0
        self.current_player = None
        self.music = None
 
    def advance_song(self):
        """ Advance our pointer to the next song. This does NOT start the song. """
        self.current_song_index += 1
        if self.current_song_index >= len(self.music_list):
            self.current_song_index = 0
        print(f"Advancing song to {self.current_song_index}.")
 
    def play_song(self):
        """ Play the song. """
        # Stop what is currently playing.
        if self.music:
            self.music.stop()
 
        # Play the next song
        print(f"Playing {self.music_list[self.current_song_index]}")
        self.music = arcade.Sound(self.music_list[self.current_song_index], streaming=True)
        self.current_player = self.music.play(MUSIC_VOLUME)
        # This is a quick delay. If we don't do this, our elapsed time is 0.0
        # and on_update will think the music is over and advance us to the next
        # song before starting this one.
        time.sleep(0.03)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """

        # List of music
        self.music_list = [":resources:music/funkyrobot.mp3", ":resources:music/1918.mp3"]
        # Array index of what to play
        self.current_song_index = 0
        # Play the song
        self.play_song()

    def on_draw(self):
        """ Render the screen. """

        arcade.start_render()

        position = self.music.get_stream_position(self.current_player)
        length = self.music.get_length()

        size = 20
        margin = size * .5

        # Print time elapsed and total
        y = SCREEN_HEIGHT - (size + margin)
        text = f"{int(position) // 60}:{int(position) % 60:02} of {int(length) // 60}:{int(length) % 60:02}"
        arcade.draw_text(text, 0, y, arcade.csscolor.BLACK, size)

        # Print current song
        y -= size + margin
        text = f"Currently playing: {self.music_list[self.current_song_index]}"
        arcade.draw_text(text, 0, y, arcade.csscolor.BLACK, size)

    def on_update(self, dt):

        position = self.music.get_stream_position(self.current_player)

        # The position pointer is reset to 0 right after we finish the song.
        # This makes it very difficult to figure out if we just started playing
        # or if we are doing playing.
        if position == 0.0:
            self.advance_song()
            self.play_song()


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

# """ Sprite Sample Program """

# import arcade

# # Constants
# SPRITE_SCALING_BOX = 0.5
# SPRITE_SCALING_PLAYER = 0.5

# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600

# MOVEMENT_SPEED = 5

# class MyGame(arcade.Window):
#     """ This class represents the main window of the game"""

#     def __init__(self):
#         """ Initializer """
#         # Call the parent class initializer
#         super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite with walls example")

#         # Sprite lists
#         self.player_list = None
#         self.wall_list = None

#         # Set up the player
#         self.player_sprite = None

#         # This variable holds our simple "physics engine"
#         self.physics_engine = None

#         # Create the cameras. One for the GUI, one for the sprites
#         # We scroll the "sprite world" but not the GUI
#         self.camera_for_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
#         self.camera_for_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

#     def setup(self):

#         # Sprite lists
#         self.player_list = arcade.SpriteList()
#         self.wall_list = arcade.SpriteList()

#         # Reset score
#         self.score = 0

#         # Create Player
#         self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
#         self.player_sprite.center_x = 50
#         self.player_sprite.center_y = 64
#         self.player_list.append(self.player_sprite)

#         # Manually create and position a box at 300, 200
#         wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
#         wall.center_x = 300
#         wall.center_y = 200
#         self.wall_list.append(wall)

#         # Manually create and position a box at 364, 200
#         wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
#         wall.center_x = 364
#         wall.center_y = 200
#         self.wall_list.append(wall)

#         # Place boxes using a loop
#         for x in range(173, 650, 64):
#             wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
#             wall.center_x = x
#             wall.center_y = 350
#             self.wall_list.append(wall)
        
#         # List of co-ordinates used to make a list
#         coordinate_list = [[400, 500],
#                            [470, 500],
#                            [400, 570],
#                            [470, 570]]
        
#         # Loop through coordinates
#         for coordinate in coordinate_list:
#             wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
#             wall.center_x = coordinate[0]
#             wall.center_y = coordinate[1]
#             self.wall_list.append(wall)

#         # This variable holds our simple "physics engine"
#         self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)


#         # Set the background color
#         arcade.set_background_color(arcade.color.AMAZON)

#     def on_draw(self):
#         arcade.start_render()

#         # Select the scrolled camera for our sprites
#         self.camera_for_sprites.use()
        
#         # Draw the sprites
#         self.wall_list.draw()
#         self.player_list.draw()

#         # Select the (unscrolled) camera for our GUI
#         self.camera_for_gui.use()
#         arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 24)
    
    
#     def on_update(self, delta_time):
#         """ Movement and game logic """

#         # Call update on all sprites (The sprites don't do much in this example though)
#         self.physics_engine.update()

#         # Scroll the screen to the player
#         #self.scroll_to_player()

#         # Scroll the window to the player.

#         # If CAMERA_SPEED is 1, the camera wil; immediately move to the desired position.
#         # Anything between 0 and 1 will have the camera move to the location with a smoother pan
#         CAMERA_SPEED = 1
#         lower_left_corner = (self.player_sprite.center_x - self.width / 2,
#                              self.player_sprite.center_y - self.height / 2)
#         self.camera_for_sprites.move_to(lower_left_corner, CAMERA_SPEED)

#     def on_key_press(self, key, modifiers):
#         """ Called whenever a key is pressed. """
        
#         if key == arcade.key.UP:
#             self.player_sprite.change_y = MOVEMENT_SPEED
#         elif key == arcade.key.DOWN:
#             self.player_sprite.change_y = -MOVEMENT_SPEED
#         elif key == arcade.key.LEFT:
#             self.player_sprite.change_x = -MOVEMENT_SPEED
#         elif key == arcade.key.RIGHT:
#             self.player_sprite.change_x = MOVEMENT_SPEED

#     def on_key_release(self, key, modifiers):
#         """ Called when the user releases a key. """

#         if key == arcade.key.UP or key == arcade.key.DOWN:
#             self.player_sprite.change_y = 0
#         elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
#             self.player_sprite.change_x = 0

#     # def update(self, delta_time):
#     #     self.physics_engine.update()

# def main():
#     window = MyGame()
#     window.setup()
#     arcade.run()

# if __name__ == "__main__":
#     main()

    
