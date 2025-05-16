from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, position, radius):
        # CircleShape expects (x, y, radius)
        super().__init__(position.x, position.y, radius)
        self.velocity = pygame.Vector2(0, 0)
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 5)

    def update(self, dt):
        self.position += self.velocity * dt