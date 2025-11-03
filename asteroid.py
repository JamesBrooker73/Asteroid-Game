import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
  def _init_(self, x, y, radius):
    super()._init_(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return

    random_angle = random.uniform(20, 50)

    a = self.velocity.rotate(random_angle)
    b = self.velocity.rotate(random_angle)

    new_radius = self.radius - ASTEROID_MIN_RADIUS
    asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
    asteroid_1.velocity = a * 1.2
    asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
    asteroid_2.velocity = b