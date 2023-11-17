# [Randomforest 문제1] 
# kaggle.com이 제공하는 'Red Wine quality' 분류 ( 0 - 10)
# dataset은 winequality-red.csv 
# https://www.kaggle.com/sh6147782/winequalityred?select=winequality-red.csv
#
# Input variables (based on physicochemical tests):
#  1 - fixed acidity
#  2 - volatile acidity
#  3 - citric acid
#  4 - residual sugar
#  5 - chlorides
#  6 - free sulfur dioxide
#  7 - total sulfur dioxide
#  8 - density
#  9 - pH
#  10 - sulphates
#  11 - alcohol
#  Output variable (based on sensory data):
#  12 - quality (score between 0 and 10)

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score

df = pd.read_csv('../testdata/wine.csv')
print(df.head(3))
print(df.info())

df_x = df.drop(columns = ['quality'])
df_y = df['quality']

train_x, test_x, train_y, test_y = train_test_split(df_x, df_y, test_size = 0.3, random_state=1)
print(train_x.shape, test_x.shape, train_y.shape, test_y.shape) # (1117, 11) (479, 11) (1117,) (479,)

model = RandomForestClassifier(n_estimators=500, criterion='entropy')
model.fit(train_x, train_y)

pred = model.predict(test_x)
print('예측값 :', pred[:5])
print('실제값 :', np.array(test_y[:5]))

# 정확도
print('acc :', accuracy_score(test_y, pred))

# 교차검증
cross_vali = cross_val_score(model, df_x, df_y, cv = 5)
print(cross_vali)
print(np.mean(cross_vali))

# 중요변수
print('특성(변수) 중요도 :',model.feature_importances_)

