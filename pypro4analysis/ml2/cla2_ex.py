# 문1] 소득 수준에 따른 외식 성향을 나타내고 있다. 주말 저녁에 외식을 하면 1, 외식을 하지 않으면 0으로 처리되었다. 
# 다음 데이터에 대하여 소득 수준이 외식에 영향을 미치는지 로지스틱 회귀분석을 실시하라.
# 키보드로 소득 수준(양의 정수)을 입력하면 외식 여부 분류 결과 출력하라.
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.model_selection import train_test_split

data = """
토,0,57
토,0,39
토,0,28
화,1,60
토,0,31
월,1,42
토,1,54
토,1,65
토,0,45
토,0,37
토,1,98
토,1,60
토,0,41
토,1,52
일,1,75
월,1,45
화,0,46
수,0,39
목,1,70
금,1,44
토,1,74
토,1,65
토,0,46
토,0,39
일,1,60
토,1,44
일,0,30
토,0,34
"""
rows = [row.split(',') for row in data.strip().split('\n')]
data = {'요일': [], '외식유무': [], '소득수준': []}

for row in rows:
    data['요일'].append(row[0])
    data['외식유무'].append(int(row[1]))
    data['소득수준'].append(int(row[2]))

# 주말 데이터만 추출
data = pd.DataFrame(data)
data = data[data['요일'].isin(['토', '일'])]
print(data.head(5), data.shape)  # (21, 3)

# 분류 모델
myFormula = '외식유무 ~ 소득수준'
model = smf.logit(formula=myFormula, data=data).fit()
print(model.summary())
print(model.params)
print('예측값 : ', np.rint(model.predict(data)[:5].values))
print('실제값 : ', data['외식유무'][:5].values)

# 정확도 계산
from sklearn.metrics import accuracy_score
pred = model.predict(data)
print('정확도 : ', accuracy_score(data['외식유무'], np.around(pred)))  # 정확도 :  0.90476

# 키보드로 소득 수준 입력






