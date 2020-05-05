import pygame

pygame.init()

CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
bigText = pygame.font.Font('Roboto/Roboto-Medium.ttf', 60)
mediumText = pygame.font.Font('Roboto/Roboto-Medium.ttf', 46)
midText = pygame.font.Font('Roboto/Roboto-Medium.ttf', 38)
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
    textSurface = font.render(text, True, (255,235,205))
    return textSurface, textSurface.get_rect()

def text_to_screen(msg, center_x, center_y, size):
    textSurf, textRect = text_objects(msg, size)
    textRect.center = (center_x, center_y)
    SCREEN.blit(textSurf, textRect)

h = [0,0,0,0,0,0,0]
init = True
background = pygame.image.load('images/instruct1.jpg').convert()
def htp():
    global init
    init = True
    how = True
    #background = pygame.image.load('images/instruct1.jpg').convert()
    #background = pygame.transform.scale(background,(800,800))
    #SCREEN.fill((255, 255, 255))
    SCREEN.blit(background,(0,0))
    while how:
        h[6]=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        text_to_screen("How To Play", 400, 30, bigText)
        text_to_screen("Objective: Capture opponent's king", 320, 100, midText)
        #text_to_screen("Objective: ", 110, 93, mediumText)
        #text_to_screen("Capture opponent's king", 390, 97, smallText)

        if 70<mouse[0]<198 and 184<mouse[1]<312:
            pygame.draw.rect(SCREEN, (255,255,255), (70,184,128,128))
            SCREEN.blit(pygame.transform.scale(BLACK_PAWN, (128,128)), (70,184))
            pygame.display.update()
            if click[0] == 1:
                h[6] = 0
                h[0] = 1
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (70, 184, 128, 128))
            SCREEN.blit(pygame.transform.scale(WHITE_PAWN, (128, 128)), (70, 184))
            pygame.display.update()

        if 336<mouse[0]<464 and 184<mouse[1]<312:
            pygame.draw.rect(SCREEN, (255, 255, 255), (336, 184, 128, 128))
            SCREEN.blit(pygame.transform.scale(BLACK_ROOK, (128, 128)), (336, 184))
            pygame.display.update()
            if click[0] == 1:
                h[6] = 0
                h[1] = 1
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (336, 184, 128, 128))
            SCREEN.blit(pygame.transform.scale(WHITE_ROOK, (128, 128)), (336, 184))
            pygame.display.update()

        if 602<mouse[0]<730 and 184<mouse[1]<312:
            pygame.draw.rect(SCREEN, (255, 255, 255), (602, 184, 128, 128))
            SCREEN.blit(pygame.transform.scale(BLACK_KNIGHT, (128, 128)), (602, 184))
            pygame.display.update()
            if click[0] == 1:
                h[6] = 0
                h[2] = 1
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (602, 184, 128, 128))
            SCREEN.blit(pygame.transform.scale(WHITE_KNIGHT, (128, 128)), (602, 184))
            pygame.display.update()

        if 70<mouse[0]<198 and 450<mouse[1]<578:
            pygame.draw.rect(SCREEN, (255, 255, 255), (70, 450, 128, 128))
            SCREEN.blit(pygame.transform.scale(BLACK_BISHOP, (128, 128)), (70, 450))
            pygame.display.update()
            if click[0] == 1:
                h[6] = 0
                h[3] = 1
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (70, 450, 128, 128))
            SCREEN.blit(pygame.transform.scale(WHITE_BISHOP, (128, 128)), (70, 450))
            pygame.display.update()

        if 336<mouse[0]<464 and 450<mouse[1]<578:
            pygame.draw.rect(SCREEN, (255, 255, 255), (336, 450, 128, 128))
            SCREEN.blit(pygame.transform.scale(BLACK_QUEEN, (128, 128)), (336, 450))
            pygame.display.update()
            if click[0] == 1:
                h[6] = 0
                h[4] = 1
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (336, 450, 128, 128))
            SCREEN.blit(pygame.transform.scale(WHITE_QUEEN, (128, 128)), (336, 450))
            pygame.display.update()

        if 602<mouse[0]<730 and 450<mouse[1]<578:
            pygame.draw.rect(SCREEN, (255, 255, 255), (602, 450, 128, 128))
            SCREEN.blit(pygame.transform.scale(BLACK_KING, (128, 128)), (602, 450))
            pygame.display.update()
            if click[0] == 1:
                h[6] = 0
                h[5] = 1
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (602, 450, 128, 128))
            SCREEN.blit(pygame.transform.scale(WHITE_KING, (128, 128)), (602, 450))
            pygame.display.update()

        if 250 < mouse[0] < 550 and 650 < mouse[1] < 725:
            pygame.draw.rect(SCREEN, (205,170,125), (250, 650, 300, 75))
            text_to_screen('Main Menu', 400, 688, mediumText)
            if click[0] == 1:
               init = False
               return 
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (250, 650, 300, 75))
            text_to_screen('Main Menu', 400, 688, mediumText)
            pygame.display.update()
        
