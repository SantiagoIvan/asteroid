from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius, SHOT_RADIUS)

    def update(self, dt):
        self.position += (self.velocity * dt)