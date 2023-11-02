# 원격 DB와 연동 후 자료를 읽어 DataFrame에 저장 ...
import MySQLdb
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False  # 한글 처리때 음수가 깨지는 것을 방지하기 위해 사용
import seaborn as sns
import sys

try:
    with open('mydb.dat', mode='rb') as obj:
        config = pickle.load(obj)
        
except Exception as e:
    print('연결 오류 :', e)
    sys.exit()

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwon_no,jikwon_name,jikwon_jik,buser_name,jikwon_gen,jikwon_pay
        from jikwon j join 
        buser b on b.buser_no=j.buser_num
    """
    cursor.execute(sql)

    # 출력1 : console
    for a, b, c, d, e, f in cursor:
        print(a, b, c, d, e, f)
    print()

    # 출력2 : DataFrame
    df = pd.DataFrame(cursor.fetchall(),
                      columns=['jikwon_no', 'jikwon_name', 'jikwon_jik', 'buser_name', 'jikwon_gen', 'jikwon_pay'])
    print(df.head(3), len(df))
    print()

    # 출력3 : csv 파일로 저장
    import csv

    with open('jikdata.csv', mode='w', encoding='utf-8') as fobj:
        writer = csv.writer(fobj)
        for r in cursor:
            writer.writerow(r)

    print()

    # 저장된 csv 읽기
    df2 = pd.read_csv('jikdata.csv', header=None, names=['번호', '이름', '직급', '부서명', '성별', '연봉'])
    print(df.head(3))
    print()

    # 출력4 : DataFrame의 sql 이용
    df3 = pd.read_sql(sql, conn)
    df3.columns = ['번호', '이름', '직급', '부서명', '성별', '연봉']
    print(df3.head(3))

    # DataFrame의 자료로 기술 통계 :
    print(df3[:3])
    print()

    print(df3[:-27])
    print()

    print('건수 : ', len(df3), df3['이름'].count())
    print()

    print('직급별 인원수 : ', df3['직급'].value_counts())
    print()

    print('연봉 평균 : ', df3.loc[:, '직급'].value_counts())
    print()

    print('연봉 평균의 표준편차 : ', df3.loc[:, '연봉'].std())
    print()

    print(df3.loc[:, '연봉'].describe())  # 요약 통계량
    print()

    print(df3.loc[df3['연봉'] >= 7000])  # 요약 통계량
    print()
    
    # 교차표
    ctab = pd.crosstab(df3['성별'], df3['직급'], margins=True)
    print(ctab)
    print()
    
    print(df3.groupby(['성별', '직급'])['이름'].count())
    print()

    print(df3.pivot_table(['연봉'], index=['성별', '직급'], aggfunc=np.mean))

    # 시각화 : pie
    jik_ypay = df3.groupby(['직급'])['연봉'].mean()  # 반환값 Series
    print(jik_ypay.index)
    print(jik_ypay.values)
    plt.pie(jik_ypay, labels=jik_ypay.index, shadow=True, labeldistance=0.7, counterclock=False)
    plt.close()

except Exception as e:
    print('처리 오류 :', e)

finally:
    cursor.close()
    conn.close()
