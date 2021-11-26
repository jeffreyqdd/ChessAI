import io
import src.config.globals as globals
import chess.pgn
from typing import List
import sys
import warnings
from tqdm import tqdm

class PgnParser:
    """a parser for pgn files"""

    CONSTRAINTS = {
        'termination' : 'Normal',
        'white_elo' : 2200,
        'black_elo' : 2200
    }   

    def __init__(self, filename:str):
        """initializer

        # params:
        - 
        # returns:
        - 

        """
        self.filename:str = filename
        self.file:io.FileIO = open(filename, 'r')

    def read_batch_from_file(self, batch_size=10_000, verbose:bool=True):
        ret:List[chess.pgn.Game] = [None] * batch_size
        for i in (tqdm(range(batch_size), desc = "Parsing PGN File: ") if verbose else range(batch_size)):
            game = chess.pgn.read_game(self.file)

            if game is None:
                msg = (
                    f"Warning: eof before batch_size={batch_size} could be reached." + 
                    f" Will proceed with batch size of {i}"
                )
                warnings.warn(msg, RuntimeWarning)
                return ret[:i], True

            ret[i] = game

        return ret, False


    def filter_batch(self, batch:List[chess.pgn.Game], termination:str, white_elo:int, black_elo:int, verbose=True):
        ret:List[chess.pgn.Game] = []
        for game in (tqdm(batch, desc="Filtering Batch: ") if verbose else batch):
            if game.headers['Termination'] != termination:
                continue
            if int(game.headers['BlackElo']) < black_elo or int(game.headers['WhiteElo']) < white_elo:
                continue
            ret.append(game)

        return ret

    def write_batch(self, filename:str, batch:List[chess.pgn.Game], verbose=True):
        with open(filename, "a") as file:
            for game in (tqdm(batch, desc='Writing Batch:') if verbose else batch):
                print(game, file=file, end="\n\n")
    
    def reset_write_file(self, filename:str):
        file = open(filename,"w")
        file.close()
    
    def __del__(self):
        self.file.close()



if __name__ == "__main__":
    # if called as main, pgnparser will generate data for model training. 
    # currently filters for 2200+ elo players from games containing 1800+ elo players

    GUARD = True # guards against accidental execuation of this code

    if GUARD:
        warnings.warn("Terminating to guard against overwritting", RuntimeWarning)

    else:
        parser = PgnParser(globals.PGN_ADVANCED_DATA)
        parser.reset_write_file(filename=globals.PGN_MASTER_DATA)
        isDone = False
        while not isDone:
            x, isDone = parser.read_batch_from_file(batch_size=10_000)
            y = parser.filter_batch(batch=x, **PgnParser.CONSTRAINTS)
            parser.write_batch(filename=globals.PGN_MASTER_DATA, batch=y)
