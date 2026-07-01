import pygame
from settings import *

class Player:
    def __init__(self):
        self.rect = pygame.Rect(
            WIDTH // 2 - PLAYER_WIDTH // 2,
            HEIGHT - PLAYER_HEIGHT - 20,
            PLAYER_WIDTH,
            PLAYER_HEIGHT
        )

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED

        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += PLAYER_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)