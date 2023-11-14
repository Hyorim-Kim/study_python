# LinearRegression 클래스를 사용해 선형회귀모델 작성
# 보통 독립변수만 표준화 함

from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, explained_variance_score, mean_squared_error
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler

# 편차가 큰 표본 데이터를 생성
sample_size = 100

np.random.seed(1)
x = np.random.normal(0, 10, sample_size)
y = np.random.normal(0, 10, sample_size)  + x * 30
print(x[:10])
print(y[:10])
print('상관계수 : ', np.corrcoef(x, y))  # 0.99939357

scaler = MinMaxScaler()  # 정규화
x_scaled = scaler.fit_transform(x.reshape(-1, 1))
print(x_scaled[:10].flatten())  # 2차원 => 1차원

# 시각화
# plt.scatter(x_scaled, y)
# plt.show()

model = LinearRegression().fit(x_scaled, y)
print(model)
y_pred = model.predict(x_scaled)
print('예측값 : ', y_pred[:10])
print('실제값 : ', y[:10])

# 모델 성능 확인
# print(model.summary())  # 'summary' 지원 X
def regScoreFunc(y_true, y_pred):
    print('r2_score(결정계수, 설명력) : {}'.format(r2_score(y_true, y_pred)))  # **
    print('explained_variance_score(설명분산점수) : {}'.format(explained_variance_score(y_true, y_pred)))
    print('mean_squared_error(MSE, 평균제곱근오차) : {}'.format(mean_squared_error(y_true, y_pred)))

regScoreFunc(y, y_pred)  # 실제값, 예측값
# r2_score(결정계수, 설명력) : 0.9987875127274646
# explained_variance_score(설명분산점수) : 0.9987875127274646  # 결정계수와 설명분산점수의 결과의 차이(편향)가 크다면 모델 학습이 잘못됐다고 봄
# mean_squared_error(MSE, 평균제곱근오차, SSE와 같음) : 86.14795101998743
# 평균제곱근오차 : 잔차 제곱의 합이 작을수록 좋음(값이 작아야 함)

print('------------------------------')
# 분산이 크게 다른 표본 데이터를 생성
x = np.random.normal(0, 1, sample_size)
y = np.random.normal(0, 500, sample_size) + x * 30
print(x[:10])
print(y[:10])
print('상관계수 : ', np.corrcoef(x, y))  # 0.00401167

scaler = MinMaxScaler()  # 정규화
x_scaled2 = scaler.fit_transform(x.reshape(-1, 1))
print(x_scaled2[:10].flatten())  # 2차원 => 1차원

model2 = LinearRegression().fit(x_scaled2, y)
y_pred2 = model2.predict(x_scaled2)
print('예측값 : ', y_pred2[:10])  # 예측값 제대로 안나옴(좋은 모델이 아니기 때문)
print('실제값 : ', y[:10])
regScoreFunc(y, y_pred2)
# r2_score(결정계수, 설명력) : 1.6093526521765433e-05
# explained_variance_score(설명분산점수) : 1.6093526521765433e-05
# mean_squared_error(MSE, 평균제곱근오차) : 282457.9703485092
