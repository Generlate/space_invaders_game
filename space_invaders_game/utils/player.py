import pygame
import os
from utils.ship import Ship

WIDTH, HEIGHT = 750, 750

YELLOW_SPACE_SHIP = pygame.image.load(
    os.path.join("assets", "yellow_space_ship.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "yellow_laser.png"))


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_image = YELLOW_SPACE_SHIP
        self.laser_image = YELLOW_LASER
        # Create a mask for collision detection using the ship image
        self.mask = pygame.mask.from_surface(self.ship_image)
        self.max_health = health

    def move_lasers(self, velocity, objects):
        self.shoot_cooldown()
        for laser in self.lasers:
            laser.move(velocity)
            # Remove the laser from the list if it's off the screen
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for object in objects:
                    if laser.collision(object):
                        objects.remove(object)
                        if laser in self.lasers:
                            # Remove the laser from the list if it caused a collision
                            self.lasers.remove(laser)

    def spawn(self, window):
        # spawn the yellow ship on the window
        super().spawn(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y +
                         self.ship_image.get_height() + 10, self.ship_image.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.ship_image.get_height() +
                         10, self.ship_image.get_width() * (self.health/self.max_health), 10))
