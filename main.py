"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import time

import arcade
from dataclasses import dataclass
import random
from arcade.color import SAE, ALMOND, ALLOY_ORANGE, ALABAMA_CRIMSON, AERO_BLUE, ANTIQUE_WHITE, BALL_BLUE, \
    AUROMETALSAURUS, ATOMIC_TANGERINE

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
WINDOW_TITLE = "Arcade Test"

cercle_change_x = 3
cercle_change_y = 3
cercle_x = 0
cercle_y = 0


@dataclass
class RGB:
    r: int
    g: int
    b: int


class GameView(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.AMAZON
        self.color_list = None
        self.color_choice = None
        self.circles_list = None
        self.cercle_x_init = 0
        self.cercle_y_init = 0
        self.background_color = arcade.color.BURNT_UMBER
        self.rayon_cercle = 10
        self.reset()

    def reset(self):
        """Reset the game to the initial state."""
        # Do changes need to restart the game here if you want to support that
        self.circles_list = []
        self.color_list = [AERO_BLUE, ALABAMA_CRIMSON, ALLOY_ORANGE, ALMOND, SAE, ANTIQUE_WHITE, BALL_BLUE,
                           AUROMETALSAURUS, ATOMIC_TANGERINE]
        for i in range(0, 20):
            color_choice = random.choice(self.color_list)
            cercle_x_init = random.randint(10, 620)
            cercle_y_init = random.randint(10, 460)
            rayon_cercle = self.rayon_cercle
            self.circles_list.append([cercle_x_init, cercle_y_init, rayon_cercle, color_choice])

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        global cercle_change_y
        global cercle_change_x
        global cercle_x
        global cercle_y
        for circle in self.circles_list:
            circle[0] += cercle_change_x
            circle[1] += cercle_change_y
            cercle_x = circle[0]
            cercle_y = circle[1]
            print("Moved circles by (3,3)")
            if cercle_x < self.rayon_cercle:
                cercle_change_x *= -1
            if cercle_x > WINDOW_WIDTH - self.rayon_cercle:
                cercle_change_x *= -1
            if cercle_y < self.rayon_cercle:
                cercle_change_y *= -1
                print("checked")
            if cercle_y > WINDOW_HEIGHT - self.rayon_cercle:
                cercle_change_y *= -1

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()
        for circle in self.circles_list:
            arcade.draw_circle_filled(circle[0], circle[1], circle[2], circle[3])

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create and setup the GameView
    game = GameView()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()

# """
# Créé par Dorian Bernaquez Girard, 3 Décembre 2025
# Introduction à Arcade et ses fonctions
# """
# from dataclasses import dataclass
#
# import arcade
# import random
# import time
#
# from arcade.color import SAE, ALMOND, ALLOY_ORANGE, ALABAMA_CRIMSON, AERO_BLUE, ANTIQUE_WHITE, BALL_BLUE, \
#     AUROMETALSAURUS, ATOMIC_TANGERINE
#
# SCREEN_WIDTH = 480
# SCREEN_HEIGHT = 640
#
#
# @dataclass
# class RGB:
#     r: int
#     g: int
#     b: int
#
#
# class MyGame(arcade.Window):
#     def __init__(self, width, height, title):
#         super().__init__(width, height, title)
#         self.color_list = None
#         self.color_choice = None
#         self.color = None
#         self.circles_list = None
#         self.background_color = arcade.color.BURNT_UMBER
#         self.x_coordinate = None
#         self.y_coordinate = None
#
#     def setup(self):
#         self.circles_list = []
#         self.color_list = [AERO_BLUE, ALABAMA_CRIMSON, ALLOY_ORANGE, ALMOND, SAE, ANTIQUE_WHITE,
#                            ATOMIC_TANGERINE, AUROMETALSAURUS, BALL_BLUE]
#         for i in range(0, 20):
#             color_choice = random.choice(self.color_list)
#             x_coordinate = random.randint(10, 460)
#             y_coordinate = random.randint(10, 620)
#             self.circles_list.append([x_coordinate, y_coordinate, 10, color_choice])
#
#     def on_update(self):
#
#     def on_draw(self):
#         self.clear()
#         for circle in self.circles_list:
#             arcade.draw_circle_filled(circle[0], circle[1], circle[2], circle[3])
#
#
# def main():
#     window = MyGame(640, 480, "Tutoriel Arcade")
#     window.setup()
#     window.on_draw()
#
#     arcade.run()
#
#
# main()
