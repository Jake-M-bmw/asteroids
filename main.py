
import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
	pygame.init()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroid = pygame.sprite.Group()
	shot = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	AsteroidField.containers = (updatable,)
	Asteroid.containers = (asteroid, updatable, drawable)
	Shot.containers = (shot, updatable, drawable)

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()

	while True:
		screen.fill("black")
		updatable.update(dt)
		for sprite in drawable:
			sprite.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000
		for ast in asteroid:
			if player.collision(ast):
				print("Game Over!")
				sys.exit()
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return



if __name__ == "__main__":
    main()


