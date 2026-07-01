import pygame
from settings import *

class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(
            x - BULLET_WIDTH // 2,
            y,
            BULLET_WIDTH,
            BULLET_HEIGHT
        )

    def move(self):
        self.rect.y -= BULLET_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)

    def is_off_screen(self):
        return self.rect.bottom < 0