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
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.api
import numpy as np

score = pd.read_csv("../testdata/student.csv")
print(score.head(3), score.shape)
print(score.columns)
print(score.describe())
print(np.corrcoef(score.국어, score.수학)[0,1])  # 0.7662626

result = smf.ols(formula='수학 ~ 국어', data=score).fit()
print(result.summary())
print('국어점수:{}에 대한 수학점수 예측:{}'.format(90, result.predict(pd.DataFrame({'수학':[90]}))))





