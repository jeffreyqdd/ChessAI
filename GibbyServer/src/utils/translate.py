import numpy as np
import chess

# see: https://chess.stackexchange.com/questions/29294/quickly-converting-board-to-bitboard-representation-using-python-chess-library

class Translate:
    """translates from a chess.Board object into a numpy matrix for the nn to process. 
    """

    def board_to_matrix3d(board:chess.Board):

        """translates board into an array of bits.
        
        # params:
        - board (chess.Board) - board object to translate into array of bitboards

        # returns:
        - (np.ndarray) - bitboard array with dims = (12, 8, 8)
        """

        black, white = board.occupied_co

        bitboards = np.array([
            black & board.pawns,
            black & board.rooks,
            black & board.knights,
            black & board.bishops,
            black & board.queens,
            black & board.kings,
            white & board.pawns,
            white & board.rooks,
            white & board.knights,
            white & board.bishops,
            white & board.queens,
            white & board.kings,
        ], dtype=np.uint64)

        return Translate.__bitboards_to_array(bitboards)

    def __bitboards_to_array(bb: np.ndarray) -> np.ndarray:
        bb = np.asarray(bb, dtype=np.uint64)[:, np.newaxis]
        s = 8 * np.arange(7, -1, -1, dtype=np.uint64)
        b = (bb >> s).astype(np.uint8)
        b = np.unpackbits(b, bitorder="little")
        return b.reshape(-1, 8, 8)

if __name__ == '__main__':
    import time

    print("TESTING TRANSLATE SPEED")
    num_it = 100_000
    board = chess.Board()
    
    start = time.time()
    for i in range(num_it):
        y = Translate.board_to_matrix3d(board)
    stop = time.time()
    total_time = stop - start

    print(f"{num_it} iterations in {total_time}(s).....{num_it / total_time} it/s")

    res = Translate.board_to_matrix3d(board)
    print(res, f"shape = {res.shape}, with dype = {type(res)}")


