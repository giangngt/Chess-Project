import pygame, chess
from random import choice
from traceback import format_exc
from sys import stderr
from time import strftime
from copy import deepcopy
import time
pygame.init()


AI_SEARCH_DEPTH = 2

RED_CHECK          = (240, 150, 150)
WHITE              = (255, 255, 255)
BLUE_LIGHT         = (140, 184, 219)
BLUE_DARK          = (91,  131, 159)
GRAY_LIGHT         = (240, 240, 240)
GRAY_DARK          = (200, 200, 200)
CHESSWEBSITE_LIGHT = (212, 202, 190)
CHESSWEBSITE_DARK  = (100,  92,  89)
LICHESS_LIGHT      = (240, 217, 181)
LICHESS_DARK       = (181, 136,  99)
LICHESS_GRAY_LIGHT = (164, 164, 164)
LICHESS_GRAY_DARK  = (136, 136, 136)

BOARD_COLORS = [(GRAY_LIGHT, GRAY_DARK),
                (BLUE_LIGHT, BLUE_DARK),
                (WHITE, BLUE_LIGHT),
                (CHESSWEBSITE_LIGHT, CHESSWEBSITE_DARK),
                (LICHESS_LIGHT, LICHESS_DARK),
                (LICHESS_GRAY_LIGHT, LICHESS_GRAY_DARK)]
BOARD_COLOR = choice(BOARD_COLORS)

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

SCREEN = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
SCREEN_TITLE = 'Chess Game'
SQUARE_SIDE = 100

MOVE_SOUND = pygame.mixer.Sound('sounds/chess-effect.wav')
pygame.mixer.music.load('sounds/peaceful-piano.wav')



def resize_screen(square_side_len):
    global SQUARE_SIDE
    global SCREEN
    SCREEN = pygame.display.set_mode((8*square_side_len, 8*square_side_len), pygame.RESIZABLE)
    SQUARE_SIDE = square_side_len

"""HTP part
h = [0, 0, 0, 0, 0, 0, 0]
init_menu = True
init_game = False
init_htp = False
bigText = pygame.font.Font('Roboto/Roboto-Medium.ttf', 60)
mediumText = pygame.font.Font('Roboto/Roboto-Medium.ttf', 46)
midText = pygame.font.Font('Roboto/Roboto-Medium.ttf', 38)
smallText = pygame.font.Font('Roboto/Roboto-Medium.ttf', 30)

"""



"""HTP part
def text_to_screen(msg, center_x, center_y, size):
    textSurf, textRect = text_objects(msg, size)
    textRect.center = (center_x, center_y)
    SCREEN.blit(textSurf, textRect)
"""



