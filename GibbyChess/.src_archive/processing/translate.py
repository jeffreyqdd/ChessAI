import numpy as np
import chess

class Translate:
    chess_dict = {
        'p' : 0,
        'P' : 6,
        'n' : 1,
        'N' : 7,
        'b' : 2,
        'B' : 8,
        'r' : 3,
        'R' : 9,
        'q' : 4,
        'Q' : 10,
        'k' : 5,
        'K' : 11,

    }

    def board_to_matrix2d(board:chess.Board):
        pgn:str = board.epd()
        pieces:str = pgn.split(" ", 1)[0]
        rows:np.ndarray = pieces.split("/")

        matrix = np.array(
            [
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.']
            ]
            ,dtype=str
        )

        for r, row in enumerate(rows):
            col = 0
            for entry in row:
                if entry.isdigit():
                    col += int(entry)
                else:
                    matrix[r, col] = entry
                    col += 1
        return matrix


    def matrix2d_to_matrix3d(matrix2d):
        # rows, cols, piece types
        matrix3d = np.zeros(shape=(8, 8, 12), dtype=int)
        
        for row in range(8):
            for col in range(8):
                if matrix2d[row, col] == '.':
                    continue 
                else:
                    matrix3d[row, col, Translate.chess_dict[matrix2d[row, col]]] = 1
        return matrix3d