import pygame


def text_objects(text, font):
    textSurface = font.render(text, True, (119, 136, 153))
    return textSurface, textSurface.get_rect()

def main_menu(SCREEN,CLOCK):
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
                return #before HTP
                """HTP part
                global init_game
                init_game = True
                global init_menu
                init_menu = False
                return init_game, init_menu
                """
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
            """part HTP
            if click[0] == 1:
                global init_htp
                init_htp = True
                return init_htp
            """
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
