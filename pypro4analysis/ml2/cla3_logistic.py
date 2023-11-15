# 인디언들의 당뇨병 관련 데이터를 이용해 이항분류 : LogisticRegression 클래스 사용

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression  # sigmoid 함수가 아니라 softmax 함수를 사용해 다항분류 가능

names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
df = pd.read_csv("../testdata/pima-indians-diabetes.data.csv", header=None, names=names)
print(df.head(2))
array = df.values
print(array[:3], array.shape)  # (768, 9) matrix(feature)
x = array[:, 0:8]
y = array[:, 8]
print(x[:2], x.shape)  # (768, 8)  matrix(2차원)
print(y[:2], y.shape)  # (768,)  vector(1차원)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=7)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)  # (537, 8) (231, 8) (537,) (231,)
'''
model = LogisticRegression()
model.fit(x_train, y_train)
print('예측값 : ', model.predict(x_test[:10]))
print('실제값 : ', y_test[:10])
print((model.predict(x_test) != y_test).sum())  # 예측값과 실제값의 차이의 합(예측 실패) : 58

print('test로 검정한 분류 정확도 : ', model.score(x_test, y_test))  # test로 정확도 확인  0.7489
print('train으로 검정한 분류 정확도 : ', model.score(x_train, y_train))  # train으로 정확도 확인  0.7839
# 위 두 결과가 비슷하지 않을 경우 편향된 데이터를 추출한 것임(비복원 데이터 추출이 아님) => 설득력 떨어짐
# 위 결과 값이 작은 경우(약 40% 이하)는 underfitting
# 위 결과 값이 100에 근접한 경우(약 100%)는 overfitting

from sklearn.metrics import accuracy_score
pred = model.predict(x_test)
print('분류정확도 : ', accuracy_score(y_test, pred))  # 0.7489
'''
# 모델 저장
import joblib
# joblib.dump(model, 'cla3model.save')

# 학습이 끝난 모델 파일 로딩 후 사용
mymodel = joblib.load('cla3model.save')
print(x_test[:1])
print('분류 예측 : ', mymodel.predict(x_test[:1]))
