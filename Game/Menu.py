import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600)) # Change to reso of gui

clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()


def main_menu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #if event.type == pygame.MOUSEBUTTONDOWN:
                #if event.key == pygame.
        screen.fill((255, 255, 255))
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        textSurf, textRect = text_objects('Chess Game', largeText)
        textRect.center = (400, 300)
        screen.blit(textSurf, textRect)
        mouse = pygame.mouse.get_pos()
        if 750 > mouse[0] > 50 and 575 > mouse[1] > 525:
            pygame.draw.rect(screen, (0, 150, 0), (50, 525, 700, 50))
        else:
            pygame.draw.rect(screen, (0, 255, 0), (50, 525, 700, 50))

        if 750 > mouse[0] > 450 and 500 > mouse[1] > 450:
            pygame.draw.rect(screen, (150, 0, 0), (450, 450, 300, 50))
        else:
            pygame.draw.rect(screen, (255, 0, 0), (450, 450, 300, 50))
        if 350 > mouse[0] > 50 and 500 > mouse[1] > 450:
            pygame.draw.rect(screen, (0, 0, 150), (50, 450, 300, 50))
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