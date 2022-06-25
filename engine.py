import numpy as np

"""
Stores all information about the state of the current game
"""

class GameState:
    
    def __init__(self):
        self.board = [["bR","bN","bB","bQ","bK","bB","bN","bR"],
                     ["bP","bP","bP","bP","bP","bP","bP","bP"],
                     ["--","--","--","--","--","--","--","--"],
                     ["--","--","--","--","--","--","--","--"],
                     ["--","--","--","--","--","--","--","--"],
                     ["--","--","--","--","--","--","--","--"],
                     ["wP","wP","wP","wP","wP","wP","wP","wP"],
                     ["wR","wN","wB","wQ","wK","wB","wN","wR"]]

        self.absolute_pins = [[0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0], 
                             [0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0]]

        self.WhiteToMove = True
        self.WKingMoved = False
        self.WKSquare = (7,4)
        self.BKingMoved = False
        self.BKSquare = (0,4)
        self.move_log = []

    def make_move(self,move):
        #don't allow player to put themselves in check
        if self.absolute_pins[move.start_row][move.start_col] == 1:
            pass
        else:
            self.board[move.start_row][move.start_col] = "--"
            self.board[move.end_row][move.end_col] = move.piece_moved
            self.move_log.append(move)
            if move.piece_moved == "wK":
                self.WKingMoved = True
                self.WKSquare = (move.end_row,move.end_col)
            if move.piece_moved == "bK":
                self.BKingMoved = True
                self.BKSquare = (move.end_row,move.end_col)

            self.WhiteToMove = not self.WhiteToMove
            self.find_abs_pins()


    def undo(self):
        if len(self.move_log) == 0:
            print("No moves to undo!")
            pass
        else:
            last_move = self.move_log[-1]
            '''
            Replace captured piece and put piece moved back on its initial square
            '''
            self.board[last_move.end_row][last_move.end_col] = last_move.piece_captured
            self.board[last_move.start_row][last_move.start_col] = last_move.piece_moved
            self.move_log.pop() #remove last move

    def find_abs_pins(self):
        pass
        board_array = np.array(self.board)



#generate candidate move
class move:
    '''
    mapping between indices and ranks/files
    '''
    ranks_to_rows = {"1": 7, "2": 6, "3": 5, "4":4,"5":3,"6":2,"7":1,"8":0}
    rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}
    files_to_cols = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}
    cols_to_files = {v: k for k, v in files_to_cols.items()}


    def __init__(self,start_square,end_square,board):
        self.start_row = start_square[0]
        self.start_col = start_square[1]
        self.end_row = end_square[0]
        self.end_col = end_square[1]

        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col] 


    def get_chess_notation(self):
        return self.get_rank_file(self.start_row,self.start_col) + self.get_rank_file(self.end_row,self.end_col)

    def get_rank_file(self,r,c):
        return self.cols_to_files[c] + self.rows_to_ranks[r]
