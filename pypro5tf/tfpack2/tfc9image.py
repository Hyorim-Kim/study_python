# 이미지 분류 모델 작성
# MNIST dataset(흑백 : 28 * 28)을 사용
# Mnist 데이타셋에는 총 60,000개의 데이타가 있는데, 이 데이타는 크게 아래와 같이 세종류의 데이타 셋으로 나눠 집니다.
# 모델 학습을 위한 학습용 데이타인 mnist.train 그리고, 학습된 모델을 테스트하기 위한 테스트 데이타 셋은 minst.test,
# 그리고 모델을 확인하기 위한 mnist.validation 데이타셋으로 구별됩니다.
# 각 데이타는 아래와 같이 학습용 데이타 55000개, 테스트용 10,000개, 그리고, 확인용 데이타 5000개로 구성되어 있습니다.

import tensorflow as tf
import keras
import sys
import numpy as np

(x_train, y_train),(x_test, y_test) = keras.datasets.mnist.load_data()
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)  # (60000, 28, 28) (60000,) (10000, 28, 28) (10000,)
print(x_train[0])  # 0번째 feature
print(y_train[0])  # 0번째 label
# for i in x_train[0]:
#     for j in i:
#         sys.stdout.write('%s  '%j)
#     sys.stdout.write('\n')

# import matplotlib.pyplot as plt
# plt.imshow(x_train[100], cmap='gray')
# plt.show()

print(x_train[0].shape)
x_train = x_train.reshape(60000, 784).astype('float32')  # 28 * 28 ==> 784 1차원배열
x_test = x_test.reshape(10000, 784).astype('float32')
print(x_train[0], x_train[0].shape)

x_train /= 255.0  # 정규화 : 필수는 아님. 권장
x_test /= 255.0
print(x_train[0])  # 모든 데이터가 0~1영역 안으로 들어옴

# label은 softmax를 사용하기 때문에 one-hot 처리
print(y_train[0])
y_train = keras.utils.to_categorical(y_train, 10)  # num_classes = 10
y_test = keras.utils.to_categorical(y_test, num_classes=10)
print(y_train[0])

# train data의 일부(1만개)를 validation data로 사용
x_val = x_train[50000:60000]
y_val = y_train[50000:60000]
x_train = x_train[0:50000]
y_train = y_train[0:50000]
print(x_train.shape, x_val.shape)

# model
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten, Dropout

model = Sequential()
'''
model.add(Dense(units=128, input_shape=(784,)))  # reshape을 한 경우
# model.add(Flatten(input_shape=(28,28)))  # reshape을 하지 않은 경우  **
# model.add(Dense(units=128))
model.add(Activation('relu'))
model.add(Dropout(rate=0.2))  # 과적합 방지 : 서로 연결된 연결망(layer)에서 0부터 1 사이의 확률로 뉴런을 제거하는 기법

model.add(Dense(units=64))
model.add(Activation('relu'))

model.add(Dense(units=10))
model.add(Activation('softmax'))
'''

model.add(Dense(units=128, input_shape=(784,), activation='relu'))
# model.add(Flatten(input_shape=(28,28)))
model.add(Dropout(rate=0.2))  # 과적합 방지
model.add(Dense(units=64, activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)))
# regularizers.l2(0.001) 정규화를 통해 학습 시 가중치가 커지는 경우에 penalty를 부과하여 과적합 방지
model.add(Dropout(rate=0.2))  # 과적합 방지
model.add(Dense(units=10, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# one-hot처리를 했으니까 categorical_crossentropy 사용
print(model.summary())

history = model.fit(x=x_train, y=y_train, epochs=10, batch_size=128, \
                                    validation_data=(x_val, y_val), verbose=2)
print('loss : ', history.history['loss'])
print('val_loss : ', history.history['val_loss'])
print('accuracy : ', history.history['accuracy'])
print('val_accuracy : ', history.history['val_accuracy'])

# 시각화
import matplotlib.pyplot as plt
plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label='val_loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend()
plt.show()

plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('epochs')
plt.ylabel('accuracy')
plt.legend()
plt.show()

# 모델 평가
score = model.evaluate(x=x_test, y=y_test, batch_size=128, verbose=0)
print('score loss : ', score[0])
print('score accuracy : ', score[1])

# 모델 저장
model.save('tfc9model.hdf5')

print('----------------------')
mymodel = keras.models.load_model('tfc9model.hdf5')

plt.imshow(x_test[:1].reshape(28, 28), cmap='gray')
plt.show()

pred = mymodel.predict(x_test[:1])
print('예측값 : ', pred)
print('예측값 : ', np.argmax(pred,axis=1))
print('실제값 : ', y_test[:1])
print('실제값 : ', np.argmax(y_test[:1], axis=1))
