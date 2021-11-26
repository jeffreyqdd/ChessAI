from keras import optimizers
from keras.layers import (LSTM, BatchNormalization, Dense, Dropout, Flatten,
                          TimeDistributed)
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.models import Sequential, load_model, model_from_json

def build_model_1():

    model = Sequential()
    model.add(Conv2D(filters=64, kernel_size=1, activation='relu', input_shape=(8,8,12)))
    model.add(MaxPooling2D())
    model.add(Conv2D(filters=24, kernel_size=1, activation='relu'))
    model.add(MaxPooling2D())
    model.add(Conv2D(filters=10, kernel_size=1, activation='relu'))
    model.add(Flatten())
    model.add(BatchNormalization())
    model.add(Dense(1,activation = 'tanh'))
    model.compile(optimizer='Nadam', loss='mse')

    return model
