from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from aiohttp.web_routedef import head
"""
[two-sample t 검정 : 문제2]  
아래와 같은 자료 중에서 남자와 여자를 각각 15명씩 무작위로 비복원 추출하여
혈관 내의 콜레스테롤 양에 차이가 있는지를 검정하시오.
"""
# 귀무 : 성별 간 혈관 내의 콜레스테롤 양에 차이가 없다.
# 귀무 : 성별 간 혈관 내의 콜레스테롤 양에 차이가 있다.

male = [0.9, 2.2, 1.6, 2.8, 4.2, 3.7, 2.6, 2.9, 3.3, 1.2, 3.2, 2.7, 3.8, 4.5, 4, 2.2, 0.8, 0.5, 0.3, 5.3, 5.7, 2.3, 9.8]
female = [1.4, 2.7, 2.1, 1.8, 3.3, 3.2, 1.6, 1.9, 2.3, 2.5, 2.3, 1.4, 2.6, 3.5, 2.1, 6.6, 7.7, 8.8, 6.6, 6.4]

np.random.seed(1)
np.random.shuffle(male)
np.random.shuffle(female)

male = male[:15]
female = female[:15]
print(male, female)
print(np.mean(male), np.mean(female))

two_sample = stats.ttest_ind(male, female, equal_var=True, alternative='two-sided')
print(two_sample)  # statistic=-1.0276984691893334, pvalue=0.3128883456767575, df=28.0
# 해석 : pvalue=0.31288 > 0.05이므로 귀무 채택, 성별 간 혈관 내의 콜레스테롤 양에 차이가 없다.


print()
"""
[two-sample t 검정 : 문제3]
DB에 저장된 jikwon 테이블에서 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하는지 검정하시오.
연봉이 없는 직원은 해당 부서의 평균연봉으로 채워준다.
"""
# 귀무 : 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하지 않는다.
# 대립 : 총무부, 영업부 직원의 연봉의 평균에 차이가 존재한다.

import MySQLdb
import pickle

with open('mydb.dat', mode='rb') as obj:
    config = pickle.load(obj)

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
    select buser_name, jikwon_pay  from jikwon
    inner join buser on buser_no=buser_num
    """
    cursor.execute(sql)
    datas = cursor.fetchall()
    df = pd.DataFrame(datas)
    df.columns = '부서명', '연봉'
    df.index = range(1, 31)
    print(df.head(5))
    print("부서별 연봉의 평균 : ", df.groupby(['부서명'])['연봉'].mean())
    
    a = df[df['부서명'] == '총무부']
    a_pay_mean = a.loc[:,'연봉']
    print(a_pay_mean)
    b = df[df['부서명'] == '영업부']
    b_pay_mean = b.loc[:,'연봉']
    print(b_pay_mean)
    
    print(stats.shapiro(a_pay_mean)) # pvalue=0.02604 < 0.05 이므로 정규성 불만족
    print(stats.shapiro(b_pay_mean)) # pvalue=0.02560 < 0.05 이므로 정규성 불만족
    
    print(stats.mannwhitneyu(a_pay_mean, b_pay_mean)) # 정규성 만족이 안 될 때 이 방법을 사용한다.
    # statistic=51.0, pvalue=0.47213346080125185
    # 판정 : pvalue=0.4721 > 0.05이므로 귀무 채택, 연봉의 평균에 차이가 존재하지 않는다.

except Exception as e:
    print('err : ', e)

finally:
    cursor.close()
    conn.close()


print()
"""
[대응표본 t 검정 : 문제4]
어느 학급의 교사는 매년 학기 내 치뤄지는 시험성적의 결과가 실력의 차이없이 비슷하게 유지되고 있다고 말하고 있다.
이 때, 올해의 해당 학급의 중간고사 성적과 기말고사 성적은 다음과 같다.
점수는 학생 번호 순으로 배열되어 있다.
그렇다면 이 학급의 학업능력이 변화했다고 이야기 할 수 있는가?
"""
# 귀무 : 시험성적의 결과가 실력의 차이없이 비슷하게 유지되고 있다.
# 대립 : 시험성적의 결과가 실력의 차이없이 비슷하게 유지되고 있지 않다.

mid = [80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80]
fin = [90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95]

print(np.mean(mid))
print(np.mean(fin))

plt.bar(np.arange(2), [np.mean(mid), np.mean(fin)])
plt.show()

pair_sample = stats.ttest_rel(mid, fin)
print('t-value : %.5f, p-value : %.5f'%pair_sample)
# 판정 : p-value : 0.02349 < 0.05이므로 귀무가설 기각
# 블로그 참고해서 답 수정하기
