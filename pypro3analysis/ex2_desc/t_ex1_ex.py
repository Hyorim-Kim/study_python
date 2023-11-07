import numpy as np
import scipy.stats as stats
import pandas as pd
"""
[one-sample t 검정 : 문제1]  
영사기에 사용되는 구형 백열전구의 수명은 250시간이라고 알려졌다. 
한국연구소에서 수명이 50시간 더 긴 새로운 백열전구를 개발하였다고 발표하였다. 
연구소의 발표결과가 맞는지 새로 개발된 백열전구를 임의로 수집하여 수명시간 관련 자료를 얻었다. 
한국연구소의 발표가 맞는지 새로운 백열전구의 수명을 분석하라.
   305 280 296 313 287 240 259 266 318 280 325 295 315 278
"""
# 귀무 : 영사기에 사용되는 백열전구의 수명은 300시간이다.
# 대립 : 영사기에 사용되는 백열전구의 수명은 300시간이 아니다.

data = [305, 280, 296, 313, 287, 240, 259, 266, 318, 280, 325, 295, 315, 278]
print(np.array(data).mean())  # 289.785
# 정규성 확인 생략 - stats.shapiro(data)
result = stats.ttest_1samp(data, popmean=300)
print(result)  # TtestResult(statistic=-1.556435658177089, pvalue=0.143606254517609, df=13)
print('statistic(t값):%.5f, pvalue:%.5f'%result)
# 해석 : pvalue:0.14361 > 0.05이므로 귀무가설 채택. 영사기에 사용되는 백열전구의 수명은 300시간이다.

print('------------------------')
"""
[one-sample t 검정 : 문제2] 
국내에서 생산된 대다수의 노트북 평균 사용 시간이 5.2 시간으로 파악되었다.
A회사에서 생산된 노트북 평균시간과 차이가 있는지를 검정하기 위해서 A회사 노트북 150대를 랜덤하게 선정하여 검정을 실시한다.
실습 파일 : one_sample.csv
참고 : time에 공백을 제거할 땐 ***.time.replace("     ", "")
"""

# 귀무 : A회사에서 생산된 노트북 평균 사용 시간은 5.2 시간이다.
# 대립 : A회사에서 생산된 노트북 평균 사용 시간은 5.2 시간이 아니다.

data2 = pd.read_csv("../testdata/one_sample.csv")
#print(data2.time.replace("     ", ""))
data2['time'] = pd.to_numeric(data2['time'].replace("     ", ""), errors='coerce')
data2 = data2.dropna()  # NaN 값을 평균값으로 대체
print(data2.head(3))
print(np.mean(data2.time))  # 5.556 / 5.2

result2 = stats.ttest_1samp(data2.time, popmean=5.2)
print(result2)  # TtestResult(statistic=3.9460595666462424, pvalue=0.00014166691390197087, df=108)
print('statistic(t값):%.5f, pvalue:%.5f'%result2)
# 해석 : pvalue:0.00014 < 0.05이므로 귀무가설 기각. A회사에서 생산된 노트북 평균 사용 시간은 5.2 시간이 아니다.

print('------------------------')
"""
[one-sample t 검정 : 문제3] 
https://www.price.go.kr/tprice/portal/main/main.do 에서 
메뉴 중  가격동향 -> 개인서비스요금 -> 조회유형:지역별, 품목:미용 자료(엑셀)를 파일로 받아 미용 요금을 얻도록 하자. 
정부에서는 전국 평균 미용 요금이 15000원이라고 발표하였다. 이 발표가 맞는지 검정하시오.
"""

# 귀무 : 전국 평균 미용 요금은 15000원이다.
# 대립 : 전국 평균 미용 요금은 15000원이 아니다.

data3 = pd.read_excel("../testdata/개인서비스.xls")
data3 = data3.dropna(axis=1)
data3 = data3.drop(['번호', '품목'], axis=1)
print(data3.transpose())
print(np.mean(data3.T.iloc[:,0]))  # 18311.875

result3 = stats.ttest_1samp(data3.iloc[0], popmean=15000)
print(result3)  # TtestResult(statistic=6.285993008166382, pvalue=1.4593857848302074e-05, df=15)
print('statistic(t값):%.5f, pvalue:%.5f'%result3)
# 해석 : pvalue:0.00001 < 0.05이므로 귀무가설 기각. 전국 평균 미용 요금은 15000원이 아니다.
