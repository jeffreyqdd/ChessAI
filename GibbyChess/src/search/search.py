import chess
import uuid
import time
from keras.layers.pooling import MaxPooling2D
import numpy as np
from numpy.lib.arraysetops import isin
from tqdm import tqdm
from typing import List

from src.search.score import Eval, Mate, Score
from src.models.model import GibbyModel, ModelBuilder
from src.utils.translate import Translate

from src.config.globals import STOCKFISH
import chess.engine

class Node:
    def __init__(
        self, 
        parent:'Node' = None,
        board:chess.Board = None,
        evaluation:Score = None,
        children:List['Node'] = []
    ):
        self.parent:Node = parent
        self.board:chess.Board = board
        self.evaluation:Score = evaluation
        self.children:List['Node'] = children
    
    def has_children(self):
        return len(self.children) > 0

    def get_sorted_children(self, reverse=False):
        self.children.sort(reverse=reverse)
        return self.children

    def __str__(self):
        return f"Node({str(self.evaluation)}, children={len(self.children)})"

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other:'Node'):
        return self.evaluation < other.evaluation

class IterativeDeepeningSearchFramework:
    def __init__(self, evaluation_model:GibbyModel):
        self.evaluation_model:GibbyModel = evaluation_model
        self.engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH)

    def iterative_deepening(self, board:chess.Board, max_depth:int=8, timeout=100_000):
        assert max_depth >= 1

        # create root node
        root = Node(parent=None, board=board)

        start_time = time.time()
        for i in range(1, max_depth+1):
            # if there is not enough time to perform this search
            if time.time() - start_time >= timeout:
                break

            # search node
            
            start = time.time()
            self.__alpha_beta(
                node = root,
                board = board.copy(),
                depth = i,
                alpha = Mate(0, False, True),
                beta = Mate(0, True, False),
                maximizing=board.turn
            )
            end = time.time()
            print(end - start)

            # walk up node
            while root.parent is not None:
                root = root.parent

    def __alpha_beta(self,
    node:Node,
    board:chess.Board,
    depth:int,
    alpha:Score,
    beta:Score,
    maximizing:bool) -> Score:
        ### 1) end node
        # mate
        if depth == 0:
            return node.evaluation

        ### 2) expand if on leaf
        if not node.has_children():
            list_moves = list(board.legal_moves)
            node.children = [None] * len(list_moves)


            # queue evaluation
            for idx, move in tqdm(enumerate(list_moves)):
                board.push(move)
                # create node
                new_node = Node(parent=node)

                # create children
                new_node.board = board.copy()
            
                # create score
                if board.is_checkmate():
                    new_node.evaluation = Mate(mate_in=0, mate_side=maximizing, turn=not maximizing)
                # stalemate or insufficient material
                elif board.is_stalemate() or board.is_insufficient_material():
                    new_node.evaluation = Eval(evaluation=0, turn=not maximizing)
                else:
                    res:chess.engine.PovScore = self.engine.analyse(board, chess.engine.Limit(depth=1))['score']
                    if res.is_mate():
                        new_node.evaluation = Mate(mate_in=0, mate_side=maximizing, turn=not maximizing)
                    else:
                        new_node.evaluation = Eval(
                            float(res.white().cp), #self.evaluation_model.predict( np.array([Translate.board_to_matrix3d(board)]) )[0][0],
                            turn = not maximizing
                        )
                node.children[idx] = new_node
                board.pop()

        if maximizing: 
            # worst score - mate is being given
            value = Mate(0, False, True)
            for child in node.get_sorted_children():
                result = self.__alpha_beta(
                        node = child,
                        board = child.board,
                        depth = depth-1,
                        alpha = alpha,
                        beta = beta,
                        maximizing = False,
                    ).get_propagated_score()

                value = max(value, result)

                node.evaluation = value

                if value > beta.get_propagated_score():
                    break

                alpha = max(alpha, value)
                
            return value
                

        else:
            value = Mate(0, True, False)

            for child in node.get_sorted_children():
                value = max(value,
                    self.__alpha_beta(
                        node = child,
                        board = child.board,
                        depth = depth-1,
                        alpha = alpha,
                        beta = beta,
                        maximizing = True,
                    ).get_propagated_score()
                )
                
                node.evaluation = value

                if value > alpha.get_propagated_score():
                    break

                beta = max(beta, value)
            
            return value

    def __del__(self):
        self.engine.quit()
    

if __name__ == '__main__':
    model = GibbyModel(*ModelBuilder.build_model_1())
    model.load_weights('src/models/bin/gibbyv1.h5')

    x = IterativeDeepeningSearchFramework(evaluation_model=model)
    x.iterative_deepening(board=chess.Board(), max_depth=4)
    x.__del__()