"""partHTP
def htp():
    how = True
    SCREEN.fill((255, 255, 255))
    while how:
        h[6] = 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        text_to_screen("How To Play", 400, 30, bigText)
        text_to_screen("Objective: Capture opponent's king", 320, 100, midText)
        # text_to_screen("Objective: ", 110, 93, mediumText)
        # text_to_screen("Capture opponent's king", 390, 97, smallText)

        if 50 < mouse[0] < 178 and 184 < mouse[1] < 312:
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 184, 128, 128))
            SCREEN.blit(pygame.transform.scale(BLACK_PAWN, (128, 128)), (50, 184))
            pygame.display.update()
            if click[0] == 1:
                h[6] = 0
                h[0] = 1
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (50, 184, 128, 128))
            SCREEN.blit(pygame.transform.scale(WHITE_PAWN, (128, 128)), (50, 184))
            pygame.display.update()

        if 316 < mouse[0] < 444 and 184 < mouse[1] < 312:
            pygame.draw.rect(SCREEN, (255, 255, 255), (316, 184, 128, 128))
            SCREEN.blit(pygame.transform.scale(BLACK_ROOK, (128, 128)), (316, 184))
            pygame.display.update()
            if click[0] == 1:
                h[6] = 0
                h[1] = 1
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (316, 184, 128, 128))
            SCREEN.blit(pygame.transform.scale(WHITE_ROOK, (128, 128)), (316, 184))
            pygame.display.update()

        if 582 < mouse[0] < 710 and 184 < mouse[1] < 312:
            pygame.draw.rect(SCREEN, (255, 255, 255), (582, 184, 128, 128))
            SCREEN.blit(pygame.transform.scale(BLACK_KNIGHT, (128, 128)), (582, 184))
            pygame.display.update()
            if click[0] == 1:
                h[6] = 0
                h[2] = 1
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (582, 184, 128, 128))
            SCREEN.blit(pygame.transform.scale(WHITE_KNIGHT, (128, 128)), (582, 184))
            pygame.display.update()

        if 50 < mouse[0] < 178 and 450 < mouse[1] < 578:
            pygame.draw.rect(SCREEN, (255, 255, 255), (50, 450, 128, 128))
            SCREEN.blit(pygame.transform.scale(BLACK_BISHOP, (128, 128)), (50, 450))
            pygame.display.update()
            if click[0] == 1:
                h[6] = 0
                h[3] = 1
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (50, 450, 128, 128))
            SCREEN.blit(pygame.transform.scale(WHITE_BISHOP, (128, 128)), (50, 450))
            pygame.display.update()

        if 316 < mouse[0] < 444 and 450 < mouse[1] < 578:
            pygame.draw.rect(SCREEN, (255, 255, 255), (316, 450, 128, 128))
            SCREEN.blit(pygame.transform.scale(BLACK_QUEEN, (128, 128)), (316, 450))
            pygame.display.update()
            if click[0] == 1:
                h[6] = 0
                h[4] = 1
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (316, 450, 128, 128))
            SCREEN.blit(pygame.transform.scale(WHITE_QUEEN, (128, 128)), (316, 450))
            pygame.display.update()

        if 582 < mouse[0] < 710 and 450 < mouse[1] < 578:
            pygame.draw.rect(SCREEN, (255, 255, 255), (582, 450, 128, 128))
            SCREEN.blit(pygame.transform.scale(BLACK_KING, (128, 128)), (582, 450))
            pygame.display.update()
            if click[0] == 1:
                h[6] = 0
                h[5] = 1
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (582, 450, 128, 128))
            SCREEN.blit(pygame.transform.scale(WHITE_KING, (128, 128)), (582, 450))
            pygame.display.update()

        if 250 < mouse[0] < 550 and 650 < mouse[1] < 725:
            pygame.draw.rect(SCREEN, (192, 192, 192), (250, 650, 300, 75))
            text_to_screen('Main Menu', 400, 688, mediumText)
            # if click[0] == 1:
            # link Main Menu
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (250, 650, 300, 75))
            text_to_screen('Main Menu', 400, 688, mediumText)
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
        pygame.draw.rect(SCREEN, (0, 0, 0), (325, 5, 150, 150))
        SCREEN.blit(pygame.transform.scale(WHITE_PAWN, (150, 150)), (325, 5))
        text_to_screen('- These pieces can move one step at a time', 400, 200, smallText)
        text_to_screen('(2 for the first move)', 400, 275, smallText)
        text_to_screen('- Can attack one step diagonally', 400, 350, smallText)
        text_to_screen('- When reached the end of the chess board', 400, 425, smallText)
        text_to_screen('can be transformed into Queen', 400, 500, smallText)
        pygame.display.update()
        if 600 < mouse[0] < 750 and 650 < mouse[1] < 725:
            pygame.draw.rect(SCREEN, (192, 192, 192), (600, 650, 150, 75))
            text_to_screen('Rook', 675, 688, mediumText)
            if click[0] == 1:
                h[0] = 0
                h[1] = 1
                pygame.time.wait(250)
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (600, 650, 150, 75))
            text_to_screen('Rook', 675, 688, mediumText)
        pygame.display.update()
        if 50 < mouse[0] < 200 and 650 < mouse[1] < 725:
            pygame.draw.rect(SCREEN, (192, 192, 192), (50, 650, 150, 75))
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
    SCREEN.fill((255, 255, 255))
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
        text_to_screen("-If the right-sided rook (based on player perspective)", 400, 450, smallText)
        text_to_screen("and the king have not been moved and there are no other", 400, 500, smallText)
        text_to_screen("pieces between them, you can perform castling", 400, 550, smallText)
        pygame.display.update()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 600 < mouse[0] < 750 and 650 < mouse[1] < 725:
            pygame.draw.rect(SCREEN, (192, 192, 192), (600, 650, 150, 75))
            text_to_screen('Knight', 675, 688, mediumText)

            if click[0] == 1:
                h[1] = 0
                h[2] = 1
                pygame.time.wait(250)
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (600, 650, 150, 75))
            text_to_screen('Knight', 675, 688, mediumText)
        pygame.display.update()
        if 50 < mouse[0] < 200 and 650 < mouse[1] < 725:
            pygame.draw.rect(SCREEN, (192, 192, 192), (50, 650, 150, 75))
            text_to_screen('Menu', 125, 688, mediumText)
            if click[0] == 1:
                h[1] = 0
                h[6] = 1
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (50, 650, 150, 75))
            text_to_screen('Menu', 125, 688, mediumText)
        pygame.display.update()


def htp_knight():
    SCREEN.fill((255, 255, 255))
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
        text_to_screen('The knight can capture it', 400, 425, smallText)
        pygame.display.update()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 600 < mouse[0] < 750 and 650 < mouse[1] < 725:
            pygame.draw.rect(SCREEN, (192, 192, 192), (600, 650, 150, 75))
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
            pygame.draw.rect(SCREEN, (192, 192, 192), (50, 650, 150, 75))
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
    SCREEN.fill((255, 255, 255))
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
            pygame.draw.rect(SCREEN, (192, 192, 192), (600, 650, 150, 75))
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
            pygame.draw.rect(SCREEN, (192, 192, 192), (50, 650, 150, 75))
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
    SCREEN.fill((255, 255, 255))
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
            pygame.draw.rect(SCREEN, (192, 192, 192), (600, 650, 150, 75))
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
            pygame.draw.rect(SCREEN, (192, 192, 192), (50, 650, 150, 75))
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
    SCREEN.fill((255, 255, 255))
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
            pygame.draw.rect(SCREEN, (192, 192, 192), (300, 650, 200, 75))
            text_to_screen('Menu', 400, 688, mediumText)
            if click[0] == 1:
                h[5] = 0
                h[6] = 1
                return h
        else:
            pygame.draw.rect(SCREEN, (0, 0, 0), (300, 650, 200, 75))
            text_to_screen('Menu', 400, 688, mediumText)
        pygame.display.update()
"""

