"""
Driver. Handles user input and graphics

"""

import pygame as p
import engine


#board dimensions
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}


'''
Create image dictionary
'''

def load_images():
    pieces = ['wP','wR','wN','wB','wK','wQ','bP','bR','bN','bB','bK','bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"),(SQ_SIZE,SQ_SIZE))




def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))

    gs = engine.GameState()

    load_images()
    running = True

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = false

            draw_game_state(screen,gs)
            clock.tick(MAX_FPS)
            p.display.flip()

'''
Graphics
'''

def draw_game_state(screen,gs):
    draw_board(screen)
    draw_pieces(screen,gs.board)

'''
draw the squares
'''
def draw_board(screen):
    colors = [p.Color("white"),p.Color("gray")]

    for r in range(DIMENSION):
        for c in range(DIMENSION):
            #for light squares, row + col is always even
            color = colors[((r+c)%2)]
            p.draw.rect(screen,color,p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))

'''
Draw pieces using current gamestate
'''
def draw_pieces(screen,board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))



if __name__ == "__main__":
    main()
