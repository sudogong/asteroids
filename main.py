import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print(f"Player: {player}")

    # (Intended Infinite) Rendering Loop
    while True:
        log_state()
        for event in pygame.event.get():
            # Make the close button work
            if event.type == pygame.QUIT:
                print("INFO - User successfully stopped the program")
                return
            
        screen.fill("black")

        #Add a player
        player.draw(screen=screen)

        # Update player position on screen on each frame
        player.update(dt=dt)

        # Render next screen
        dt = clock.tick(60) / 1000
        pygame.display.flip()
    

if __name__ == "__main__":
    main()
