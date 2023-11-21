# SVM : 데이터 분류 및 예측을 위한 가장 큰 폭의 경계선을 찾는 알고리즘을 사용
# 커널트릭이라는 기술을 통해 선형은 물론 비선형, 이미지 분류까지도 처리 가능

# SVM으로 XOr 처리를 실습(+ or, and 연산)
x_data = [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import svm, metrics

df = pd.DataFrame(x_data)
print(df)

feature = np.array(df.iloc[:, 0:2])  # 2차원
label = np.array(df.iloc[:, 2])  # 1차원
print(feature)
print(label)

print()
model1 = LogisticRegression().fit(feature, label)
pred = model1.predict(feature)
print('Logistic 예측값 : ', pred)
print('Logistic accuracy : ', metrics.accuracy_score(label, pred))  # 순서 : 실제값, 예측값

print()
model2 = svm.SVC(c=1.0).fit(feature, label)  # 선형 비선형 안가리고 사용 가능, c=1.0 : 과적합 방지
# model2 = svm.LinearSVC().fit(feature, label)  # 선형에 가까울 때 LinearSVC 사용하면 성능 good
pred = model2.predict(feature)
print('SVM 예측값 : ', pred)
print('SVM accuracy : ', metrics.accuracy_score(label, pred))
