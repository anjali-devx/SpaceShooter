import pygame
import random

from settings import *
from player import Player
from bullet import Bullet
from enemy import Enemy

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

player = Player()
bullets = []
enemies = []
score = 0

running = True

while running:
    clock.tick(FPS)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(player.rect.centerx, player.rect.top))

    # Move player
    player.move()

    # Spawn enemies
    if random.randint(1, ENEMY_SPAWN_RATE) == 1:
        enemies.append(Enemy())

    # Move bullets
    for bullet in bullets[:]:
        bullet.move()
        if bullet.is_off_screen():
            bullets.remove(bullet)

    # Move enemies
    for enemy in enemies[:]:
        enemy.move()

        if enemy.is_off_screen():
            enemies.remove(enemy)
            continue

        # Game over if enemy hits player
        if enemy.rect.colliderect(player.rect):
            running = False

    # Bullet-enemy collisions
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.rect.colliderect(enemy.rect):
                if bullet in bullets:
                    bullets.remove(bullet)
                if enemy in enemies:
                    enemies.remove(enemy)
                score += 1
                break

    # Draw
    screen.fill(BLACK)

    player.draw(screen)

    for bullet in bullets:
        bullet.draw(screen)

    for enemy in enemies:
        enemy.draw(screen)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()