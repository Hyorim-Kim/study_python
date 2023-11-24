# 다중선형회귀분석
# tensorboard : 머신러닝 실험을 위한 시각화 툴킷(toolkit)입니다.
# TensorBoard를 사용하면 손실 및 정확도와 같은 측정 항목을 추적 및 시각화하는 것, 모델 그래프를 시각화하는 것,
# 히스토그램을 보는 것, 이미지를 출력하는 것 등이 가능합니다.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers

# 5명이 치른 세 번의 시험줌수로 다음번 시험 점수 예측
x_data = np.array([[70, 85, 80], [71, 89, 78], [50, 85, 60], [55, 25, 50], [50, 35, 10]])  # 2차원
y_data = np.array([73, 82, 72, 50, 34])  # 1차원

print('1) Sequential api ----')
model = Sequential()  # 순차적으로 노드를 쌓음
model.add(Dense(units=6, input_dim=3, activation='linear', name="a"))  # input layer 3개로 들어와서 6개로 나감
model.add(Dense(units=3, activation='linear', name="b"))
model.add(Dense(units=1, activation='linear', name="c"))
print(model.summary())

opti = optimizers.Adam(learning_rate=0.01)  # 모델 생성
model.compile(optimizer=opti, loss='mse', metrics=['mse'])  # 모델 생성 후 컴파일
history = model.fit(x_data, y_data, batch_size=1, epochs=50, verbose=2)  # 학습
print(history.history['loss'])  # loss는 작을 수록 좋음, 학습을 통해 w값을 조정해 loss값 낮춤

# plt.plot(history.history['loss'])  # 28line 시각화
# plt.xlabel('epochs')
# plt.ylabel('loss')
# plt.show()  # epochs = 50, 굳이 50번 수행안해도 괜찮음
# 결과가 고정되어있지 않기 때문에 다시 실행 시 다르게 나올 수 있음 => 모델 고정해야함
# 보고서에 필요한 자료. 시각화 중요 *

# 설명력 확인
# evaluate는 fit과 batch_size를 똑같이 줘야함
loss_metrics = model.evaluate(x_data, y_data, batch_size=1, verbose=0)
print('loss_metrics : ', loss_metrics)
# train과 test의 차이가 크면 underfitting, 거의 동일하면 overfitting
# 일반적으로 train이 test보다 조금 더 잘나옴
from sklearn.metrics import r2_score
print('설명력 : ', r2_score(y_data, model.predict(x_data)))  # 0.927

print('2) functional api ----')
from keras.layers import Input
from keras.models import Model

inputs = Input(shape=(3,))
output1 = Dense(6, activation='linear', name='a')(inputs)
output2 = Dense(3, activation='linear', name='b')(output1)
output3 = Dense(1, activation='linear', name='c')(output2)
model2 = Model(inputs, output3)
print(model2.summary())

opti = optimizers.Adam(learning_rate=0.01)  # 모델 생성
model2.compile(optimizer=opti, loss='mse', metrics=['mse'])  # 모델 생성 후 컴파일

# TensorBoard
from keras.callbacks import TensorBoard

tb = TensorBoard(
    log_dir="./my",
    histogram_freq=1,
    write_graph=True,
    write_images=False,
    write_steps_per_second=False,
    update_freq='epoch',
    profile_batch=2,
    embeddings_freq=1
)

history = model2.fit(x_data, y_data, batch_size=1, epochs=50, verbose=1, callbacks=[tb])
print(history.history['loss'])

# 설명력 확인
# evaluate는 fit과 batch_size를 똑같이 줘야함
loss_metrics = model2.evaluate(x_data, y_data, batch_size=1, verbose=0)
print('loss_metrics : ', loss_metrics)
print('설명력 : ', r2_score(y_data, model2.predict(x_data)))

# 새로운 값 예측
x_new = np.array([[30, 35, 30], [5, 7, 88]])
print('예상 점수 : ', model2.predict(x_new).flatten())  # 차원 떨어뜨림
