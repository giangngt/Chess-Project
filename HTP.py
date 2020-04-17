import pygame
from random import choice
from traceback import format_exc
from sys import stderr
from time import strftime
from copy import deepcopy
import time

pygame.init()

CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
bigText = pygame.font.Font('Roboto/Roboto-Medium.ttf', 60)
mediumText = pygame.font.Font('Roboto/Roboto-Medium.ttf', 46)
smallText = pygame.font.Font('Roboto/Roboto-Medium.ttf', 30)

def text_objects(text, font):
    textSurface = font.render(text, True, (119, 136, 153))
    return textSurface, textSurface.get_rect()

def text_to_screen(msg, center_x, center_y, size):
    textSurf, textRect = text_objects(msg, size)
    textRect.center = (center_x, center_y)
    SCREEN.blit(textSurf, textRect)

def htp():
    how = True
    while how:
        SCREEN.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        text_to_screen("How To Play", 400, 30, bigText)
        text_to_screen("Objective: ", 110, 93, mediumText)
        text_to_screen("Capture opponent's king", 390, 97, smallText)
        pygame.display.update()

htp()

