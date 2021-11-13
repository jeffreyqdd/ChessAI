# not a traditional unittest because the output cannot be verified
# more of a visualization for the user!
# from src.utils.pgnparse import PgnParser
# from src.utils.dataset import DatasetManager
# from src.models.model import GibbyModel, ModelBuilder
# from src.config.globals import PGN_MASTER_DATA

import cairosvg
import cv2
import io
from PIL import Image
import numpy as np
from src.config.globals import STOCKFISH
from src.models.model import GibbyModel, ModelBuilder
from src.utils.translate import Translate

import chess, chess.engine, chess.svg
import random




if __name__ == '__main__':
    ### run using: python model_test.py

    # create play a game and simulate it   
    board = chess.Board()

    # create engine instance
    with chess.engine.SimpleEngine.popen_uci(STOCKFISH) as engine:
        # create GibbyModel instance
        gibby = GibbyModel(*ModelBuilder.build_model_1())
        gibby.load_weights('src/models/bin/gibbyv2.h5')

        # simulate until board game is over
        while True:
            ### evaluate current chess position
            stockfish_nnue = engine.analyse(board, chess.engine.Limit(depth=5))['score'].white()

            gibby_nn = gibby.predict(np.array([Translate.board_to_matrix3d(board)])) [0]
            
            ### render board and put evaluation texts
            # render
            svg = chess.svg.board(board=board, size=600)
            png = cairosvg.svg2png(svg)
            imageFile = Image.open(io.BytesIO(png)).convert('RGB')
            image = cv2.cvtColor(np.array(imageFile) , cv2.COLOR_RGB2BGR)

            # texts
            image = cv2.putText(
                img=image,
                text=str(stockfish_nnue) + "   " + str(gibby_nn),
                org=(0,50),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=0.7,
                color=(255, 255, 0),
                thickness=2
            )
         

            # display
            cv2.imshow('window', image)
            k = cv2.waitKey(1) # current catched key

            if k == ord('q'):
                board.pop()
            elif k == ord('e'):
                ### make next move?
                if board.is_game_over():
                    # stop
                    break
                else:
                    # make random move
                    board.push(random.choice(list(board.legal_moves)))




            


        
       