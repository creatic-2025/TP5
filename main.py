"""
Créé par Dorian Bernaquez Girard, 3 Décembre 2025
Introduction à Arcade et ses fonctions
"""
from dataclasses import dataclass

import arcade
import random
import time

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640


@dataclass
class RGB:
    r: int
    g: int
    b: int


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.circles_list = None
        self.background_color = arcade.color.BUD_GREEN
        self.rgb_tuple = None
        self.x_coordinate = None
        self.y_coordinate = None

    def setup(self):
        self.circles_list = []
        for i in range(0, 20):
            circles = self.circles_list
            self.rgb_tuple = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.x_coordinate = random.randint(10, 470)
            self.y_coordinate = random.randint(10, 630)
            circle_variables = [self.rgb_tuple, self.x_coordinate, self.y_coordinate]
            circles.append(circle_variables)


    def on_draw(self):
        self.clear()
        arcade.draw_circle_filled()


def main():
    window = MyGame(640, 480, "Tutoriel Arcade")
    window.setup()
    window.on_draw()

    arcade.run()


main()
