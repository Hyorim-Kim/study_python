# CNN은 Convolutional Neural Networks의 약자로 딥러닝에서 주로 이미지나 영상 데이터를 처리할 때 쓰이며
# 이름에서 알수있다시피 Convolution이라는 전처리 작업이 들어가는 Neural Network 모델
# 특징추출 알고리즘 사용 : 이미지나 텍스트 데이터를 conv와 pooling을 반복하여 데이터 양을 줄인 후 완전연결층으로 전달해 분류작업

import tensorflow as tf
import keras
import sys
import numpy as np

(x_train, y_train),(x_test, y_test) = keras.datasets.mnist.load_data()
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)  # (60000, 28, 28) (60000,) (10000, 28, 28) (10000,)
print(x_train[0])  # 0번째 feature
print(y_train[0])  # 0번째 label

# cnn은 채널(channel)을 사용하므로 3차원을 4차원으로 변환
x_train = x_train.reshape((60000, 28, 28, 1))  # (-1, 28, 28, 1)
x_test = x_test.reshape((10000, 28, 28, 1))  # (-1, 28, 28, 1)
print(x_train.shape, x_test.shape)  # (60000, 28, 28, 1) (10000, 28, 28, 1)
print(x_train[:1])  # [[[[  0]   [  0] ...

x_train = x_train / 255.0
x_test = x_test / 255.0

# 모델 (CNN : 고해상도, 크기가 큰 이미지를 전처리 후 작은 이미지로 변환 후 ==> Dense(완전연결층으로 전달)로 분류 진행
print('방법3 : subclassing API 사용')
import keras

class MyModel(keras.Model):
    def __init__(self):
        super(MyModel, self).__init__()
        self.conv1 = keras.layers.Conv2D(filters=16, kernel_size=[3,3], padding='valid', activation='relu')
        self.pool1 = keras.layers.MaxPool2D((2,2))
        self.drop1 = keras.layers.Dropout(0.3)

        self.conv2 = keras.layers.Conv2D(filters=16, kernel_size=[3,3], padding='valid', activation='relu')
        self.pool2 = keras.layers.MaxPool2D((2,2))
        self.drop2 = keras.layers.Dropout(0.3)

        self.flatten = keras.layers.Flatten(dtype='float32')

        self.d1 = keras.layers.Dense(64, activation='relu')
        self.drop3 = keras.layers.Dropout(0.3)

        self.d2 = keras.layers.Dense(10, activation='softmax')

    def call(self, inputs):
        net = self.conv1(inputs)
        net = self.pool1(net)
        net = self.drop1(net)

        net = self.conv2(net)
        net = self.pool2(net)
        net = self.drop2(net)

        net = self.flatten(net)
        
        net = self.d1(net)
        net = self.drop3(net)
        
        net = self.d2(net)
        return net

model = MyModel()
temp_inputs = keras.layers.Input(shape=(28,28,1))
model(temp_inputs)

print(model.summary())
