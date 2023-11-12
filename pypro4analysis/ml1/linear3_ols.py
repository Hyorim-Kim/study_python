# 단순선형회귀분석 모델 작성 : ols() 함수 - OLS Regression Results 내용 알기
# 결정론적 선형회귀분석 방법 - 확률적 모형에 비해 불확실성이 덜 하다.
from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
import statsmodels.formula.api as smf

df = pd.read_csv("../testdata/drinking_water.csv")
print(df.head(3), df.shape)
print(df.corr(method='pearson'))  # 적절성 / 만족도 : 0.766853
# 독립변수(x, feature) : 적절성
# 종속변수(x, label) : 만족도
# 목적 : 주어진 feature와 결정적 기반에서 학습을 통해최적의 회귀계수(slope, bias)를 찾아내는 것
model = smf.ols(formula='만족도 ~ 적절성', data=df).fit()
# print(model.summary())
"""
==============================================================================
Dep. Variable:                      만족도   R-squared:                         0.588  결정계수(설명력) : 0~1로 1에 가까울수록 좋음
Model:                                        OLS   Adj. R-squared:                 0.586  58%정도 설명하고 있음
Method:                   Least Squares   F-statistic:                         374.0
Date:                   Fri, 10 Nov 2023   Prob (F-statistic):        2.24e-52  : 0.05보다 작아야 의미있는 모델(귀무 기각의 증거)
Time:                                 16:45:06   Log-Likelihood:            -207.44
No. Observations:                    264   AIC:                                     418.9
Df Residuals:                            262   BIC:                                     426.0
Df Model:                                        1                                         
Covariance Type:          nonrobust                                         
==============================================================================
SSR(residual) + SSE(error) = SST(total), 설명가능한 변동값 + 설명불가능한 변동값 = 총변동값
1 - SSR/SST = R-squared
R-squared : 독립변수(x)가 종속변수(y)의 분산을 설명해주는 값
교집합이 많을수록 독립변수가 종속변수를 잘 설명하는 것
R-squared(설명력)는 accuracy(분류 정확도)가 아니기 때문에 100% 신뢰할 수 없음. 애매모호함
독립변수의 개수가 늘어나면 설명력과 상관없이 R-squared가 증가함 => 패널티로 수정된 R-squared 값을 사용/
==============================================================================
                             coef             std err           t           P>|t|       [0.025      0.975]         
------------------------------------------------------------------------------
Intercept  (bias)0.7789      0.124      6.273      0.000       0.534       1.023
적절성    (slope)0.7393     0.038     19.340     0.000       0.664       0.815
==============================================================================
std err : (표준오차, 표본 평균들의 표준편차), 작을수록 좋다.
표준오차가 커지면 t값이 작아지고, 따라서 p값이 커진다. => 독립변수가 의미없다는 결론을 내리게 됨.
표준오차가 작아야 모집단과 평균에 차이가 없어져 모집단을 좀 더 신뢰할 수 있게 됨.
적절성의 회귀계수(Intercept)는 0.7393으로, 적절성이 1 증가할 때마다 만족도가 약 0.7393 증가한다

t-test를 통해 추세선을 증명함
t 값 : 기울기/표준오차   0.7393/0.038 = 19.340.     p(<0.05) -'적절성'은 가치 있는 독립변수임/
==============================================================================
Omnibus:                    11.674   Durbin-Watson:                2.185   잔차의 독립성과 관련
Prob(Omnibus):           0.003   Jarque-Bera (JB):            16.003  자기상관, 오차의 정규성 가정을 검정한 값?
Skew:                           -0.328   Prob(JB):                      0.000335  자기상관, 오차의 정규성 가정을 검정한 값
Kurtosis:                       4.012   Cond. No.                              13.4  다중공선성과 관련
==============================================================================
Prob(Omnibus)는 회귀 모델의 유의성을 검사, 0.05보다 작으면 유의함
Jarque-Bera로 정규분포를 따르는지 확인
"""
# 부분적으로 보기
print(model.params)
print(model.pvalues)

# 예측값
print(df.적절성[:5].values)
new_df = pd.DataFrame({'적절성':[4, 3, 4, 2, 2]})
new_pred = model.predict(new_df)
print('만족도 실제값 : ', df['만족도'][:5].values)
print('만족도 예측값 : ', new_pred.values)  # 0.588 설명력이 있는 모델로 검정, 설명력은 참고자료임
