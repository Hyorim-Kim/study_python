# [ANOVA 예제 1]
# 빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 양을 측정하였다.
# 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하는지를 분산분석을 통해 알아보자.
# 조건 : NaN이 들어 있는 행은 해당 칼럼의 평균값으로 대체하여 사용한다.
# 수정해야함 파일질라
import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt

# 귀무 : 기름의 종류에 따라 흡수하는 기름의 평균에 차이는 없다.
# 대립 : 기름의 종류에 따라 흡수하는 기름의 평균에 차이는 있다.

kind = [1, 2, 3, 4, 2, 1, 3, 4, 2, 1, 2, 3, 4, 1, 2, 1, 1, 3, 4, 2]
quantity = [64, 72, 68, 77, 56, 0, 95, 78, 55, 91, 63, 49, 70, 80, 90, 33, 44, 55, 66, 77]  # 문제대로 수정하기

df1 = pd.DataFrame(kind)
df2 = pd.DataFrame(quantity)
df2.iloc[5, 0] = np.nan

df = pd.concat([df1, df2], axis = 1)
df.columns = ['기름종류', '흡수량']
df['흡수량'] = df['흡수량'].fillna(df['흡수량'].mean())
df = df.astype('int')
print(df)

result = df[['기름종류', '흡수량']]
m1 = result[result['기름종류'] == 1]  # , quantity?
m2 = result[result['기름종류'] == 2]
m3 = result[result['기름종류'] == 3]
m4 = result[result['기름종류'] == 4]

gr1 = m1['흡수량']  # ?
gr2 = m2['흡수량']
gr3 = m3['흡수량']
gr4 = m4['흡수량']

# print(gr1[:3])
# print(gr2[:3])
# print(gr3[:3])
# print(gr4[:3])

print(np.mean(gr1), ' ', np.mean(gr2), ' ', np.mean(gr3), ' ', np.mean(gr4))
# 63.166666666666664 vs 68.83333333333333 vs 66.75 vs 72.75

# 한 개의 표본이 같은 분포를 따르는지 정규성 확인
print(stats.shapiro(gr1).pvalue) # 0.86710 > 0.05 이므로 정규성 만족
print(stats.shapiro(gr2).pvalue) # 0.59239 > 0.05 이므로 정규성 만족
print(stats.shapiro(gr3).pvalue) # 0.48601 > 0.05 이므로 정규성 만족
print(stats.shapiro(gr4).pvalue) # 0.41621 > 0.05 이므로 정규성 만족

print()
# 두 개의 표본이 같은 분포를 따르는지 정규성 확인
print(stats.ks_2samp(gr1, gr2).pvalue)  # 0.9307 > 0.05 이므로 정규성 만족
print(stats.ks_2samp(gr1, gr3).pvalue)  # 0.9238 > 0.05 이므로 정규성 만족
print(stats.ks_2samp(gr1, gr4).pvalue)  # 0.5523 > 0.05 이므로 정규성 만족
print(stats.ks_2samp(gr2, gr3).pvalue)  # 0.9238 > 0.05 이므로 정규성 만족
print(stats.ks_2samp(gr2, gr4).pvalue)  # 0.5523 > 0.05 이므로 정규성 만족
print(stats.ks_2samp(gr3, gr4).pvalue)  # 0.7714 > 0.05 이므로 정규성 만족

print()
# 등분산성 : 만족하지 않으면 welch_anova test 사용
print(stats.bartlett(gr1, gr2, gr3, gr4).pvalue) # 0.1938 > 0.05 이므로 등분산성 만족

# 데이터의 퍼짐 정도 시각화
plt.boxplot([gr1, gr2, gr3, gr4], showmeans = True)
plt.show()

# 일원분산분석 방법 : f_oneway()
f_sta, pvalue = stats.f_oneway(gr1, gr2, gr3, gr4)
print('f통계량 : ', f_sta)   # 0.27241
print('유의확률 : ', pvalue)  # 0.84438 > 0.05이므로 귀무 채택.
# 기름의 종류에 따라 흡수하는 기름의 평균에 차이는 없다.

# 사후검정
from statsmodels.stats.multicomp import pairwise_tukeyhsd
turkeyResult = pairwise_tukeyhsd(endog = df.흡수량, groups = df.기름종류)
print(turkeyResult)  # 차이가 없으면 reject가 False가 나오고, 차이가 크면 True가 나온다.

# 시각화
turkeyResult.plot_simultaneous(xlabel = 'mean', ylabel = 'group')
plt.show()
