"""
This is our main driver file. It will be responsible for handling user input and displaying the current GameState
"""

import pygame as p

from Chess import ChessEngine

p.init()
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 60
IMAGES = {}
"""
Initialize a global dictionary of images. Called once to mem
"""


def loadImages():
    pieces = ["Chess_rdt60", "Chess_ndt60", "Chess_bdt60", "Chess_qdt60", "Chess_kdt60", "Chess_bdt60",
              "Chess_ndt60", "Chess_rdt60", "Chess_pdt60", "Chess_rlt60", "Chess_nlt60", "Chess_blt60", "Chess_qlt60",
              "Chess_klt60", "Chess_blt60", "Chess_rlt60", "Chess_plt60"]
    for piece in pieces:
        IMAGES[piece] = p.image.load("Chess Pieces/" + piece + ".png")
        # Note: access an image by saying 'IMAGES ['Chess bdt60']'


'''
The main driver for our code. This will handle user input and updating our graphics
'''


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()  # once before while loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.quit():
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


"""
Responsible for all the graphics within a current game state.
"""


def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)  # Drawing on top of the squares


"""
Draws the squares on the board
"""


def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


"""
Draw the pieces on the board using the current GameState,board
"""


def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "==":
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


print(5*10)


if __name__ == "__main__":
    main()