def print_empty_board():
    SCREEN.fill(BOARD_COLOR[0])
    paint_dark_squares(BOARD_COLOR[1])

def paint_square(square, square_color):
    col = chess.FILES.index(square[0])
    row = 7-chess.RANKS.index(square[1])
    pygame.draw.rect(SCREEN, square_color, (SQUARE_SIDE*col,SQUARE_SIDE*row,SQUARE_SIDE,SQUARE_SIDE), 0)

def paint_dark_squares(square_color):
    for position in chess.single_gen(chess.DARK_SQUARES):
        paint_square(chess.bb2str(position), square_color)

def get_square_rect(square):
    col = chess.FILES.index(square[0])
    row = 7-chess.RANKS.index(square[1])
    return pygame.Rect((col*SQUARE_SIDE, row*SQUARE_SIDE), (SQUARE_SIDE,SQUARE_SIDE))

def coord2str(position, color=chess.WHITE):
    if color == chess.WHITE:
        file_index = int(position[0]/SQUARE_SIDE)
        rank_index = 7 - int(position[1]/SQUARE_SIDE)
        return chess.FILES[file_index] + chess.RANKS[rank_index]
    if color == chess.BLACK:
        file_index = 7 - int(position[0]/SQUARE_SIDE)
        rank_index = int(position[1]/SQUARE_SIDE)
        return chess.FILES[file_index] + chess.RANKS[rank_index]

