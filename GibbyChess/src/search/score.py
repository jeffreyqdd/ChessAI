import chess
from abc import ABC, abstractclassmethod
from typing import List, Tuple, Optional
import math
import chess

class Score(ABC):
    """evaluation of a position"""
    def __init__(self, turn:chess.Color) -> None:
        self.turn = turn

    @abstractclassmethod
    def get_propagated_score(self) -> 'Score':
        """ returns score if node was 1-depth higher
        """
        raise NotImplementedError()
    
    @abstractclassmethod
    def get_score_tuple(self) -> Tuple[int, int, float]:
        """ returns score used for comparison
        - Tuple[1] = 1 same side mate, 0 no mate, -1 opposite side mate
        - Tuple[2] = mate_in
        - Tuple[3] = position_eval
        """
        raise NotImplementedError()

    def __assert_proper_comparison(self, other:'Score') -> None:
        if not self.turn == other.turn:
            raise ValueError("Cannot compare scores of different turns.")

    def __str__(self) -> str:
        raise NotImplementedError()

    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, other:'Score') -> bool:
        self.__assert_proper_comparison(other)
        return self.get_score_tuple() == other.get_score_tuple()

    def __lt__(self, other:'Score') -> bool:
        self.__assert_proper_comparison(other)

        return self.get_score_tuple() < other.get_score_tuple()

    def __le__(self, other:'Score') -> bool:
        self.__assert_proper_comparison(other)
        return self.get_score_tuple() <= other.get_score_tuple()

    def __gt__(self, other:'Score') -> bool:
        self.__assert_proper_comparison(other)
        return self.get_score_tuple() > other.get_score_tuple()

    def __ge__(self, other:'Score') -> bool:
        self.__assert_proper_comparison(other)
        return self.get_score_tuple() >= other.get_score_tuple()

class Mate(Score):
    def __init__(self, mate_in:int, mate_side:bool, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.mate_in = mate_in
        self.mate_side = mate_side

    def get_propagated_score(self) -> 'Score':
        return Mate(
            mate_in = self.mate_in + 1,
            mate_side = self.mate_side,
            turn = not self.turn
        )

    def get_score_tuple(self) -> Tuple[int, int, float]:
        isSameSideMate = 1 if self.mate_side == self.turn else -1
        return [isSameSideMate, -self.mate_in * isSameSideMate, 0]
    
    def __str__(self) -> str:
        colorTxt = "WHITE" if self.mate_side == chess.WHITE else "BLACK"
        return f"Mate({self.mate_in}, {colorTxt})"


class Eval(Score):
    def __init__(self, evaluation:float, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.evaluation = evaluation

    def get_propagated_score(self) -> 'Score':
        return Eval(evaluation=self.evaluation, turn=not self.turn)

    def get_score_tuple(self) -> Tuple[bool, bool, int, float]:
        return [0, 0, self.evaluation * (1 if self.turn == chess.WHITE else -1)]
    
    def __str__(self) -> str:
        colorTxt = "WHITE" if self.turn == chess.WHITE else "BLACK"
        return f"Eval({round(self.evaluation, 2)}, {colorTxt})"

