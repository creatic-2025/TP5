"""
Créé par Dorian Bernaquez Girard, 3 Décembre 2025
Introduction à Arcade et ses fonctions
"""
from dataclasses import dataclass
from enum import Enum

import arcade
import random
import time

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


@dataclass
class RGB:
    r: int
    g: int
    b: int


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.RGB_liste = []
        self.background_color = 74, 103, 65
        self.rgb_tuple = [int, int, int]

    def random_choice(self):
        for i in range(0, 20):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            self.rgb_tuple = [r, g, b]

    def on_draw(self):
        self.clear()

        arcade.draw_circle_filled(300, 300, 10, (self.rgb_tuple))


def main():
    window = MyGame(640, 480, "Tutoriel Arcade")

    arcade.run()


run = MyGame(640, 480, "Tutoriel")
run.random_choice()
run.on_draw()

main()
