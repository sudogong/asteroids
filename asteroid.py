import random
import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split") 
            angle = random.uniform(20.0,50.0)
            
            first_asteroid_vector = self.velocity.rotate(angle)
            second_asteroid_vector = self.velocity.rotate(-angle)
            
            radius = self.radius - ASTEROID_MIN_RADIUS
            
            first_asteroid = Asteroid(self.position.x, self.position.y, radius)
            second_asteroid = Asteroid(self.position.x, self.position.y, radius)
            
            first_asteroid.velocity = first_asteroid_vector * 1.2
            second_asteroid.velocity = second_asteroid_vector

            return first_asteroid, second_asteroid
