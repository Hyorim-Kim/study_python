# 원격 DB와 연동 후 자료를 읽어 DataFrame에 저장 ... 연습
import MySQLdb
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False  # 한글 처리때 음수가 깨지는 것을 방지하기 위해 사용
import seaborn as sns
import sys
import csv

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
        select jikwon_no,jikwon_name,buser_name,jikwon_pay,jikwon_jik
        from jikwon inner join buser on buser_no=buser_num
    """
    cursor.execute(sql)

    # 문제a-1)
    # 사번 이름 부서명 연봉, 직급을 읽어 DataFrame을 작성
    df = pd.DataFrame(cursor.fetchall(), columns=['번호', '이름', '부서명', '연봉', '직급'])
    print(df.head(10))
    print()
    
    # 문제a-2)
    # DataFrame의 자료를 파일로 저장
    with open('practice_jikdata.csv', mode='w', encoding='utf-8') as fobj:
        writer = csv.writer(fobj)
        for r in cursor:
            writer.writerow(r)

    # 문제a-3)
    # 부서명별 연봉의 합, 연봉의 최대/최소값을 출력
    buser_pay = df.groupby(['부서명'])['연봉'].agg(['sum', 'max', 'min']).reset_index()
    print(buser_pay)
    print()
    
    # 문제a-4)
    # 부서명, 직급으로 교차 테이블(빈도표)을 작성(crosstab(부서, 직급))    
    ctab = pd.crosstab(df['부서명'], df['직급'], margins=True)
    print(ctab)
    print()
    
    # 문제a-5)
    # 직원별 담당 고객자료(고객번호, 고객명, 고객전화)를 출력. 담당 고객이 없으면 "담당 고객  X"으로 표시
    sql2 = """
          select jikwon_name,gogek_no,gogek_name,gogek_tel
          from gogek right outer join 
          jikwon on gogek_damsano=jikwon_no
      """
    cursor.execute(sql2)
    
    df2 = pd.DataFrame(cursor.fetchall(), columns=['직원명', '고객번호', '고객명', '고객전화'])
    df2.fillna('고객 X', inplace=True)
    print(df2)
    print()
    
    # 문제a-6)
    # 부서명별 연봉의 평균으로 가로 막대 그래프를 작성
    jik_ypay = df.groupby(['부서명'])['연봉'].mean()
    plt.bar(jik_ypay.index, jik_ypay)
    plt.title('부서명별 연봉의 평균')
    plt.xlabel('부서명')
    plt.ylabel('평균 연봉')
    plt.show()

    # 문제b-1)
    # pivot_table을 사용하여 성별 연봉의 평균을 출력
    sql3 = """
            select jikwon_no,jikwon_name,buser_name,jikwon_pay,jikwon_jik,jikwon_gen
            from jikwon j join 
            buser b on b.buser_no=j.buser_num
        """
    cursor.execute(sql3)
    df3 = pd.DataFrame(cursor.fetchall(), columns=['사번', '이름', '부서명', '연봉', '직급', '성별'])

    print(df3.pivot_table(['연봉'], index=['성별'], aggfunc=np.mean))
    print()

    # 문제b-2)
    # 성별(남, 여) 연봉의 평균으로 시각화 - 세로 막대 그래프
    jik_a = df3.groupby(['성별'])['연봉'].mean()
    plt.barh(jik_a.index, jik_a)
    plt.show()

    # 문제b-3)
    # 부서명, 성별로 교차 테이블을 작성 (crosstab(부서, 성별))
    tab = pd.crosstab(df3['부서명'], df3['성별'], margins=True)
    print(tab)

except Exception as e:
    print('처리 오류 :', e)
    
finally:
    cursor.close()
    conn.close()
