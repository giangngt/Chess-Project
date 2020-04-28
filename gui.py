import pygame,chess
from gameplay import play_random_color
from HTP import how_to_play

pygame.init()

SQUARE_SIDE = 100

MOVE_SOUND = pygame.mixer.Sound('sounds/chess-effect.wav')
pygame.mixer.music.load('sounds/peaceful-piano.wav')

CLOCK = pygame.time.Clock()
CLOCK_TICK = 15
gamestt = 0


#SCREEN = pygame.display.set_mode((8*SQUARE_SIDE, 8*SQUARE_SIDE), pygame.RESIZABLE)
SCREEN = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
SCREEN_TITLE = 'Chess Game'


pygame.display.set_icon(pygame.image.load('images/chess_icon.ico'))
pygame.display.set_caption(SCREEN_TITLE)


def text_objects(text, font):
    textSurface = font.render(text, True, (119, 136, 153))
    return textSurface, textSurface.get_rect()

def main_menu():
    global gamestt
    gamestt = 0
    background = pygame.image.load('images/better-wallpaper.jpg').convert()
    background = pygame.transform.scale(background, (800, 800))
    title = pygame.image.load('images/title_pink.png').convert_alpha()
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)

    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == 109: # M key
                    if pygame.mixer.music.get_volume() == 0:
                        pygame.mixer.music.set_volume(0.05)
                    elif pygame.mixer.music.get_volume() != 0:
                        pygame.mixer.music.set_volume(0)

            #if event.type == pygame.MOUSEBUTTONDOWN:
                #if event.key == pygame.
        #SCREEN.fill((255, 255, 255))
        SCREEN.blit(background, (0, 0))
        SCREEN.blit(title,(50,50))
        #largeText = pygame.font.Font('freesansbold.ttf', 115)
        #textSurf, textRect = text_objects('Chess Game', largeText)
        #textRect.center = (400, 100)
        #SCREEN.blit(textSurf, textRect)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 350 > mouse[0] > 50 and 400 > mouse[1] > 350:
            pygame.draw.rect(SCREEN, (0, 255, 127), (50, 350, 300, 50))
            if click[0] == 1:
                gamestt = 1
                return #before HTP
        else:
            pygame.draw.rect(SCREEN, (169, 169, 169), (50, 350, 300, 50))

        if 350 > mouse[0] > 50 and 600 > mouse[1] > 550:
            pygame.draw.rect(SCREEN, (220, 20, 60), (50, 550, 300, 50))
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(SCREEN, (169, 169, 169), (50, 550, 300, 50))

        if 350 > mouse[0] > 50 and 500 > mouse[1] > 450:
            pygame.draw.rect(SCREEN, (100, 149, 237), (50, 450, 300, 50))
            if click[0] == 1:
                gamestt = 2
                return
        else:
            pygame.draw.rect(SCREEN, (169, 169, 169), (50, 450, 300, 50))

        smallText = pygame.font.Font('Roboto/Roboto-Medium.ttf', 30)
        textSurf, textRect = text_objects('Start', smallText)
        textRect.center = (200, 375)
        SCREEN.blit(textSurf, textRect)
        textSurf, textRect = text_objects('Instruction', smallText)
        textRect.center = (200, 475)
        SCREEN.blit(textSurf, textRect)
        pygame.display.update()
        textSurf, textRect = text_objects('Quit', smallText)
        textRect.center = (200, 575)
        SCREEN.blit(textSurf, textRect)
        pygame.display.update()
        CLOCK.tick(30)

while True:
    main_menu()
    if(gamestt == 1):
        play_random_color()
    else:
        how_to_play()