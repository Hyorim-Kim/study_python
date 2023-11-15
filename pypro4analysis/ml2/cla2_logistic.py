# Logistic Linear Regression
# weather dataset으로 다음날 비 여부를 예측하는 분류 모델 작성
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.model_selection import train_test_split

data = pd.read_csv("../testdata/weather.csv")
print(data.head(2), data.shape)  # (366, 12)
data2 = pd.DataFrame()  # 빈 프레임
data2 = data.drop(['Date', 'RainToday'], axis=1)  # 선택적으로 열 삭제
print(data2.head(2), data2.shape)  # (366, 10)
print(data2.columns)
print(data2.RainTomorrow.unique())  # ['Yes' 'No']   # dummy화 [1, 0]
data2['RainTomorrow'] = data2['RainTomorrow'].map({'Yes':1, 'No':0})
print(data2.RainTomorrow.unique())  # [1 0] ndarray임(콤마 없음)

# RainTomorrow : 종속(label), 나머지 변수 : 독립(feature)
# 모델을 학습 후 검증하고 싶다면 train/test로 분리 (과적합 방지)
train, test = train_test_split(data2, test_size = 0.3, random_state=42, shuffle=True) # 7:3
print(train.shape, test.shape)  # (256, 10) (110, 10)

# 분류 모델
col_select = "+".join(train.columns.difference(['RainTomorrow']))
print(col_select)
myFormula = 'RainTomorrow ~ ' + col_select
# model = smf.glm(formula=myFormula, data=train, family=sm.families.Binomial()).fit()
model = smf.logit(formula=myFormula, data=train).fit()
print(model.summary())
# Cloud MaxTemp Rainfall Temp WindSpeed > 0.05
# 하지만 다른 변수를 제거했을 때 해당변수의 p값이 감소할 수도 있음
# 빼고 가야하지만 패스
print(model.params)
print('예측값 : ', np.rint(model.predict(test)[:5].values))
print('실제값 : ', test['RainTomorrow'][:5].values)
# 예측값 :  [0. 0. 0. 0. 0.]
# 실제값 :  [0 0 0 0 0]  # 결과 good

# 정확도 계산
conf_mat = model.pred_table()
print('confusion matrix : \n', conf_mat)  # 'GLMResults' object has no attribute 'pred_table' 지원X => logit 모델 사용
print('정확도 : ', (conf_mat[0][0] + conf_mat[1][1]) / len(train))  # 정확도 :  0.87109375

from sklearn.metrics import accuracy_score
pred = model.predict(test)
print('정확도 : ', accuracy_score(test['RainTomorrow'], np.around(pred)))  # 정확도 :  0.87272727
# 정확도에 미미한 차이를 보이는 이유는 샘플링 때문.

 # [[197.   9.]  # 분류모델 Accuracy table 참고
 # [ 21.  26.]]
