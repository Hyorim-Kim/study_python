# 이항분포 : 정규분포는 연속변량인데 반해 이산변량을 사용
# 이항 검정 : 결과가 두가지 값을 가지는 확률변수의 분포를 판단하기에 효과적
# 예) 10명의 자격증 시험 합격자 중에서 여성이 6명이었다고 한다면 '여성이 남성보다 합격률이 높다'라고 할 수 있는가?

import pandas as pd
import scipy.stats as stats

# 직원을 대상으로 고객대응 교육을 실시하면 고객안내 서비스 만족률이 높아질까?
# 귀무 : 직원을 대상으로 고객대응 교육을 실시하면 고객안내 서비스 만족률이 80%이다.
# 대립 : 직원을 대상으로 고객대응 교육을 실시하면 고객안내 서비스 만족률이 80%가 아니다.

data = pd.read_csv('../testdata/one_sample.csv')
print(data.head(3))
print(data['survey'].unique())  # [1 0]

ctab = pd.crosstab(index=data['survey'], columns='count')
ctab.index = ['불만족', '만족']
print(ctab)

print('\n양측검정 : 방향성이 없다 . 기존 80% 만족을 기준으로 실시')
result = stats.binom_test([136, 14], p=0.8, alternative='two-sided')  # stats.binom_test(x:성공 또는 실패 횟수, N:시도 횟수, p가설확률)
print(result)  # 0.00067347 < 0.05   귀무기각. 기존 만족률 80%와 차이가 있다.

result = stats.binom_test([14, 136], p=0.2, alternative='two-sided')
print(result)  # 0.00067347

print('\n단측검정 : 방향성이 있다 (크다, 작다). 기존 80% 만족을 기준으로 실시')
result = stats.binom_test([136, 14], p=0.8, alternative='greater')
print(result)  # 0.00031794

result = stats.binom_test([14, 136], p=0.2, alternative='less')
print(result)  # 0.00031794
