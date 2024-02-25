"""This module defines the Ship class and its methods."""

from utils.laser import Laser


WIDTH, HEIGHT = 750, 750


class Ship:
    """Construct a ship that can shoot lasers with a cool-down and has position coordinates"""

    SHOOT_COOLDOWN = 30

    def __init__(self, x, y, health=100):
        """Ship constructor"""
        self.x = x
        self.y = y
        self.health = health
        self.ship_image = None
        self.laser_image = None
        self.lasers = []
        self.cool_down_counter = 0

    def spawn(self, window):
        """Add a new Ship Object."""
        window.blit(self.ship_image, (self.x, self.y))
        for laser in self.lasers:
            laser.spawn(window)

    def move_lasers(self, velocity, object):
        """Update laser position and remove off-screen lasers"""
        self.shoot_cooldown()
        for laser in self.lasers:
            laser.move(velocity)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(object):
                object.health -= 10
                self.lasers.remove(laser)

    def shoot_cooldown(self):
        """A timer that determines whether a laser can be shot or not."""
        if self.cool_down_counter >= self.SHOOT_COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        """Instantiates a laser object with cool-down timer."""

        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_image)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_width(self):
        """returns object width."""
        return self.ship_image.get_width()

    def get_height(self):
        """returns object height."""
        return self.ship_image.get_height()
