from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        global updatable
        global drawable
        global asteroids
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_angle = random.uniform(20, 50)
        small_one = pygame.math.Vector2.rotate(self.velocity, new_angle)
        small_two = pygame.math.Vector2.rotate(self.velocity, -new_angle)
        old_radius = self.radius
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_one.velocity = small_one * 1.2
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two.velocity = small_two * 1.2
