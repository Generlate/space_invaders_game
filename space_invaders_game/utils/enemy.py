"""This module defines the Enemy class and its methods."""

import pygame
import os
from utils.ship import Ship
from utils.laser import Laser


RED_SPACE_SHIP = pygame.image.load(
    os.path.join("assets", "red_space_ship.png")
)
GREEN_SPACE_SHIP = pygame.image.load(
    os.path.join("assets", "green_space_ship.png")
)
BLUE_SPACE_SHIP = pygame.image.load(
    os.path.join("assets", "blue_space_ship.png")
)

RED_LASER = pygame.image.load(os.path.join("assets", "red_laser.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "green_laser.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "blue_laser.png"))


class Enemy(Ship):
    """Enemies can spawn as either red, green or blue. They can move and shoot."""

    color_map = {
        "red": (RED_SPACE_SHIP, RED_LASER),
        "green": (GREEN_SPACE_SHIP, GREEN_LASER),
        "blue": (BLUE_SPACE_SHIP, BLUE_LASER),
    }

    def __init__(self, x, y, color, health=100):
        """Initialize enemies of different colors."""
        super().__init__(x, y, health)
        self.ship_image, self.laser_image = self.color_map[color]
        self.mask = pygame.mask.from_surface(self.ship_image)

    def move(self, velocity):
        """Update the enemy's position."""
        self.y += velocity

        def shoot(self):
            if self.cool_down_counter == 0:
                laser = Laser(self.x - 18, self.y, self.laser_image)
                self.lasers.append(laser)
                self.cool_down_counter = 1
