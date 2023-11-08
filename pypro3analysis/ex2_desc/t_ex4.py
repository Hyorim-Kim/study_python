# 독립표본 t 검정
# 어느 음식점의 매출데이터, 날씨 데이터, 두 개의 파일을 이용해 강수 여부에 따른 음식점 매출액 평균의 차이를  검정
# 귀무 : 강수 여부에 따른 음식점 매출액 평균의 차이는 없다.
# 대립 : 강수 여부에 따른 음식점 매출액 평균의 차이는 있다.

import numpy as np
import pandas as pd
import scipy.stats as stats

# 매출 데이터
sales_data = pd.read_csv('../testdata/tsales.csv', dtype={'YMD':'object'})
print(sales_data.head(3))  # YMD : 20190514
print(sales_data.info())  # int를 object로 바꿔야함, dtype을 지정함

# 날씨 데이터
wt_data = pd.read_csv('../testdata/tweather.csv')
print(wt_data.head(3))  # tm : 2018-06-01
# print(wt_data.info())
wt_data.tm = wt_data.tm.map(lambda x:x.replace('-', ''))  # 함수를 실행하는 함수 map, lambda 반복함수
print(wt_data.head(3))  # tm : 20180601

# merge
frame = sales_data.merge(wt_data, how='left', left_on='YMD', right_on='tm')  # left join 함
print(frame.head(3))
print(frame.tail(3), frame.shape)
print(frame.columns)  # ['YMD', 'AMT', 'CNT', 'stnId', 'tm', 'avgTa', 'minTa', 'maxTa', 'sumRn', 'maxWs', 'avgWs', 'ddMes']

data = frame.iloc[:, [0,1,7,8]]  # YMD(날짜), AMT(매출액), maxTa(최고기온), sumRn(강수량)
print(data.head(3))
print(data.isnull().sum())

print('\n--------------two-sample t-test---------------')
# print(data['sumRn'] > 0)
# data['rain_yn'] = (data['sumRn'] > 0).astype(int)  # true: 1, false: 0, 방법1
# print(data.head(3))

# print(True * 1, False * 1)  # 방법2
data['rain_yn'] = (data.loc[:,('sumRn')] > 0)  * 1  # 방법3
print(data.head(3))

# 매출액 시각화
import matplotlib.pyplot as plt

sp = np.array(data.iloc[:, [1, 4]])
# print(sp)  # [[      0       0]  [  18000       1]
tg1 = sp[sp[:, 1] == 0, 0]  # 집단1 : 비 안올 때 매출액
tg2 = sp[sp[:, 1] == 1, 0]  # 집단1 : 비 올 때 매출액
print(tg1[:3])
print(tg2[:3])

# plt.plot(tg1)
# plt.show()
# plt.plot(tg2)
# plt.show()
plt.boxplot([tg1, tg2], notch=True, meanline=True, showmeans=True)
plt.show()

print(np.mean(tg1), ' ', np.mean(tg2))  # 761040.25   757331.52

# 정규성
print(len(tg1), len(tg2))
print(stats.shapiro(tg1).pvalue)  # 0.0560
print(stats.shapiro(tg2).pvalue)  # 0.8827

# 등분산성
print(stats.levene(tg1, tg2).pvalue)  # 0.7123

print(stats.ttest_ind(tg1, tg2, equal_var=True))
# TtestResult(statistic=0.10109828602924716, pvalue=0.919534587722196, df=326.0)
# 해석 : pvalue=0.91953 > 0.05이므로 귀무가설 채택(귀무가설 기각 실패)
