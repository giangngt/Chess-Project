import pygame, chess
from random import choice
from traceback import format_exc
from sys import stderr
from time import strftime
from copy import deepcopy
import time
pygame.init()


SQUARE_SIDE = 100
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

MOVE_SOUND = pygame.mixer.Sound('sounds/chess-effect.wav')
pygame.mixer.music.load('sounds/peaceful-piano.wav')

CLOCK = pygame.time.Clock()
CLOCK_TICK = 15



#SCREEN = pygame.display.set_mode((8*SQUARE_SIDE, 8*SQUARE_SIDE), pygame.RESIZABLE)
SCREEN = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
SCREEN_TITLE = 'Chess Game'

pygame.display.set_icon(pygame.image.load('images/chess_icon.ico'))
pygame.display.set_caption(SCREEN_TITLE)
def text_objects(text, font):
    textSurface = font.render(text, True, (119, 136, 153))
    return textSurface, textSurface.get_rect()


def resize_screen(square_side_len):
    global SQUARE_SIDE
    global SCREEN
    SCREEN = pygame.display.set_mode((8*square_side_len, 8*square_side_len), pygame.RESIZABLE)
    SQUARE_SIDE = square_side_len



def main_menu():
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
                return
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
            # if click[0] == 1:
                # link to HTP
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
            CLOCK.tick(CLOCK_TICK)
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
    color = choice([chess.WHITE, chess.BLACK])
    play_as(game, color)

# chess.verbose = True
while True:
    main_menu()
    play_random_color()





