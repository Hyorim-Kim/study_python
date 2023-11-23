import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv('../testdata/titanic_data.csv', usecols=['Survived', 'Pclass', 'Sex', 'Age','Fare'])
print(data.head(2), data.shape) # (891, 12)
data.loc[data["Sex"] == "male","Sex"] = 0
data.loc[data["Sex"] == "female", "Sex"] = 1
print(data["Sex"].head(2))
print(data.columns)

feature = data[["Pclass", "Sex", "Fare"]]
label = data["Survived"]

# train_test_split
X_train, X_test, y_train, y_test = train_test_split(feature, label, test_size=0.3, random_state=12)

# DecisionTreeClassifier 모델 생성
model = DecisionTreeClassifier()

# 모델 훈련
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)

# 분류 정확도 출력
accuracy = accuracy_score(y_test, y_pred)
print('분류 정확도:', accuracy)
