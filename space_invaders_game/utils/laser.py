"""This module defines the Laser class and its methods."""

import pygame


class Laser:
    """A laser can spawn, move and tell if it is offscreen or colliding."""

    def __init__(self, x, y, image):
        """Initializes a laser."""
        self.x = x
        self.y = y
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)

    def spawn(self, window):
        """Spawns the laser to the window."""
        window.blit(self.image, (self.x, self.y))

    def move(self, velocity):
        """Update the laser's position."""
        self.y += velocity

    def off_screen(self, height):
        """Returns True if the laser is off the screen, False otherwise."""
        return not (self.y <= height and self.y >= 0)

    def collision(self, object):
        """Returns True if there is a collision, False otherwise."""
        return collide(self, object)


def collide(object1, object2):
    """Returns True if there is a collision, False otherwise."""
    offset_x = object2.x - object1.x
    offset_y = object2.y - object1.y
    return object1.mask.overlap(object2.mask, (offset_x, offset_y)) is not None
