import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.math.Vector2(x,y)
        self.radius = radius
    rotation = 0
    random_angle = random.uniform(20,50)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_vector_1 = self.velocity.rotate(self.random_angle)
        new_vector_2 = self.velocity.rotate(-self.random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = new_vector_1
        asteroid_2.velocity = new_vector_2

    
    def rotate(self, random_angle):
        self.rotation += random_angle