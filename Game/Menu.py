import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))


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
        screen.fill((255, 255, 255))
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        textSurf, textRect = text_objects('Chess Game', largeText)
        textRect.center = (400,300)
        screen.blit(textSurf,textRect)
        pygame.display.update()
        
main_menu()