def print_board(board, color=chess.WHITE):
    if color == chess.WHITE:
        printed_board = board
    if color == chess.BLACK:
        printed_board = chess.rotate_board(board)

    print_empty_board()

    if chess.is_check(board, chess.WHITE):
        paint_square(chess.bb2str(chess.get_king(printed_board, chess.WHITE)), RED_CHECK)
    if chess.is_check(board, chess.BLACK):
        paint_square(chess.bb2str(chess.get_king(printed_board, chess.BLACK)), RED_CHECK)

    for position in chess.colored_piece_gen(printed_board, chess.KING, chess.BLACK):
        SCREEN.blit(pygame.transform.scale(BLACK_KING,   (SQUARE_SIDE,SQUARE_SIDE)), get_square_rect(chess.bb2str(position)))
    for position in chess.colored_piece_gen(printed_board, chess.QUEEN, chess.BLACK):
        SCREEN.blit(pygame.transform.scale(BLACK_QUEEN,  (SQUARE_SIDE,SQUARE_SIDE)), get_square_rect(chess.bb2str(position)))
    for position in chess.colored_piece_gen(printed_board, chess.ROOK, chess.BLACK):
        SCREEN.blit(pygame.transform.scale(BLACK_ROOK,   (SQUARE_SIDE,SQUARE_SIDE)), get_square_rect(chess.bb2str(position)))
    for position in chess.colored_piece_gen(printed_board, chess.BISHOP, chess.BLACK):
        SCREEN.blit(pygame.transform.scale(BLACK_BISHOP, (SQUARE_SIDE,SQUARE_SIDE)), get_square_rect(chess.bb2str(position)))
    for position in chess.colored_piece_gen(printed_board, chess.KNIGHT, chess.BLACK):
        SCREEN.blit(pygame.transform.scale(BLACK_KNIGHT, (SQUARE_SIDE,SQUARE_SIDE)), get_square_rect(chess.bb2str(position)))
    for position in chess.colored_piece_gen(printed_board, chess.PAWN, chess.BLACK):
        SCREEN.blit(pygame.transform.scale(BLACK_PAWN,   (SQUARE_SIDE,SQUARE_SIDE)), get_square_rect(chess.bb2str(position)))
    for position in chess.colored_piece_gen(printed_board, chess.JOKER, chess.BLACK):
        SCREEN.blit(pygame.transform.scale(BLACK_JOKER,  (SQUARE_SIDE,SQUARE_SIDE)), get_square_rect(chess.bb2str(position)))

    for position in chess.colored_piece_gen(printed_board, chess.KING, chess.WHITE):
        SCREEN.blit(pygame.transform.scale(WHITE_KING,   (SQUARE_SIDE,SQUARE_SIDE)), get_square_rect(chess.bb2str(position)))
    for position in chess.colored_piece_gen(printed_board, chess.QUEEN, chess.WHITE):
        SCREEN.blit(pygame.transform.scale(WHITE_QUEEN,  (SQUARE_SIDE,SQUARE_SIDE)), get_square_rect(chess.bb2str(position)))
    for position in chess.colored_piece_gen(printed_board, chess.ROOK, chess.WHITE):
        SCREEN.blit(pygame.transform.scale(WHITE_ROOK,   (SQUARE_SIDE,SQUARE_SIDE)), get_square_rect(chess.bb2str(position)))
    for position in chess.colored_piece_gen(printed_board, chess.BISHOP, chess.WHITE):
        SCREEN.blit(pygame.transform.scale(WHITE_BISHOP, (SQUARE_SIDE,SQUARE_SIDE)), get_square_rect(chess.bb2str(position)))
    for position in chess.colored_piece_gen(printed_board, chess.KNIGHT, chess.WHITE):
        SCREEN.blit(pygame.transform.scale(WHITE_KNIGHT, (SQUARE_SIDE,SQUARE_SIDE)), get_square_rect(chess.bb2str(position)))
    for position in chess.colored_piece_gen(printed_board, chess.PAWN, chess.WHITE):
        SCREEN.blit(pygame.transform.scale(WHITE_PAWN,   (SQUARE_SIDE,SQUARE_SIDE)), get_square_rect(chess.bb2str(position)))
    for position in chess.colored_piece_gen(printed_board, chess.JOKER, chess.WHITE):
        SCREEN.blit(pygame.transform.scale(WHITE_JOKER,  (SQUARE_SIDE,SQUARE_SIDE)), get_square_rect(chess.bb2str(position)))

    pygame.display.flip()

def set_title(title):
    pygame.display.set_caption(title)
    pygame.display.flip()

