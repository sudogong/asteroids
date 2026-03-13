import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroid_field import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Defining groups (player vs asteroids)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add objects to corresponding groups
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()

    # Create an instance of a player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    # (Intended Infinite) Rendering Loop
    while True:
        log_state()
        for event in pygame.event.get():
            # Make the close button work
            if event.type == pygame.QUIT:
                print("INFO - User successfully stopped the program")
                return
            
        screen.fill("black")

        #Add drawable objects (players, asteroids)
        for item in drawable:
            item.draw(screen=screen)            

        # Update objects position on screen
        updatable.update(dt=dt)

        # Check for collisions
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()


        # Render next frame
        dt = clock.tick(60) / 1000
        pygame.display.flip()
    

if __name__ == "__main__":
    main()
