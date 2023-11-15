# Logistic Linear Regression
# 선형회귀분석처럼 신뢰구간, 표준오차, p값 등이 제공되나 회귀계수의 결과를 해석하는 방법이 다르다.
# 독립변수 : 연속형, 종속변수 : 범주형, 이항분포를 따르며 출력값은 0 ~ 1 사이의 확률로 제공됨.
# 연속형 결과를 로짓(오즈비에 로그를 씌움)변환 후 시그모이드 함수를 통해 결과를 내보낸다.

import math
# sigmoid function 경험
def sigmoidFunc(x):
    return 1/(1+math.exp(-x))

print(sigmoidFunc(3))  # 0에서 1사이의 값을 리턴
print(sigmoidFunc(1))
print(sigmoidFunc(-2))
print(sigmoidFunc(-5))

print('mtcars dataset을 사용')
import statsmodels.api as sm

mtcarData = sm.datasets.get_rdataset('mtcars')
print(mtcarData.keys())
mtcars = sm.datasets.get_rdataset('mtcars').data  # data만 뽑기
print(mtcars.head(2))
mtcar = mtcars.loc[:, ['mpg', 'hp', 'am']]
print(mtcar.head(2))
print(mtcar['am'].unique())  # [1 0]

# 연비와 마력수는 변속기에 영향을 주는가?
# 모델 작성 방법1 : logit()
import statsmodels.formula.api as smf
formula='am ~ hp+mpg'
model1 = smf.logit(formula=formula, data=mtcar).fit()
# 내부적으로 최적이 되는 선을 찾아 9번 반복함
print(model1)
print(model1.summary())  # 설명력, 결정계수 안나옴

import numpy as np
pred = model1.predict(mtcar[:10])
print('예측값 : ', pred.values)  # 데이터가 적어 train/test split 없이 학습만 함
print('예측값 : ', np.around(pred.values))
print('실제값 : ', mtcar['am'][:10].values)

conf_tab = model1.pred_table()
print('confusion matrix : \n', conf_tab)
 # [[16.  3.]  3, 3은 모델이 잘못 예측한 것 => Accuracy 표 참고(+ Presicion, Recall)
 # [ 3. 10.]]
print('분류 정확도 : ', (16 + 10) / len(mtcar))  # 0.8125   분류정확도는 81.2%
print('분류 정확도 : ', (conf_tab[0][0] + conf_tab[1][1]) / len(mtcar))
from sklearn.metrics import accuracy_score
pred2 = model1.predict(mtcar)
print('분류 정확도 : ', accuracy_score(mtcar['am'], np.around(pred2)))

print('-----------------------------')
# 모델 작성 방법2 : glm() - 일반화 선형모델
model2 = smf.glm(formula=formula, data=mtcar, family=sm.families.Binomial()).fit()  # 이항분포 따름, 기본은 Gaussian(정규분포)
print(model2)
print(model2.summary())
glmPred = model2.predict(mtcar[:10])
print('glm 예측값 : ', np.around(glmPred.values))
print('glm 실제값 : ', mtcar['am'][:10].values)
glmPred2 = model2.predict(mtcar)
print('분류 정확도 : ', accuracy_score(mtcar['am'], np.around(glmPred2)))  # 0.8125

print('새로운 값으로 분류 예측')
newdf = mtcar.iloc[:2].copy()  # 기존 자료 2행 읽어 값 수정 후 분류에 참여
print(newdf)
newdf['mpg'] = [10, 30]
newdf['hp'] = [100, 130]
print(newdf)
new_pred = model2.predict(newdf)
print('new_pred : ', np.around(new_pred.values))
print('new_pred : ', np.rint(new_pred.values))  # 상동
# 10  100은 0으로, 30  130은 1로 분류함

print()
import pandas as pd  # df로 만들기
newdf2 = pd.DataFrame({'mpg':[10, 35, 50, 5], 'hp':[80,100,125,50]})
new_pred2 = model2.predict(newdf2)
print('new_pred2 : ', np.around(new_pred2.values))
# new_pred2 :  [0. 1. 1. 0.]

# 머신러닝의 포용성(inclusion, tolerance)
# 생성모델은 최적화와 일반화를 잘 융합해야 한다.
# 분류정확도가 100%인 경우는 과적합(overfitting) 모델이므로 새로운 데이터에 대해 정확한 분류를 할 수 없는 경우가 있다.
# eg. 꼬리없는 동물
