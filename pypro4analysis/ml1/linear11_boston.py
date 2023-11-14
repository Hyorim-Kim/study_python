# Boston Housing Price (보스턴 주택 가격 데이터)로 선형회귀 모델 생성

import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
df = pd.read_csv("../testdata/housing.data", header=None, sep='\s+')
df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
print(df.head(2), df.shape)  # (506, 14)
print(df.corr())  # MEDV, LSTAT : -0.737663 (음의 상관관계가 매우 강함)

x = df[['LSTAT']].values
y = df['MEDV'].values  # vector로 가져오기
model = LinearRegression()
model.fit(x, y)

# y_lin_fit = model.predict(x)
# model_r2 = r2_score(y, y_lin_fit)
# print('model_r2 : ', model_r2)  # 0.54414

x_fit = np.arange(x.min(), x.max(), 1)[:, np.newaxis]  # 차트 작성용 시작
print(x_fit)
# [[ 1.73]
#  [ 2.73]
#  [ 3.73]
# ...

# 다항 특성
quad = PolynomialFeatures(degree=2)
x_quad = quad.fit_transform(x)
print(x_quad)
# [[ 1.      4.98   24.8004]
#  [ 1.      9.14   83.5396]
#  [ 1.      4.03   16.2409]

cubic = PolynomialFeatures(degree=3)
x_cubic = cubic.fit_transform(x)
print(x_cubic)
# [[  1.         4.98      24.8004   123.505992]
#  [  1.         9.14      83.5396   763.551944]
#  [  1.         4.03      16.2409    65.450827]

# degree = 1
model.fit(x, y)
y_lin_fit = model.predict(x_fit)  # 차트 작성용 끝
model_r2 = r2_score(y, model.predict(x))
print('model_r2 : ', model_r2)

# degree = 2
model.fit(x_quad, y)
y_quad_fit = model.predict(quad.fit_transform(x_fit))
quad_r2 = r2_score(y, model.predict(x_quad))
print('quad_r2 : ', quad_r2)

# degree = 3
model.fit(x_cubic, y)
y_cubic_fit = model.predict(cubic.fit_transform(x_fit))
cubic_r2 = r2_score(y, model.predict(x_cubic))
print('cubic_r2 : ', cubic_r2)


# 시각화
plt.scatter(x, y, label='training data', c='lightblue')

plt.plot(x_fit, y_lin_fit, linestyle=':', label='linear fit(d=1), $R^2=%.2f$'%model_r2, c='b', lw=3)  # 선형
plt.plot(x_fit, y_quad_fit, linestyle='-', label='quad fit(d=2), $R^2=%.2f$'%quad_r2, c='r', lw=3)
plt.plot(x_fit, y_cubic_fit, linestyle='--', label='cubic fit(d=3), $R^2=%.2f$'%model_r2, c='g', lw=3)

plt.xlabel('하위계층비율')
plt.ylabel('주택가격')
plt.legend()
plt.show() 
# 음의 상관관계가 뚜렷, 살짝 커브 형태(선형? 비선형?)
# 무조건 비선형 모델을 사용하는 것이 좋은 것은 아님
# 어떤 형태의 모델을 사용할 지는 분석가가 결정함
