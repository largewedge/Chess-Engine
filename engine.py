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

        self.WhiteToMove = True
        self.move_log = []
