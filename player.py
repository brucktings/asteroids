from circleshape import CircleShape
import pygame
from constants import PLAYER_RADIUS  # Import from your constants file
from constants import PLAYER_TURN_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        # Call parent constructor with x, y, and PLAYER_RADIUS
        super().__init__(x, y, PLAYER_RADIUS)
        # Set rotation as an instance attribute
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
        
    def draw(self, screen):
        # Override the draw method to draw a triangle
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)