# 회귀분석 문제 3)    
# kaggle.com에서 carseats.csv 파일을 다운 받아 (https://github.com/pykwon 에도 있음)
# Sales 변수에 영향을 주는 변수들을 선택하여 선형회귀분석을 실시한다.  ==> 다중선형회귀 분석 실시
# 변수 선택은 모델.summary() 함수를 활용하여 타당한 변수만 임의적으로 선택한다.
# 회귀분석모형의 적절성을 위한 조건도 체크하시오.
# 완성된 모델로 Sales를 예측.

import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.api
import numpy as np

df = pd.read_csv("../testdata/Carseats.csv", usecols=[0,1,2,3,4,5,7,8])
print(df.head(3), df.shape)  # (400, 11)
print(df.info())

print('r : \n', df.corr())

# 다중선형회귀모델
lm = smf.ols(formula = 'Sales ~ CompPrice+Income+Advertising+Population+Price+Age+Education', data=df).fit()
# print(lm.summary())  # 타당한 변수만 임의적으로 선택 Income, Advertising, Price, Age       income 찝찝함(r값 작음)
print(lm.params)
print(lm.pvalues)
print(lm.rsquared)

# 다중선형회귀모델 결론
lm2 = smf.ols(formula = 'Sales ~ Income+Advertising+Price+Age', data=df).fit()
print(lm2.summary())

# 모델 검정
pred = lm2.predict(df[:10])
print('실제값 : ', df.Sales[:10].values)
print('예측값 : ', pred[:10].values)
# 예측 : 새로운 Income, Advertising, Price, Age 값으로 Sales 추정
x_new = pd.DataFrame({'Income':[80, 90, 60],'Advertising':[10, 5, 8],'Price':[100.0, 90.5, 85.0],'Age':[37, 45, 52]})
new_pred = lm2.predict(x_new)
print('Sales 추정값 : ', new_pred.values)  # [9.72179008 9.38266604 9.39490659]   ***

print('잔차항 구하기')
fitted = lm2.predict(df.iloc[:, [2, 3, 5, 6]])  # Income, Advertising, Price, Age 열만 출력
# print(fitted)
residual = df['Sales'] - fitted  # 실제값 - 예측값 = 잔차
# print('residual : ', residual, sum(residual)


# . 선형성 : 독립변수(feature)의 변화에 따라 종속변수도 일정 크기로 변화해야 한다
sns.regplot(x=fitted, y=residual, lowess=True, line_kws={'color':'red'})
plt.plot([fitted.min(), fitted.max()],[0, 0], '--', color='blue')
plt.show()
# 예측값과 잔차가 일정 - 선형성을 만족


# . 정규성 : 잔차항(오차항)이 정규분포를 따라야 한다. Q-Q plot을 사용
import scipy.stats
ssz = scipy.stats.zscore(residual)
(x, y), _ = scipy.stats.probplot(ssz)
sns.scatterplot(x=x, y=y)
plt.plot([-3, 3], [-3, 3], '--', color='blue')
plt.show()
# 정규성 만족. shapiro로 확인
print('정규성 : ', scipy.stats.shapiro(residual))  # pvalue=0.20746654272079468-09 > 0.05 (만족O)


# . 독립성 : 독립변수의 값이 서로 관련되지 않아야 한다.
# Durbin-Watson 지수를 이용하여 검정한다. 2에 가까울수록 자기상관이 없이 독립적임
print('Durbin-Watson: ', 1.931)  # 독립성 만족


# . 등분산성 : 그룹간의 분산이 유사해야 한다. 독립변수의 모든 값에 대한 오차들의 분산은 일정해야 한다.
sns.regplot(x=fitted, y=np.sqrt(np.abs(ssz)), lowess=True, line_kws = {'color':'red'})  # fitted와 분산값
plt.show()
# 적색 실선이 수평선을 그리므로 등분산성 만족


# . 다중공선성 : 다중회귀 분석 시 두 개 이상의 독립변수 간에 강한 상관관계가 있어서는 안된다.
# VIF(Variance Inflation Factor, 분산 팽창 지수) 확인
from statsmodels.stats.outliers_influence import variance_inflation_factor

df2 = df[['Income', 'Advertising', 'Price', 'Age']]
vifdf = pd.DataFrame()
vifdf['vif_value'] = [variance_inflation_factor(df2.values,i)for i in range(df2.shape[1])]  # **
print(vifdf)
# vif 지수가 10보다 작음 따라서 다중공성선 만족

# 모델 검증이 끝난 경우 모델을 저장
# 방법1 (오리지널)
'''
import pickle
with open('linear6_kaggle.model', 'wb')as obj:
    pickle.dump(lm2, obj)

with open('linear6_kaggle.model', 'rb')as obj:
    mymodel = pickle.load(obj)
'''

# 방법2 (메모리 절약, 속도 향상) **
'''
import joblib
joblib.dump(lm2, 'linear6_kaggle.model')

mymodel = joblib.load('linear6_kaggle.model')
'''
# 값 예측은 37line에 있음
