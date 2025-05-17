from circleshape import CircleShape
import pygame
from constants import PLAYER_RADIUS  # Import from your constants file
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOOT_SPEED
from constants import SHOT_RADIUS
from constants import PLAYER_SHOOT_COOLDOWN
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        # Call parent constructor with x, y, and PLAYER_RADIUS
        super().__init__(x, y, PLAYER_RADIUS)
        # Set rotation as an instance attribute
        self.rotation = 0
        self.timer = 0

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
        if keys[pygame.K_SPACE]:
            shot = self.shoot()
            if shot is not None:
                self.shots_group.add(shot)
        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        print(f"timer: {self.timer}")
        if self.timer > 0:
            self.timer -= dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
    # First check if we can shoot
        if self.timer > 0:
            return None  # Cannot shoot, return None
        
        # If we get here, we can shoot
        # Set cooldown timer
        self.timer = PLAYER_SHOOT_COOLDOWN
        
        # Create and return the shot
        shot = Shot(self.position, SHOT_RADIUS)
        shot_direction = pygame.Vector2(0, 1)
        shot_direction = shot_direction.rotate(self.rotation)
        shot.velocity = shot_direction * PLAYER_SHOOT_SPEED
        return shot