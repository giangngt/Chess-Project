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

BLACK_KING   = pygame.image.load('images/black_king.png')
BLACK_QUEEN  = pygame.image.load('images/black_queen.png')
BLACK_ROOK   = pygame.image.load('images/black_rook.png')
BLACK_BISHOP = pygame.image.load('images/black_bishop.png')
BLACK_KNIGHT = pygame.image.load('images/black_knight.png')
BLACK_PAWN   = pygame.image.load('images/black_pawn.png')
BLACK_JOKER  = pygame.image.load('images/black_joker.png')

WHITE_KING   = pygame.image.load('images/white_king.png')
WHITE_QUEEN  = pygame.image.load('images/white_queen.png')
WHITE_ROOK   = pygame.image.load('images/white_rook.png')
WHITE_BISHOP = pygame.image.load('images/white_bishop.png')
WHITE_KNIGHT = pygame.image.load('images/white_knight.png')
WHITE_PAWN   = pygame.image.load('images/white_pawn.png')
WHITE_JOKER  = pygame.image.load('images/white_joker.png')


def text_objects(text, font):
    textSurface = font.render(text, True, (119, 136, 153))
    return textSurface, textSurface.get_rect()

def text_to_screen(msg, center_x, center_y, size):
    textSurf, textRect = text_objects(msg, size)
    textRect.center = (center_x, center_y)
    SCREEN.blit(textSurf, textRect)

h = [0,0,0,0,0,0,0,0]

def htp():
    how = True
    while how:
        SCREEN.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        text_to_screen("How To Play", 400, 30, bigText)
        text_to_screen("Objective: ", 110, 93, mediumText)
        text_to_screen("Capture opponent's king", 390, 97, smallText)
        if 50<mouse[0]<178 and 150<mouse[1]<278:
            pygame.draw.rect(SCREEN, (255,255,255), (50,150,128,128))
            SCREEN.blit(pygame.transform.scale(BLACK_PAWN, (128,128)), (50,150))
            pygame.display.update()
            if click[0] == 1:
                h[0] = 1
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (50, 150, 128, 128))
            SCREEN.blit(pygame.transform.scale(WHITE_PAWN, (128, 128)), (50, 150))
            pygame.display.update()
        
def htp_pawn():
    SCREEN.fill((255, 255, 255))
    while h[0] == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(click)
        pygame.draw.rect(SCREEN, (0, 0, 0), (325, 0, 150, 150))
        SCREEN.blit(pygame.transform.scale(WHITE_PAWN, (150, 150)), (325, 0))
        text_to_screen('- These pieces can move one step at a time', 400, 200, smallText)
        text_to_screen('(2 for the first move)', 400, 275, smallText)
        text_to_screen('- Can attack one step diagonally', 400, 350, smallText)
        text_to_screen('- When reached the end of the chess board', 400, 425, smallText)
        text_to_screen('can be transformed into Queen', 400, 500, smallText)
        pygame.display.update()
        if 600<mouse[0]<750 and 650<mouse[1]<725:
            pygame.draw.rect(SCREEN, (192, 192, 192), (600, 650, 150, 75))
            text_to_screen('Rook', 675, 688, mediumText)
            if click[0] == 1:
                h[0]=0
                h[1]=1
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (600, 650, 150, 75))
            text_to_screen('Rook', 675, 688, mediumText)
        pygame.display.update()
        if 50<mouse[0]<200 and 650<mouse[1]<725:
            pygame.draw.rect(SCREEN, (192, 192, 192), (50, 650, 150, 75))
            text_to_screen('Menu', 125, 688, mediumText)
            #  if click[0]=1:

        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (50, 650, 150, 75))
            text_to_screen('Menu', 125, 688, mediumText)
        pygame.display.update()

def htp_rook():
    SCREEN.fill((255, 255, 255))
    while h[1] == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.rect(SCREEN, (0, 0, 0), (325, 0, 150, 150))
        SCREEN.blit(pygame.transform.scale(WHITE_ROOK, (150, 150)), (325, 0))
        text_to_screen('- These pieces can move horizontally or vertically in ', 400, 200, smallText)
        text_to_screen('unlimited steps until there is another chess piece', 400, 250, smallText)
        text_to_screen('blocking its way.', 400, 300, smallText)
        text_to_screen('-If the blocking piece is the opponent’s, the rook', 400, 350, smallText)
        text_to_screen("the rook can capture it.", 400, 400, smallText)
        text_to_screen("-If the right-sided rook (based on player perspective)",400,450,smallText)
        text_to_screen("and the king have not been moved and there are no other", 400 ,500, smallText)
        text_to_screen("pieces between them, you can perform castling",400,550,smallText)
        pygame.display.update()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 600<mouse[0]<750 and 650<mouse[1]<725:
            pygame.draw.rect(SCREEN, (192, 192, 192), (600, 650, 150, 75))
            text_to_screen('Knight', 675, 688, mediumText)
            '''if click[0] == 1:
                h[1]=0
                h[2]=1
                return h'''
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (600, 650, 150, 75))
            text_to_screen('Knight', 675, 688, mediumText)
        pygame.display.update()
        if 50<mouse[0]<200 and 650<mouse[1]<725:
            pygame.draw.rect(SCREEN, (192, 192, 192), (50, 650, 150, 75))
            text_to_screen('Menu', 125, 688, mediumText)
            #  if click[0]=1:

        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (50, 650, 150, 75))
            text_to_screen('Menu', 125, 688, mediumText)
        pygame.display.update()

htp()
if h[0]==1:
    htp_pawn()

if h[1]==1:
    htp_rook()

