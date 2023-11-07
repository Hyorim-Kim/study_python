# 추론 통계 분석 중 가설검정 : 단일 표본 t-검정(one-sample t-test)
# 정규분포의(모집단) 표본에 대해 기대값을  조사(평균 차이 사용)하는 검정 방법
# 예) 새우깡 과자 무게가 진짜 120그램이 맞는가?

# 실습1) 어느 남성 집단의 평균키 검정
# 귀무 : 남성의 평균키는 177.0 (모집단의 평균)이다.
# 대립 : 남성의 평균키는 177.0 (모집단의 평균)이 아니다.

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

one_sample = [167.0, 182.7, 169.6, 176.8, 185.0]
# plt.boxplot(one_sample)
# plt.xlabel('data')
# plt.ylabel('height')
# plt.grid()
# plt.show()

print(np.array(one_sample).mean())  # 176.219
print(np.array(one_sample).mean() - 177.0)  # -0.78
print('정규성 확인 : ', stats.shapiro(one_sample))  # pvalue=0.54005 > 0.05 정규성 만족
result = stats.ttest_1samp(one_sample, 177.0)
print(result)  # TtestResult(statistic=-0.22139444579394396, pvalue=0.8356282194243566, df=4)
print('statistic(t값):%.5f, pvalue:%.5f'%result)
# 해석 : pvalue:0.83563 > 0.05이므로 귀무가설 채택. 수집된 자료는 우연히 발생된 것이라 할 수 있다.

print('------------------------')
# 실습 예제 2)
# A중학교 1학년 1반 학생들의 시험결과가 담긴 파일을 읽어 처리 (국어 점수 평균검정) student.csv
# 귀무 : 학생들의 국어 점수 평균은 80.0이다.
# 대립 : 학생들의 국어 점수 평균은 80.0이 아니다.

data = pd.read_csv("../testdata/student.csv")
print(data.head(3))
print(data.describe())
print(np.mean(data.국어))  # 72.9 / 80.0

result2 = stats.ttest_1samp(data.국어, popmean=80.0)
print(result2)  # TtestResult(statistic=-1.3321801667713216, pvalue=0.19856051824785262, df=19)
print('statistic(t값):%.5f, pvalue:%.5f'%result2)
# 해석 : pvalue:0.19856 > 0.05이므로 귀무가설 채택. 수집된 자료는 우연히 발생된 것이라 할 수 있다.

print('------------------------')
# 실습 예제 3)
# 여아 신생아 몸무게의 평균 검정 수행 babyboom.csv
# 여아 신생아의 몸무게는 평균이 2800(g)으로 알려져 왔으나 이보다 더 크다는 주장이 나왔다.
# 표본으로 여아 18명을 뽑아 체중을 측정하였다고 할 때 새로운 주장이 맞는지 검정해 보자.

# 귀무 : 여아 신생아의 몸무게는 평균이 2800(g)이다.
# 대립 : 여아 신생아의 몸무게는 평균이 2800(g) 보다 크다.

data2 = pd.read_csv("../testdata/babyboom.csv")
print(data2.head(3), len(data2))  # 44
fdata = data2[data2['gender'] == 1]
print(fdata.head(3), len(fdata))  # 18
print(np.mean(fdata['weight']))  # 3132.44

# 정규성 확인 수치
print(stats.shapiro(fdata.iloc[:, 2]))  # pvalue=0.0179 < 0.05 이므로 정규성을 만족하지 못함

# 정규성 확인 시각화 1
stats.probplot(fdata.iloc[:, 2], plot=plt)  # Q-Q plot
plt.show()

# 정규성 확인 시각화 2 : histogram
sns.displot(fdata.iloc[:, 2], kde=True)
plt.show()

result3 = stats.ttest_1samp(fdata.weight, popmean=2800)
print(result3)  # TtestResult(statistic=2.233187669387536, pvalue=0.03926844173060218, df=17)
print('statistic(t값):%.5f, pvalue:%.5f'%result3)
# 해석 : pvalue:0.03927 < 0.05이므로 귀무가설 기각. 여아 신생아의 몸무게는 평균이 2800(g) 보다 크다.
# .....
