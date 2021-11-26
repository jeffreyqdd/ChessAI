import numpy as np
from tqdm import tqdm
import chess.pgn
import chess
from typing import List

from src.utils.translate import Translate


class DatasetManager:
    def create_dataset(games:List[chess.pgn.Game], verbose:bool=True):
        # cnt = 0
        X = []
        y = []

        for game in (tqdm(games, desc = "Generating Dataset: ") if verbose else games):
            # establish winner
            if game.headers['Result'] == '1-0':
                outcome = 1
            elif game.headers['Result'] == '0-1':
                outcome = -1
            else:
                outcome = 0


            board = chess.Board()
            for move in game.mainline_moves():
                board.push(move)

                X.append(
                    Translate.board_to_matrix3d(board)
                )
                y.append(outcome)

        X = np.array(X)
        y = np.array(y)

        return X, y