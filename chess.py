from enum import Enum
import pygame

ROW_NUM = 8
COL_NUM = 8
DEFAULT_PIECE_SIZE = (55, 57)
PAWN_DEFAULT_SIZE = (48, 53)

position = [[0 for i in range(8)] for i in range(8)]

class WhitePiece(Enum):
    ROOK    = "R"
    KNIGHT  = "N"
    BISHOP  = "B"
    QUEEN   = "Q"
    KING    = "K"
    PAWN    = "P"

class BlackPiece(Enum):
    ROOK    = "R"
    KNIGHT  = "N"
    BISHOP  = "B"
    QUEEN   = "Q"
    KING    = "K"
    PAWN    = "P"

def initial_position():
    position[0][0] = BlackPiece.ROOK
    position[0][1] = BlackPiece.KNIGHT
    position[0][2] = BlackPiece.BISHOP
    position[0][3] = BlackPiece.QUEEN
    position[0][4] = BlackPiece.KING
    position[0][5] = BlackPiece.BISHOP
    position[0][6] = BlackPiece.KNIGHT
    position[0][7] = BlackPiece.ROOK
    
    position[1][0] = BlackPiece.PAWN
    position[1][1] = BlackPiece.PAWN
    position[1][2] = BlackPiece.PAWN
    position[1][3] = BlackPiece.PAWN
    position[1][4] = BlackPiece.PAWN
    position[1][5] = BlackPiece.PAWN
    position[1][6] = BlackPiece.PAWN
    position[1][7] = BlackPiece.PAWN

    position[6][0] = WhitePiece.PAWN
    position[6][1] = WhitePiece.PAWN
    position[6][2] = WhitePiece.PAWN
    position[6][3] = WhitePiece.PAWN
    position[6][4] = WhitePiece.PAWN
    position[6][5] = WhitePiece.PAWN
    position[6][6] = WhitePiece.PAWN
    position[6][7] = WhitePiece.PAWN

    position[7][0] = WhitePiece.ROOK
    position[7][1] = WhitePiece.KNIGHT
    position[7][2] = WhitePiece.BISHOP
    position[7][3] = WhitePiece.QUEEN
    position[7][4] = WhitePiece.KING
    position[7][5] = WhitePiece.BISHOP
    position[7][6] = WhitePiece.KNIGHT
    position[7][7] = WhitePiece.ROOK
    # print(position)

def create_board():
    """Create chessboard"""
    board_dark = (209,139,70)
    board_light = (254,206,158)
    for i in range(0, 16):
        board_tile1 = pygame.Rect(100 + (i % 4)*150, 50 + (int(i / 4))*150, 75, 75)
        pygame.draw.rect(board, board_light, board_tile1)
        board_tile2 = pygame.Rect(175 + (i % 4)*150, 125 + (int(i / 4))*150, 75, 75)
        pygame.draw.rect(board, board_light, board_tile2)
        board_tile3 = pygame.Rect(175 + (i % 4)*150, 50 + (int(i / 4))*150, 75, 75)
        pygame.draw.rect(board, board_dark, board_tile3)
        board_tile4 = pygame.Rect(100 + (i % 4)*150, 125 + (int(i / 4))*150, 75, 75)
        pygame.draw.rect(board, board_dark, board_tile4)

board = pygame.display.set_mode((800, 700))

pawn_white = pygame.image.load("Images/pawn_white.png")
pawn_white = pygame.transform.scale(pawn_white, PAWN_DEFAULT_SIZE)
rook_white = pygame.image.load("Images/rook_white.png")
rook_white = pygame.transform.scale(rook_white, PAWN_DEFAULT_SIZE)
knight_white = pygame.image.load("Images/knight_white.png")
knight_white = pygame.transform.scale(knight_white, DEFAULT_PIECE_SIZE)
bishop_white = pygame.image.load("Images/bishop_white.png")
bishop_white = pygame.transform.scale(bishop_white, DEFAULT_PIECE_SIZE)
queen_white = pygame.image.load("Images/queen_white.png")
queen_white = pygame.transform.scale(queen_white, DEFAULT_PIECE_SIZE)
king_white = pygame.image.load("Images/king_white.png")
king_white = pygame.transform.scale(king_white, DEFAULT_PIECE_SIZE)

pawn_black = pygame.image.load("Images/pawn_black.png")
pawn_black = pygame.transform.scale(pawn_black, PAWN_DEFAULT_SIZE)
rook_black = pygame.image.load("Images/rook_black.png")
rook_black = pygame.transform.scale(rook_black, PAWN_DEFAULT_SIZE)
knight_black = pygame.image.load("Images/knight_black.png")
knight_black = pygame.transform.scale(knight_black, DEFAULT_PIECE_SIZE)
bishop_black = pygame.image.load("Images/bishop_black.png")
bishop_black = pygame.transform.scale(bishop_black, DEFAULT_PIECE_SIZE)
queen_black = pygame.image.load("Images/queen_black.png")
queen_black = pygame.transform.scale(queen_black, DEFAULT_PIECE_SIZE)
king_black = pygame.image.load("Images/king_black.png")
king_black = pygame.transform.scale(king_black, DEFAULT_PIECE_SIZE)

def board_location_to_coordinates(x_location, y_location, adjustment=False):
    """Converts the board location (a1) to coordinates on the grid"""
    x_coordinate = x_location * 75 + 109.5
    y_coordinate = y_location * 75 + 58
    if adjustment:
        x_coordinate += 4
        y_coordinate += 3
    return (x_coordinate, y_coordinate)

initial_position()

pygame.display.set_caption("Chess!")
playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    #Make chessboard
    create_board()
    # board.blit(rook_white, board_location_to_coordinates(0, 0))
    # board.blit(rook_white, board_location_to_coordinates(7, 0))
    for i in range(0, 8):
        for j in range(0, 8):
            if position[i][j] != 0:
                if position[i][j] == WhitePiece.PAWN:
                    board.blit(pawn_white, board_location_to_coordinates(j, i, True))
                if position[i][j] == WhitePiece.ROOK:
                    board.blit(rook_white, board_location_to_coordinates(j, i, True))
                if position[i][j] == WhitePiece.KNIGHT:
                    board.blit(knight_white, board_location_to_coordinates(j, i))
                if position[i][j] == WhitePiece.BISHOP:
                    board.blit(bishop_white, board_location_to_coordinates(j, i))
                if position[i][j] == WhitePiece.QUEEN:
                    board.blit(queen_white, board_location_to_coordinates(j, i))
                if position[i][j] == WhitePiece.KING:
                    board.blit(king_white, board_location_to_coordinates(j, i))
                if position[i][j] == BlackPiece.PAWN:
                    board.blit(pawn_black, board_location_to_coordinates(j, i, True))
                if position[i][j] == BlackPiece.ROOK:
                    board.blit(rook_black, board_location_to_coordinates(j, i, True))
                if position[i][j] == BlackPiece.KNIGHT:
                    board.blit(knight_black, board_location_to_coordinates(j, i))
                if position[i][j] == BlackPiece.BISHOP:
                    board.blit(bishop_black, board_location_to_coordinates(j, i))
                if position[i][j] == BlackPiece.QUEEN:
                    board.blit(queen_black, board_location_to_coordinates(j, i))
                if position[i][j] == BlackPiece.KING:
                    board.blit(king_black, board_location_to_coordinates(j, i))
    pygame.display.update()