# [GaussanNB 문제] 
# 독버섯(poisonous)인지 식용버섯(edible)인지 분류
# https://www.kaggle.com/datasets/uciml/mushroom-classification
# feature는 중요변수를 찾아 선택, label:class
# 참고 : from xgboost import plot_importance

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from xgboost import plot_importance
import matplotlib.pyplot as plt
import xgboost as xgb


df = pd.read_csv('../testdata/mushrooms.csv')
print(df.head(3))
print(df.info())

le = LabelEncoder() # for 문으로 각 칼럼들을 넣어 인코딩하였다.
for col in df.columns:
    df[col] = le.fit_transform(df[col])
print(df.head(3))

x = df.drop(columns = ['class'])
y = df['class']

print(x[:3])
print(y[:3])

# train/test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 1)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) # (5686, 22) (2438, 22) (5686,) (2438,)

# 주요 변수 모델링 및 시각화
model = xgb.XGBClassifier(booster = 'gbtree', max_depth = 6, n_estimators=500 ).fit(x_train, y_train)
pred = model.predict(x_test)

fig, ax = plt.subplots(figsize=(10, 12))
plot_importance(model, ax = ax)
plt.show()

features = df[['spore-print-color', 'odor', 'gill-size', 'cap-color', 'population']]
labels = df['class']

# train/test
x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size = 0.3, random_state = 1)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) # (5686, 5) (2438, 5) (5686,) (2438,)

# model
gmodel = GaussianNB()
gmodel.fit(x_train, y_train)

pred = gmodel.predict(x_test)
print('예측값 :', pred[:10])
print('실제값 :', y_test[:10].values)

acc = sum(y_test == pred) / len(pred)
print('acc :', acc)
print('acc :', accuracy_score(y_test, pred))

# kfold
from sklearn import model_selection
cross_val = model_selection.cross_val_score(gmodel, x, y, cv = 5)
print('교차 검증 :', cross_val)
print('교차 검증 평균값 :', cross_val.mean())
