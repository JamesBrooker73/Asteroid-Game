import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
  def _init_(self, x, y, radius):
    super()._init_(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt
