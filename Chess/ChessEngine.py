"""
This class is resposible for storing all the information about the current state of a chess game. It will also be
 responsible for determning the valid moves at the current state. It will also keep a move log.
"""
class GameState():
    def __init__(self):
        #"--" Represents a empty square
        self.board = [
            ["Chess_rdt60", "Chess_ndt60", "Chess_bdt60", "Chess_qdt60", "Chess_kdt60", "Chess_bdt60",
             "Chess_ndt60", "Chess_rdt60"],
            ["Chess_pdt60", "Chess_pdt60", "Chess_pdt60", "Chess_pdt60", "Chess_pdt60", "Chess_pdt60",
             "Chess_pdt60", "Chess_pdt60"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["Chess_rlt60", "Chess_nlt60", "Chess_blt60", "Chess_qlt60", "Chess_klt60", "Chess_blt60",
             "Chess_nlt60", "Chess_rlt60"],
            ["Chess_plt60", "Chess_plt60", "Chess_plt60", "Chess_plt60", "Chess_plt60", "Chess_plt60",
             "Chess_plt60", "Chess_plt60"]]
        self.whiteToMove = True
        self.moveLog= []