def make_AI_move(game, color):
    set_title(SCREEN_TITLE + ' - Calculating move...')
    new_game = chess.make_move(game, chess.get_AI_move(game, AI_SEARCH_DEPTH))
    set_title(SCREEN_TITLE)
    print_board(new_game.board, color)
    pygame.mixer.Sound.play(MOVE_SOUND)
    return new_game

def try_move(game, attempted_move):
    for move in chess.legal_moves(game, game.to_move):
        if move == attempted_move:
            pygame.mixer.Sound.play(MOVE_SOUND)
            game = chess.make_move(game, move)
    return game

def play_as(game, color):
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                menu = False
    run = True
    ongoing = True
    joker = 0

    try:  
        while run and ongoing:
            print_board(game.board, color)

            if chess.game_ended(game):
                set_title(SCREEN_TITLE + ' - ' + chess.get_outcome(game))
                ongoing = False
                time.sleep(5)

            if ongoing and game.to_move == chess.opposing_color(color):
                game = make_AI_move(game, color)

            if chess.game_ended(game):
                set_title(SCREEN_TITLE + ' - ' + chess.get_outcome(game))
                if ongoing:
                    ongoing = False
                    time.sleep(5)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    leaving_square = coord2str(event.pos, color)

                if event.type == pygame.MOUSEBUTTONUP:
                    arriving_square = coord2str(event.pos, color)

                    if ongoing and game.to_move == color:
                        move = (chess.str2bb(leaving_square), chess.str2bb(arriving_square))
                        game = try_move(game, move)
                        print_board(game.board, color)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == 113:
                        run = False
                    if event.key == 104 and ongoing: # H key
                        game = make_AI_move(game, color)
                    if event.key == 117: # U key
                        game = chess.unmake_move(game)
                        game = chess.unmake_move(game)
                        set_title(SCREEN_TITLE)
                        print_board(game.board, color)
                        ongoing = True

                    if event.key == 109: # M key
                        if pygame.mixer.music.get_volume() == 0:
                            pygame.mixer.music.set_volume(0.05)
                        elif pygame.mixer.music.get_volume() != 0:
                            pygame.mixer.music.set_volume(0)
                    if event.key == 99: # C key
                        global BOARD_COLOR
                        new_colors = deepcopy(BOARD_COLORS)
                        new_colors.remove(BOARD_COLOR)
                        BOARD_COLOR = choice(new_colors)
                        print_board(game.board, color)
                    if event.key == 112 or event.key == 100: # P or D key
                        print(game.get_move_list() + '\n')
                        print('\n'.join(game.position_history))
                    if event.key == 101: # E key
                        print('eval = ' + str(chess.evaluate_game(game)/100))
                    if event.key == 106: # J key
                        joker += 1
                        if joker == 13 and chess.get_queen(game.board, color):
                            queen_index = chess.bb2index(chess.get_queen(game.board, color))
                            game.board[queen_index] = color|chess.JOKER
                            print_board(game.board, color)

                if event.type == pygame.VIDEORESIZE:
                    if SCREEN.get_height() != event.h:
                        resize_screen(int(event.h/8.0))
                    elif SCREEN.get_width() != event.w:
                        resize_screen(int(event.w/8.0))
                    print_board(game.board, color)
    except:
        print(format_exc(), file=stderr)
        bug_file = open('bug_report.txt', 'a')
        bug_file.write('----- ' + strftime('%x %X') + ' -----\n')
        bug_file.write(format_exc())
        bug_file.write('\nPlaying as WHITE:\n\t' if color == chess.WHITE else '\nPlaying as BLACK:\n\t')
        bug_file.write(game.get_move_list() + '\n\t')
        bug_file.write('\n\t'.join(game.position_history))
        bug_file.write('\n-----------------------------\n\n')
        bug_file.close()

def play_as_white(game=chess.Game()):
    return play_as(game, chess.WHITE)

def play_as_black(game=chess.Game()):
    return play_as(game, chess.BLACK)

def play_random_color(game=chess.Game()):
    """HTP part
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    """
    color = choice([chess.WHITE, chess.BLACK])
    play_as(game, color)

# chess.verbose = True

  
    """HTP part
    print(init_menu)
    print(init_game)
    print(init_htp)
    if init_menu:
        main_menu()
    if init_game:
        play_random_color()
    if init_htp:
        htp()
        while init_htp:
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

"""