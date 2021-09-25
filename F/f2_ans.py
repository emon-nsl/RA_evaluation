import numpy as np
import tensorflow as tf
import tensorflow.keras as K
from tensorflow.keras.layers import Input, Conv2D, Dense, Add, Flatten, InputLayer
from tensorflow.nn import relu
from tensorflow.keras.optimizers import Adam


imgx,imgy, img_chnl = 128,128, 3

input_1 = np.random.rand(100,imgx, imgy, img_chnl)
input_2 = np.random.rand(100,imgx, imgy, img_chnl)

y_target = np.random.randint(low=0, high=10, size=(100, 1))
# print(y_target)
# exit(0)
# input1 = InputLayer(input_shape = (imgx, imgy))
input1 = Input(shape = (imgx,imgy, img_chnl),name= "first_input" )
input2 = Input(shape = (imgx,imgy, img_chnl), name= "second_input")

conv_x = Conv2D(filters=4,kernel_size=3,strides=2,padding='same',name='conv_x')(input1)
relu_x = relu(conv_x)

conv_y = Conv2D(filters=4,kernel_size=3,strides=2,padding='same',name='conv_y')(input2)
relu_y = relu(conv_y)

add = Add()([relu_x,relu_y])

conv_z = Conv2D(filters=16,kernel_size=3,strides=2,padding='same',name='conv_z')(add)

relu_z = relu(conv_z)

flten = Flatten()(relu_z)

clsification = Dense(1,activation='relu')(flten)

model  = tf.keras.Model([input1,input2],clsification)

print(model.summary())
# model.compile()
model.compile(loss='mean_squared_error', optimizer = Adam())


model.fit([input_1, input_2], y_target, epochs=100, batch_size=16)


#single prediction
inp1, inp2 = input_1[0], input_2[0]
inp1, inp2 = np.expand_dims(inp1, axis=0), np.expand_dims(inp2, axis=0)
# print(inp1.shape, inp2.shape, 'shapes')
prediction = model.predict([inp1, inp2])
print(prediction)

