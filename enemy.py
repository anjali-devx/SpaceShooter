import pygame
import random
from settings import *

class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(
            random.randint(0, WIDTH - ENEMY_WIDTH),
            -ENEMY_HEIGHT,
            ENEMY_WIDTH,
            ENEMY_HEIGHT
        )

    def move(self):
        self.rect.y += ENEMY_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.rect)

    def is_off_screen(self):
        return self.rect.top > HEIGHT