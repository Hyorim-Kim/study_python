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



'''
# 문1] 소득 수준에 따른 외식 성향을 나타내고 있다. 주말 저녁에 외식을 하면 1, 외식을 하지 않으면 0으로 처리되었다.
# 다음 데이터에 대하여 소득 수준이 외식에 영향을 미치는지 로지스틱 회귀분석을 실시하라.
# 키보드로 소득 수준(양의 정수)을 입력하면 외식 여부 분류 결과 출력하라

import pandas as pd
from sklearn.metrics import accuracy_score
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
from io import StringIO

data = StringIO("""
요일,외식유무,소득수준
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
토,0,34""")
df = pd.read_csv(data)
df = df[(df['요일'] == '토') | (df['요일']=='일')]
print(df, df.shape)

# 모델 glm
formula='외식유무 ~ 소득수준'
model = smf.glm(formula=formula, data=df, family=sm.families.Binomial()).fit()
print(model.summary())  # <0.05 유의한 모델임
glmPred = model.predict(df[:10])
print('glm 예측값 : ', np.around(glmPred.values))      # [1. 0. 0. 0. 1. 1. 0. 0. 1. 1.]
print('glm 실제값 : ', df['외식유무'][:10].values)     # [0 0 0 0 1 1 0 0 1 1]

# 분류 정확도
glmPred2 = model.predict(df)
print('glm 분류 정확도 : ', accuracy_score(df['외식유무'], np.around(glmPred2)))     # 0.904761

newdf = pd.DataFrame({'소득수준': [int(input('소득수준 입력: '))]})
flag = np.rint(model.predict(newdf))[0]
print('외식함' if flag == 1 else '외식안함')
'''
