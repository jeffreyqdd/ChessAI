
from abc import ABC, abstractclassmethod
import datetime

from keras import Model, optimizers
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D, BatchNormalization
from keras.models import Sequential

from typing import List


class ValueNetwork:
    def __init__(self, name:str, network:Model):
        self.name = name
        self.network = network


    def train(self, X, y, epochs:int, verbose:int) -> None:
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

        history = self.network.fit(X, y, epochs=epochs, verbose=verbose, callbacks=[checkpoint, es])

        return history

    def predict(self, x):
        return self.network.predict(x)

    def load_weights(self, filename):
        self.network.load_weights(filepath=filename)

class ModelBuilder:
    def build_model_1():
        model = Sequential()
        model.add(Conv2D(filters=64, kernel_size=1, activation='relu', input_shape=(12,8,8)))
        model.add(MaxPooling2D())
        model.add(Conv2D(filters=24, kernel_size=1, activation='relu'))
        model.add(MaxPooling2D())
        model.add(Conv2D(filters=10, kernel_size=1, activation='relu'))
        model.add(Flatten())
        model.add(BatchNormalization())
        model.add(Dense(1,activation = 'tanh'))
        model.compile(optimizer='Nadam', loss='mse', metrics=['accuracy'])
        return ("gibbyv1", model)