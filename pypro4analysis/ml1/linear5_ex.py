"""
회귀분석 문제 2) 
testdata에 저장된 student.csv 파일을 이용하여 세 과목 점수에 대한 회귀분석 모델을 만든다. 
이 회귀문제 모델을 이용하여 아래의 문제를 해결하시오.  수학점수를 종속변수로 하자.
  - 국어 점수를 입력하면 수학 점수 예측
  - 국어, 영어 점수를 입력하면 수학 점수 예측
"""

import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
import statsmodels.formula.api as smf
import statsmodels.api
import numpy as np

score = pd.read_csv("../testdata/student.csv")
print(score.head(3), score.shape)
print(np.corrcoef(score.국어, score.수학)[0,1])  # 0.76626

# 국어 점수를 입력하면 수학점수 예측
result = smf.ols(formula='수학 ~ 국어', data=score).fit()
print(result.summary())  # < 0.05로 유의한 모델

국어 = int(input('국어 점수 : '))
newdf = pd.DataFrame({'국어':[국어]})
new_pred = result.predict(newdf)
print('국어점수:{}에 대한 수학점수 예측:{}'.format(newdf, new_pred[0]))


# 국어, 영어 점수를 입력하면 수학 점수 예측
result2 = smf.ols(formula='수학 ~ 국어 + 영어', data=score).fit()
print('result2 모델 정보 : ', result2.summary())  # < 0.05으로 유의한 모델

# print('국어:{}, 영어:{} 수학점수:{}'.format(70,80, result2.predict(pd.DataFrame({'국어':70,'영어':80}))))
국어 = int(input('국어:'))
영어 = int(input('수학:'))
newdf2 = pd.DataFrame({'국어':[국어], '영어':[영어]})
new_pred2 = result2.predict(newdf2)
print('국어:{}, 영어:{}에 대한 수학 예측 결과:{}'.format(newdf2['국어'][0], newdf2['영어'][0], new_pred2[0]))
