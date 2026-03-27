from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, VELOCITY_SCALING_FACTOR
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Los grandes splitean en 2 medianos y los medianos en 2 pequenios
        # Los nuevos salen en direcciones random y mas rapido
        log_event("asteroid_split")
        random_angle = random.uniform(20,50)
        vector1_velocity = self.velocity.rotate(random_angle)
        vector2_velocity = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        ast1 = Asteroid(self.position[0], self.position[1], new_radius)
        ast2 = Asteroid(self.position[0], self.position[1], new_radius)

        ast1.velocity = vector1_velocity * VELOCITY_SCALING_FACTOR
        ast2.velocity = vector2_velocity * VELOCITY_SCALING_FACTOR
        