def htp_pawn():
    SCREEN.blit(background,(0,0))
    while h[0] == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        pygame.draw.rect(SCREEN, (0, 0, 0), (325, 5, 150, 150))
        SCREEN.blit(pygame.transform.scale(WHITE_PAWN, (150, 150)), (325, 5))
        text_to_screen('- These pieces can move one step at a time', 400, 200, smallText)
        text_to_screen('(2 for the first move)', 400, 275, smallText)
        text_to_screen('- Can attack one step diagonally', 400, 350, smallText)
        text_to_screen('- When reached the end of the chess board', 400, 425, smallText)
        text_to_screen('can be transformed into Queen', 400, 500, smallText)
        pygame.display.update()
        if 600<mouse[0]<750 and 650<mouse[1]<725:
            pygame.draw.rect(SCREEN, (205, 170, 125), (600, 650, 150, 75))
            text_to_screen('Rook', 675, 688, mediumText)
            if click[0] == 1:
                h[0]=0
                h[1]=1
                pygame.time.wait(250)
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (600, 650, 150, 75))
            text_to_screen('Rook', 675, 688, mediumText)
        pygame.display.update()
        if 50<mouse[0]<200 and 650<mouse[1]<725:
            pygame.draw.rect(SCREEN, (205, 170, 125), (50, 650, 150, 75))
            text_to_screen('Menu', 125, 688, mediumText)
            if click[0] == 1:
                h[0] = 0
                h[6] = 1
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (50, 650, 150, 75))
            text_to_screen('Menu', 125, 688, mediumText)
        pygame.display.update()

def htp_rook():
    SCREEN.blit(background,(0,0))
    while h[1] == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.rect(SCREEN, (0, 0, 0), (325, 5, 150, 150))
        SCREEN.blit(pygame.transform.scale(WHITE_ROOK, (150, 150)), (325, 5))
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
            pygame.draw.rect(SCREEN, (205, 170, 125), (600, 650, 150, 75))
            text_to_screen('Knight', 675, 688, mediumText)
            
            if click[0] == 1:
                h[1]=0
                h[2]=1
                pygame.time.wait(250)
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (600, 650, 150, 75))
            text_to_screen('Knight', 675, 688, mediumText)
        pygame.display.update()
        if 50<mouse[0]<200 and 650<mouse[1]<725:
            pygame.draw.rect(SCREEN, (205, 170, 125), (50, 650, 150, 75))
            text_to_screen('Menu', 125, 688, mediumText)
            if click[0] == 1:
                h[1]=0
                h[6]=1
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (50, 650, 150, 75))
            text_to_screen('Menu', 125, 688, mediumText)
        pygame.display.update()

def htp_knight():
    SCREEN.blit(background,(0,0))
    while h[2] == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.rect(SCREEN, (0, 0, 0), (325, 5, 150, 150))
        SCREEN.blit(pygame.transform.scale(WHITE_KNIGHT, (150, 150)), (325, 5))
        text_to_screen('- These pieces can move in an “L” shape', 400, 200, smallText)
        text_to_screen('(2 steps vertically and 1 step horizontally or vice versa)', 400, 275, smallText)
        text_to_screen('- If a blocking piece is the opponent’s', 400, 350, smallText)
        text_to_screen('The knight can capture it', 400, 425,smallText)
        pygame.display.update()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 600 < mouse[0] < 750 and 650 < mouse[1] < 725:
            pygame.draw.rect(SCREEN, (205, 170, 125), (600, 650, 150, 75))
            text_to_screen('Bishop', 675, 688, mediumText)

            if click[0] == 1:
                h[2] = 0
                h[3] = 1
                pygame.time.wait(250)
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (600, 650, 150, 75))
            text_to_screen('Bishop', 675, 688, mediumText)
        pygame.display.update()
        if 50 < mouse[0] < 200 and 650 < mouse[1] < 725:
            pygame.draw.rect(SCREEN, (205, 170, 125), (50, 650, 150, 75))
            text_to_screen('Menu', 125, 688, mediumText)
            if click[0] == 1:
                h[2] = 0
                h[6] = 1
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (50, 650, 150, 75))
            text_to_screen('Menu', 125, 688, mediumText)
        pygame.display.update()

