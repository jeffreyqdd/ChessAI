#!/Users/jeffrey/Projects/ChessAI/GibbyServer/env/bin/python

import numpy as np
from collections import namedtuple

from keras import Model, optimizers
from keras.models import Sequential
from keras.callbacks import History, ModelCheckpoint, EarlyStopping
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D, BatchNormalization

from src.model.base import BaseModel

ValueConfig = namedtuple('ValueConfig', 'name model')

class ValueBuilder:
    def build_conv2d_default() -> ValueConfig:
        model:Model = Sequential()
        model.add(Conv2D(filters=64, kernel_size=1, activation='relu', input_shape=(12,8,8)))
        model.add(MaxPooling2D())
        model.add(Conv2D(filters=24, kernel_size=1, activation='relu'))
        model.add(MaxPooling2D())
        model.add(Conv2D(filters=10, kernel_size=1, activation='relu'))

        model.add(Flatten())
        model.add(BatchNormalization())
        model.add(Dense(1,activation = 'tanh'))
        model.compile(optimizer='Nadam', loss='mse')

        return ValueConfig(name='default_gibby', model = model)

class ValueNetwork(BaseModel):
    def __init__(self, config: ValueConfig) -> None:
        super().__init__()
        self.name:str = config.name
        self.model:Model = config.model

    def train(self, X, y, epochs:int, verbose:int) -> History:
        h5 = f'bin/{self.name}.h5'
        checkpoint = ModelCheckpoint(h5,
                        monitor='loss',
                        verbose=0,
                        save_best_only=True,
                        save_weights_only=True,
                        mode='auto',
                        period=1
                    )
        es = EarlyStopping(monitor='loss', mode='min', verbose=1, patience=5000/10)
        history = self.model.fit(X, y, epochs=epochs, verbose=verbose, callbacks=[checkpoint, es])
        return history

    def predict(self, x:np.ndarray):
        return self.model.predict(x)

    def load_weights(self, filename:str) -> None:
        self.model.load_weights(filepath=filename)
