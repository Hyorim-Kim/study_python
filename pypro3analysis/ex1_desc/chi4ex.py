"""
* 카이제곱 검정
  카이제곱 문제1) 부모학력 수준이 자녀의 진학여부와 관련이 있는가?를 가설검정하시오
  예제파일 : cleanDescriptive.csv
  칼럼 중 level - 부모의 학력수준, pass - 자녀의 대학 진학여부
  조건 :  level, pass에 대해 NA가 있는 행은 제외한다.
"""
# 귀무 : 부모학력 수준이 자녀의 진학여부와 관련이 없다.
# 대립 : 부모학력 수준이 자녀의 진학여부와 관련이 있다.

import pandas as pd
import scipy.stats as stats

data1 = pd.read_csv("../testdata/cleanDescriptive.csv")  # 표본자료
print(data1.head(3), data1.shape)
print(data1.columns)
data1 = data1.dropna(subset=['level', 'pass'])
print(data1['level'].unique())  # 독립변수
print(data1['pass'].unique())  # 종속변수
# 교차표 작성
ctab = pd.crosstab(index=data1['level'], columns=data1['pass'])
ctab.index=['대학원졸', '대졸', '고졸']
ctab.columns=['O', 'X']
print(ctab)

chi2, p, dof, _ = stats.chi2_contingency(ctab)
print('chi2:{}, p:{}, dof:{}'.format(chi2, p, dof))
# chi2:2.7669512025956684, p:0.25070568406521365, dof:2
# 판정 : p:0.2507056 > 0.05 이기 때문에 유의한 수준(α=0.05)에서 귀무가설 기각에 실패
# 발생된 데이터는 우연히 발생된 자료이다.
# 부모학력 수준이 자녀의 진학여부와 관련이 없다.


"""
  카이제곱 문제2) 지금껏 A회사의 직급과 연봉은 관련이 없다. 
  그렇다면 jikwon_jik과 jikwon_pay 간의 관련성 여부를 통계적으로 가설검정하시오.
  예제파일 : MariaDB의 jikwon table 
  jikwon_jik   (이사:1, 부장:2, 과장:3, 대리:4, 사원:5)
  jikwon_pay (1000 ~2999 :1, 3000 ~4999 :2, 5000 ~6999 :3, 7000 ~ :4)
  조건 : NA가 있는 행은 제외한다.
"""
# 귀무 : A회사의 직급과 연봉은 관련이 없다. 
# 대립 : A회사의 직급과 연봉은 관련이 있다.







