# CNN은 Convolutional Neural Networks의 약자로 딥러닝에서 주로 이미지나 영상 데이터를 처리할 때 쓰이며
# 이름에서 알수있다시피 Convolution이라는 전처리 작업이 들어가는 Neural Network 모델
# 특징추출 알고리즘 사용 : 이미지나 텍스트 데이터를 conv와 pooling을 반복하여 데이터 양을 줄인 후 완전연결층으로 전달해 분류작업
# 가급적이면 sequential api보다 functional api 사용하기 **

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
input_shape = (28, 28, 1)

print('방법2 : functional API 사용')
img_input = keras.layers.Input(shape=input_shape)

net = keras.layers.Conv2D(filters=16, kernel_size=(3,3), strides=(1,1), activation='relu')(img_input)
net = keras.layers.MaxPooling2D(pool_size=(2,2))(net)
net = keras.layers.Dropout(rate=0.3)(net)

net = keras.layers.Conv2D(filters=32, kernel_size=(3,3), strides=(1,1), activation='relu')(img_input)
net = keras.layers.MaxPooling2D(pool_size=(2,2))(net)
net = keras.layers.Dropout(rate=0.3)(net)

net = keras.layers.Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), activation='relu')(img_input)
net = keras.layers.MaxPooling2D(pool_size=(2,2))(net)
net = keras.layers.Dropout(rate=0.3)(net)

net = keras.layers.Flatten()(net)

net = keras.layers.Dense(units=64, activation='relu')(net)
net = keras.layers.Dropout(rate=0.2)(net)

net = keras.layers.Dense(units=32, activation='relu')(net)
net = keras.layers.Dropout(rate=0.2)(net)

outputs = keras.layers.Dense(units=10, activation='softmax')(net)

model = keras.Model(inputs=img_input, outputs=outputs)

print(model.summary())

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

from keras.callbacks import EarlyStopping
es = EarlyStopping(monitor='val_loss', patience=3)  # 보통 10

history = model.fit(x_train, y_train, batch_size=128, epochs=100, verbose=1, validation_split=0.2, callbacks=[es])

print(history.history)

# 모델 평가
train_loss, train_acc = model.evaluate(x_train, y_train)
test_loss, test_acc = model.evaluate(x_test, y_test)
print('train_loss, train_acc : ', train_loss, train_acc)
print('test_loss, test_acc : ', test_loss, test_acc)
# 둘이 차이가 많이 안나야함
print()
print('예측값 : ', np.argmax(model.predict(x_test[:1])))
print('예측값 : ', np.argmax(model.predict(x_test[[0]])))  # 상동
print('실제값 : ', y_test[0])

# -----------------------------------------------------------
import pickle
history = history.history  # history를 객체로 저장
with open('tfc12his.pickle', 'wb') as obj:
    pickle.dump(history, obj)
    
with open('tfc12his.pickle', 'rb') as obj:
    history = pickle.load(obj)
# -----------------------------------------------------------

# 시각화
import matplotlib.pyplot as plt

def plot_acc(title = None):
    plt.plot(history['accuracy'], label='accuracy')
    plt.plot(history['val_accuracy'], label='val_accuracy')
    plt.title(title)
    plt.legend()

plot_acc('accuracy')
plt.show()

def plot_loss(title = None):
    plt.plot(history['loss'], label='loss')
    plt.plot(history['val_loss'], label='val_loss')
    plt.title(title)
    plt.legend()

plot_loss('loss')
plt.show()
