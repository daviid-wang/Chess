from enum import Enum
import pygame, sys

ROW_NUM = 8
COL_NUM = 8

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
pygame.display.set_caption("Chess!")
playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    #Make chessboard
    create_board()
    initial_position()
    pygame.display.update()
