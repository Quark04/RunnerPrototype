from cgi import test
from tkinter import font
from turtle import width
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Pygame Runner Prototype')
clock = pygame.time.Clock()
test_font = pygame.font.Font('C:\Python\Runner\Font/Pixeltype.ttf', 50)

score_surf = test_font.render('My Game', False, (64,64,64))
score_rect = score_surf.get_rect(center = (400,50))

sky_surface = pygame.image.load('C:\Python\Runner\Graphics/Sky.png').convert()
ground_surface = pygame.image.load('C:\Python\Runner\Graphics/ground.png').convert()

snail_surface = pygame.image.load('C:\Python\Runner\Graphics\Snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600,300))

player_surface = pygame.image.load('C:\Python\Runner\Graphics\Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos):
                player_gravity = -20

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -20

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    pygame.draw.rect(screen,'#c0e8ec',score_rect)
    pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
    screen.blit(score_surf,(score_rect))

    snail_rect.x -= 4 
    if snail_rect .right <= 0: snail_rect.left = 800
    screen.blit(snail_surface,snail_rect)

    # PLayer

    player_gravity += 1
    player_rect.y += player_gravity
    screen.blit(player_surface,player_rect)

    pygame.display.update()
    clock.tick(60)
