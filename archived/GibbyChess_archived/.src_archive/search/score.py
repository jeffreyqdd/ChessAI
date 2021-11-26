
import chess

class Score:
    WHITE_MATE = 1
    NO_MATE = 0
    BLACK_MATE = -1

    def __init__(self, evaluation:float, mate_in:int, mate_type:int, turn:chess.Color):
        self.evaluation = evaluation
        self.mate_in = mate_in
        self.mate_type = mate_type
        self.turn = turn


    # comparisions for white
    # if no mate --> prefer higher evaluation score
    # if white mate --> prefer closer mate
    # if black mate --> prefer further black mate or non mate score

    # comparisons for black
    # if no mate --> prefer lower evaluation score 
    # if white mate --> prefer further white mate or non mate score
    # if black mate --> prefer closer mate

    # we can only compare scores of like turns
    def __lt__(self, other:'Score'):
        assert self.turn == other.turn
        if self.turn == chess.WHITE:
            pass
        else:
            pass