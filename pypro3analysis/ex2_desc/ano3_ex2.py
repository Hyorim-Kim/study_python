# [ANOVA 예제 2]
# DB에 저장된 buser와 jikwon 테이블을 이용하여 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있는지 검정하시오.
# 만약에 연봉이 없는 직원이 있다면 작업에서 제외한다.
# 수정해야함 파일질라

import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import MySQLdb
import pickle
plt.rc('font', family='malgun gothic')

# 귀무 : 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이는 없다.
# 대립 : 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이는 있다.

with open('mydb.dat', mode='rb') as obj:
    config = pickle.load(obj)

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
    select buser_name, jikwon_pay from jikwon
    INNER JOIN buser ON buser_num = buser_no
    """
    cursor.execute(sql)
    # datas = cursor.fetchall() # 이 방법도 있다.
    datas = pd.read_sql(sql, conn)
    
    df = pd.DataFrame(datas)
    df.columns = '부서명', '연봉'
    print(df.head(4))
    print("부서별 평균의 합 : ", df.groupby(['부서명'])['연봉'].mean())
    # 6262 vs 4908 vs 5328 vs 5414 평균 차이?
    
    a = df[df['부서명'] == '총무부']
    a_pay_mean = a.loc[:,'연봉']
    print(a_pay_mean)
    b = df[df['부서명'] == '영업부']
    b_pay_mean = b.loc[:,'연봉']
    print(b_pay_mean)
    c = df[df['부서명'] == '전산부']
    c_pay_mean = c.loc[:,'연봉']
    print(c_pay_mean)
    d = df[df['부서명'] == '관리부']
    d_pay_mean = d.loc[:,'연봉']
    print(d_pay_mean)
    
    # 한 개의 표본이 같은 분포를 따르는지 정규성 확인
    print(stats.shapiro(a_pay_mean)) # pvalue=0.02604 < 0.05 이므로 정규성 불만족
    print(stats.shapiro(b_pay_mean)) # pvalue=0.02560 < 0.05 이므로 정규성 불만족
    print(stats.shapiro(c_pay_mean)) # pvalue=0.41940 < 0.05 이므로 정규성 만족
    print(stats.shapiro(d_pay_mean)) # pvalue=0.90780 < 0.05 이므로 정규성 만족
    
    print()
    # 두 개의 표본이 같은 분포를 따르는지 정규성 확인
    print(stats.ks_2samp(a_pay_mean, b_pay_mean).pvalue)  # 0.33577 > 0.05 이므로 정규성 만족
    print(stats.ks_2samp(a_pay_mean, c_pay_mean).pvalue)  # 0.57517 > 0.05 이므로 정규성 만족
    print(stats.ks_2samp(a_pay_mean, d_pay_mean).pvalue)  # 0.53636 > 0.05 이므로 정규성 만족
    print(stats.ks_2samp(b_pay_mean, c_pay_mean).pvalue)  # 0.33577 > 0.05 이므로 정규성 만족
    print(stats.ks_2samp(b_pay_mean, d_pay_mean).pvalue)  # 0.64065 > 0.05 이므로 정규성 만족
    print(stats.ks_2samp(c_pay_mean, d_pay_mean).pvalue)  # 0.53636 > 0.05 이므로 정규성 만족

    print()
    # 등분산성 : 만족하지 않으면 welchi_anova test 사용
    print(stats.bartlett(a_pay_mean, b_pay_mean, c_pay_mean, d_pay_mean).pvalue) # 0.62909 > 0.05 이므로 등분산성 만족
    
    # 데이터의 퍼짐 정도 시각화
    plt.boxplot([a_pay_mean, b_pay_mean, c_pay_mean, d_pay_mean], showmeans = True)
    plt.show()
    
    print()
    # 일원분산분석 방법 : f_oneway()
    f_sta, pvalue = stats.f_oneway(a_pay_mean, b_pay_mean, c_pay_mean, d_pay_mean)
    print('f통계량 : ', f_sta)   # 0.41244
    print('유의확률 : ', pvalue)  # 0.74544 > 0.05 이므로 귀무 채택.
    # 귀무 : 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이는 없다.
    
    # 사후검정
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    turkeyResult = pairwise_tukeyhsd(endog = df.연봉, groups = df.부서명)
    print(turkeyResult)  # 차이가 없으면 reject가 False가 나오고, 차이가 크면 True가 나온다.

    # 시각화
    turkeyResult.plot_simultaneous(xlabel = 'mean', ylabel = 'group')
    plt.show()
    
    
except Exception as e:
    print('err :', e)
finally:
    cursor.close()
    conn.close()
