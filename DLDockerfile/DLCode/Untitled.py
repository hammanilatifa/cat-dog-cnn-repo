#!/usr/bin/env python
# coding: utf-8


from keras.datasets import mnist
from keras.models import Sequential

dataset = mnist.load_data('mymnist.db')

train , test = dataset

X_train,y_train = train

X_test,y_test = test



X_train = X_train.reshape(-1 , 28*28)
X_test = X_test.reshape(-1 , 28*28)

from keras.utils.np_utils import to_categorical

y_train_cat = to_categorical(y_train)
y_test_cat = to_categorical(y_test)

from keras.layers import Dense

model = Sequential()

model.add(Dense(units = 512, activation = 'relu', input_dim = 28*28))


model.add(Dense(units = 256, activation = 'relu'))


model.add(Dense(units = 128, activation = 'relu'))



model.add(Dense(units = 32, activation = 'relu'))


model.add(Dense(units = 10, activation = 'softmax'))


from keras.optimizers import RMSprop


model.compile(optimizer= RMSprop(learning_rate=0.0001),
             loss='categorical_crossentropy',
             metrics=['accuracy'])

model.fit(X_train,y_train_cat,epochs=100)
model.save('/DLCode/handwrittendigitModel.h5')


