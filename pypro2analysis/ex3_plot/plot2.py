# matplotlib 스타일 인터페이스/객체 지향 인터페이스/차트 종류 몇가지 경험하기

import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False

x = np.arange(10)
"""
# matplotlib 스타일 인터페이스
plt.figure()  # plot 영역 확보
plt.subplot(2, 1, 1)  # (row, column, panel number)
plt.plot(x, np.sin(x))
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x))
plt.show()  # 출력

# matplotlib 객체 지향 인터페이스
fig, ax = plt.subplots(nrows=2, ncols=1)  # fig : plot 전체, ax : 하나의 plot
ax[0].plot(x, np.sin(x))
ax[1].scatter(x, np.cos(x))
plt.show()
"""

"""
data = [50, 80, 100, 70, 88]

# 막대 그래프  # 데이터 양이 많지 않을 때 막대 그래프 이용
plt.bar(range(len(data)), data)
plt.show()

# 세로 막대 그래프
err = np.random.rand(len(data))
plt.barh(range(len(data)), data, xerr=err)  # error bar(오차 막대) : 편차, 오차, 신뢰구간 등 표현에 효과적
plt.show()

# 원 그래프
plt.pie(data, explode=(0,0,0.2,0,0), colors=['yellow', 'blue', 'red'])
plt.show()

# 히스토그램  # 많은 양의 데이터를 다룰 때, 연속형 데이터, 수치 데이터 중 비율척도일 때 히스토그램
plt.hist(data, bins=5, alpha=0.3)
plt.show()

# 박스 그래프
plt.boxplot(data, notch=True)
plt.show()

# 시계열 데이터 출력
import pandas as pd
fdata = pd.DataFrame(np.random.rand(1000, 4), \
                                        index=pd.date_range('1/1/2000', periods=1000), columns=list('abcd'))
fdata = fdata.cumsum()
print(fdata.head(3))
print(fdata.tail(3))
plt.plot(fdata)
plt.show()

# pandas의 plot 기능
fdata.plot(kind='box')
plt.show()
"""

# matplotlib의 기능 보충용 lib로 seaborn
import seaborn as sns
"""
# Seaborn 데이터셋 목록
# print(sns.get_dataset_names())

titanic = sns.load_dataset('titanic')
# print(titanic.info())
print(titanic.head(3))

plt.hist(titanic['age'])
plt.show()

sns.displot(titanic['age'])
plt.show()

sns.boxplot(y='age', data=titanic)
plt.show()
"""

# iris dataset
# iris_data = sns.load_dataset('iris')
# print(iris_data.head(3))

import pandas as pd
iris_data = pd.read_csv('../testdata/iris.csv')
print(iris_data.head(3))

# 산점도
plt.scatter(iris_data['Sepal.Length'], iris_data['Petal.Length'])
plt.show()

# Species 별 색상 부여
print(iris_data['Species'].unique())  # ['setosa' 'versicolor' 'virginica']
print(set(iris_data['Species']))  # {'versicolor', 'setosa', 'virginica'}

cols = []
for s in iris_data['Species']:
    choice = 0
    if s == 'setosa':choice = 1
    elif s == 'versicolor':choice = 2
    elif s == 'virginica':choice = 3
    cols.append(choice)
    
plt.scatter(iris_data['Sepal.Length'], iris_data['Petal.Length'], c=cols)
plt.xlabel('Sepal.Length')
plt.ylabel('Petal.Length')
plt.show()

# Sepal.Length  Sepal.Width  Petal.Length  Petal.Width를 사용해 scatter matrix 그래프 출력
iris_col = iris_data.loc[:, 'Sepal.Length':'Petal.Width']  # loc를 썼기 때문에 칼럼명
print(iris_col)
# pandas 사용
pd.plotting.scatter_matrix(iris_col, diagonal='kde')  # 밀도 분포 곡선 같이보기
plt.show()

# seaborn으로 scatter matrix 그래프 출력
sns.pairplot(iris_data, hue='Species', height=2)  # 카테고리 칼럼은 Species
plt.title('seaborn으로 scatter matrix')
# plt.show()

# 그래프(차트)를 이미지로 저장
# img src로 저장하면 기능x
# 파이썬의 데이터를 바탕으로 파이차트나 퓨전차트를 이용하여 동적 기능 구현해야함
fig = plt.gcf()
plt.show()
fig.savefig('plot2.png')

# 이미지 읽기
from matplotlib.pyplot import imread
img = imread('plot2.png')
plt.imshow(img)
plt.show()
