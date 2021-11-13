#!/Users/jeffrey/Projects/ChessAI/GibbyServer/env/bin/python
from abc import ABC, abstractclassmethod
from keras.callbacks import History
import numpy as np

class BaseModel(ABC):
    def __init__(self):
        pass

    def train(self, X, y, epochs:int, verbose:int) -> History:
        raise NotImplementedError()

    def predict(self, x:np.ndarray):
        raise NotImplementedError()

    def load_weights(self, filename:str) -> None:
        raise NotImplementedError()
