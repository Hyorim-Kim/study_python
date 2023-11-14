# 비선형 회귀분석(Non-linear Regression) - 다항회귀
# 데이터가 곡선의 형태로 분포되어 있는 경우에
# 직선의 회귀식(잔차가 큼)을 곡선으로 변환해 보다 더 정확하게 데이터 변화를 예측하는데 그 목적이 있다.
# 더 자세하게 정리하기

# 입력자료 특징/특성(독립변수, feature) 변환으로 선형모델 개선
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics._regression import r2_score

x = np.array([1,2,3,4,5])
y = np.array([4,2,1,3,7])

# plt.scatter(x, y)
# plt.show()
print(np.corrcoef(x, y))  # 0.4807 의미없다. 데이터 분포가 곡선.

# 선형회귀 모델을 작성
from sklearn.linear_model import LinearRegression
x = x[:, np.newaxis]  # 차원 확대(numpy의 reshape을 사용해도 됨)
print(x)
model = LinearRegression().fit(x, y)  # sklearn은 독립변수가 2d여야함 => reshape
# (-1, 1) : 행은 알아서 해결하라는 뜻
ypred = model.predict(x)  # 데이터 개수가 적어서 test/train 나누지 않음
print('ypred : ', ypred)

# plt.scatter(x, y)
# plt.plot(x, ypred, c='red')
# plt.show()  # 잔차가 최소가 되는 선을 그음
#
# from sklearn.metrics import r2_score
# print('결정계수 : ', r2_score(y, ypred))  # 결정계수 :  0.23113

# feature에 항(다항식 특징)을 추가 - 복잡한 모델로 변경
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2, include_bias=False)  # 열 개수, 편향 없음
x2 = poly.fit_transform(x)  # 특징행렬을 생성. x를 나타낸 값, x**2, x***3, ...
print(x2)
# [[ 1.  1.]
#  [ 2.  4.]
#  [ 3.  9.]
#  [ 4. 16.]
#  [ 5. 25.]]  제곱한 값 생성됨

model2 = LinearRegression().fit(x2, y)  # 특징행렬로 학습
ypred2 = model2.predict(x2)
print('ypred2 : ', ypred2)

plt.scatter(x, y)
plt.plot(x, ypred2, c='blue')
plt.show()

print('결정계수 : ', r2_score(y, ypred2))  # 결정계수 :  0.98921
