import sys

import pygame

from asteroidfield import *
from constants import *
from player import *
from asteroid import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = clock.tick(60) / 1000
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = [shots,updatable,drawable]
    Player.containers = [updatable, drawable]
    Asteroid.containers = [asteroids, updatable, drawable]
    AsteroidField.containers = [updatable,]
    field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        screen.fill("black")
        updatable.update(dt)
        for x in drawable:
            x.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for a in asteroids:
            if a.collide(player):
                print("Game over!")
                sys.exit()

        for a in asteroids:
            for s in shots:
                if s.collide(a):
                    s.kill()
                    a.split()




        clock.tick(60)




if __name__ == "__main__":
    main()
