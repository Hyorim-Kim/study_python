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








except Exception as e:
    print('처리 오류 :', e)

finally:
    cursor.close()
    conn.close()



















