"""
Driver. Handles user input and graphics

"""

import pygame as p
import engine
import numpy as np

#board dimensions
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 90
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

    square_selected = () #no square selected initially. tuple: (row,col)
    player_clicks = []  #array of two clicks

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

            elif e.type == p.MOUSEBUTTONDOWN:
                #returns mouse coordinates (x,y)
                location = p.mouse.get_pos()
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE

                if square_selected == (row,col): #deselect square
                    square_selected = ()
                    player_clicks = []
                else:
                    square_selected = (row,col)
                    if len(player_clicks) == 1: #don't allow player to move 'empty piece' to other squares
                        first_row = player_clicks[0][0]
                        first_col = player_clicks[0][1]
                        if gs.board[first_row][first_col] == "--":
                            player_clicks.pop()

                    player_clicks.append(square_selected)

                if len(player_clicks) == 2:
                    move = engine.move(player_clicks[0],player_clicks[1],gs.board)
                    print(move.get_chess_notation())
                    gs.make_move(move)
                    square_selected = ()
                    player_clicks = []
            elif e.type == p.KEYDOWN:
                if p.K_z:
                    gs.undo()

            draw_game_state(screen,gs,square_selected)
            clock.tick(MAX_FPS)
            p.display.flip()

'''
Graphics
'''

def draw_game_state(screen,gs,square_selected):
    draw_board(screen,square_selected)
    draw_pieces(screen,gs.board)

'''
draw the squares
'''
def draw_board(screen,square_selected):
    colors = [p.Color("white"),p.Color("gray")]
    selection_color = "red"

    for r in range(DIMENSION):
        for c in range(DIMENSION):
            #for light squares, row + col is always even
            if (r,c) == square_selected:
                p.draw.rect(screen,selection_color,p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))
            else:
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