def htp_bishop():
    SCREEN.blit(background,(0,0))
    while h[3] == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.rect(SCREEN, (0, 0, 0), (325, 5, 150, 150))
        SCREEN.blit(pygame.transform.scale(WHITE_BISHOP, (150, 150)), (325, 5))
        text_to_screen('- These pieces can only move diagonally in unlimited steps', 400, 200, smallText)
        text_to_screen('until there is another chess piece blocking its way', 400, 275, smallText)
        text_to_screen('If the blocking piece is the opponent’s', 400, 350, smallText)
        text_to_screen('The bishop can capture it', 400, 425, smallText)
        pygame.display.update()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 600 < mouse[0] < 750 and 650 < mouse[1] < 725:
            pygame.draw.rect(SCREEN, (205, 170, 125), (600, 650, 150, 75))
            text_to_screen('Queen', 675, 688, mediumText)

            if click[0] == 1:
                h[3] = 0
                h[4] = 1
                pygame.time.wait(250)
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (600, 650, 150, 75))
            text_to_screen('Queen', 675, 688, mediumText)
        pygame.display.update()
        if 50 < mouse[0] < 200 and 650 < mouse[1] < 725:
            pygame.draw.rect(SCREEN, (205, 170, 125), (50, 650, 150, 75))
            text_to_screen('Menu', 125, 688, mediumText)
            if click[0] == 1:
                h[3] = 0
                h[6] = 1
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (50, 650, 150, 75))
            text_to_screen('Menu', 125, 688, mediumText)
        pygame.display.update()

def htp_queen():
    SCREEN.blit(background,(0,0))
    while h[4] == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.rect(SCREEN, (0, 0, 0), (325, 5, 150, 150))
        SCREEN.blit(pygame.transform.scale(WHITE_QUEEN, (150, 150)), (325, 5))
        text_to_screen('- These pieces can move in 3 directions: vertically', 400, 200, smallText)
        text_to_screen('horizontally and diagonally in unlimited steps', 400, 275, smallText)
        text_to_screen('until there is another piece blocking its way', 400, 350, smallText)
        text_to_screen('- If the blocking piece is the opponent’s', 400, 425, smallText)
        text_to_screen('The queen can capture it', 400, 500, smallText)
        pygame.display.update()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 600 < mouse[0] < 750 and 650 < mouse[1] < 725:
            pygame.draw.rect(SCREEN, (205, 170, 125), (600, 650, 150, 75))
            text_to_screen('King', 675, 688, mediumText)

            if click[0] == 1:
                h[4] = 0
                h[5] = 1
                pygame.time.wait(250)
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (600, 650, 150, 75))
            text_to_screen('King', 675, 688, mediumText)
        pygame.display.update()
        if 50 < mouse[0] < 200 and 650 < mouse[1] < 725:
            pygame.draw.rect(SCREEN, (205, 170, 125), (50, 650, 150, 75))
            text_to_screen('Menu', 125, 688, mediumText)
            if click[0] == 1:
                h[4] = 0
                h[6] = 1
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (50, 650, 150, 75))
            text_to_screen('Menu', 125, 688, mediumText)
        pygame.display.update()

def htp_king():
    SCREEN.blit(background,(0,0))
    while h[5] == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.draw.rect(SCREEN, (0, 0, 0), (325, 5, 150, 150))
        SCREEN.blit(pygame.transform.scale(WHITE_KING, (150, 150)), (325, 5))
        text_to_screen('- These pieces are the most important pieces on the board', 400, 200, smallText)
        text_to_screen('- These pieces can move 1 step only in 3 directions', 400, 250, smallText)
        text_to_screen('vertically, horizontally and diagonally', 400, 300, smallText)
        text_to_screen('- If these pieces are in danger (being checked)', 400, 350, smallText)
        text_to_screen('other pieces can not be moved except for pieces', 400, 400, smallText)
        text_to_screen('that can protect the kings.', 400, 450, smallText)
        text_to_screen('- If the blocking piece is the opponent’s', 400, 500, smallText)
        text_to_screen('the king can capture it', 400, 550, smallText)
        text_to_screen('If these pieces are captured, the other player wins the game', 400, 600, smallText)
        pygame.display.update()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 300 < mouse[0] < 500 and 650 < mouse[1] < 725:
            pygame.draw.rect(SCREEN, (205, 170, 125), (300, 650, 200, 75))
            text_to_screen('Menu', 400, 688, mediumText)
            if click[0] == 1:
                h[5] = 0
                h[6] = 1
                pygame.time.wait(250)
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (300, 650, 200, 75))
            text_to_screen('Menu', 400, 688, mediumText)
        pygame.display.update()

def how_to_play():
    htp()
    while init:
        if h[0]==1:
            htp_pawn()
        if h[1]==1:
            htp_rook()
        if h[2]==1:
            htp_knight()
        if h[3]==1:
            htp_bishop()
        if h[4]==1:
            htp_queen()
        if h[5]==1:
            htp_king()
        if h[6]==1:
            htp()
