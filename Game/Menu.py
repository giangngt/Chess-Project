import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600)) # Change to reso of gui

# Background, change the image should you find a better one
background = pygame.image.load('images/menu-wallpaper.jpg').convert()
background = pygame.transform.scale(background, (800, 600)) # This is to resize the background to fit UI, I find not having this also looks good



clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, (0, 128, 128)) #Please consider making changes to the colouring, this is just temporary
    return textSurface, textSurface.get_rect()


def main_menu():
    menu = True
    #background = pygame.image.load('chess.bmp').convert()
    #screen.blit(background,(0,0))
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #if event.type == pygame.MOUSEBUTTONDOWN:
                #if event.key == pygame.
        screen.blit(background, (0, 0))
        #screen.fill((255, 255, 255))
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        textSurf, textRect = text_objects('Chess Game', largeText)
        textRect.center = (400, 300)
        screen.blit(textSurf, textRect)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 750 > mouse[0] > 50 and 575 > mouse[1] > 525:
            pygame.draw.rect(screen, (0, 150, 0), (50, 525, 700, 50))
            if click[0] == 1:
               exec(open('gui.py').read())
        else:
            pygame.draw.rect(screen, (0, 255, 0), (50, 525, 700, 50))

        if 750 > mouse[0] > 450 and 500 > mouse[1] > 450:
            pygame.draw.rect(screen, (150, 0, 0), (450, 450, 300, 50))
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(screen, (255, 0, 0), (450, 450, 300, 50))

        if 350 > mouse[0] > 50 and 500 > mouse[1] > 450:
            pygame.draw.rect(screen, (0, 0, 150), (50, 450, 300, 50))
            # if click[0] == 1:
                # link to HTP
        else:
            pygame.draw.rect(screen, (0, 0, 255), (50, 450, 300, 50))

        smallText = pygame.font.Font('freesansbold.ttf', 30)
        textSurf, textRect = text_objects('Start!', smallText)
        textRect.center = (400, 550)
        screen.blit(textSurf, textRect)
        textSurf, textRect = text_objects('Instruction', smallText)
        textRect.center = (200, 475)
        screen.blit(textSurf, textRect)
        pygame.display.update()
        textSurf, textRect = text_objects('Quit', smallText)
        textRect.center = (600, 475)
        screen.blit(textSurf, textRect)
        pygame.display.update()
        clock.tick(30)

main_menu()