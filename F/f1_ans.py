import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam

#converting input for the model
def conv_input(i):
    return [1, i, i+i, i*i]
x_train = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_train = np.array([5*i**2 + 7*i + 9 for i in x_train])
x_train_expanded = np.array([conv_input(i) for i in x_train])
print(x_train_expanded.shape)
print(y_train.shape)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(100, input_shape=(4,), activation='relu'),
    tf.keras.layers.Dense(50, activation='relu'),
    tf.keras.layers.Dense(20, activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(loss='mean_squared_error', optimizer = Adam())

model.fit(x_train_expanded, y_train, epochs=5000, batch_size=11)



print(y_train)
for i in x_train:
    prediction = model.predict([conv_input(i)])
    result = prediction[0][0]
    print('Input : ', i, ', Output : ', round(result))