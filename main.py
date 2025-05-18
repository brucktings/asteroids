import pygame
import sys
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    asteroidfield = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    Shot.containers = (shots_group, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    player.shots_group = shots_group
    asteroid_field = AsteroidField()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        updatable.update(dt)
        for entity in drawable:
            entity.draw(screen)
        shots_group.update(dt)
        for shot in shots_group:
            shot.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        #collision-check:
        for asteroid in asteroids:
            if player.collide(asteroid) == True:
                print("Game over!")
                pygame.quit()
                sys.exit()
        #killing asteroids:
        for asteroid in asteroids:
            for shot in shots_group:
                if asteroid.collide(shot) == True:
                    asteroid.split()
                    shot.kill()       

    pygame.quit()

if __name__ == "__main__":
    main()