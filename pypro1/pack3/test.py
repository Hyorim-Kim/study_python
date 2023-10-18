# 원격 데이터베이스 서버의 테이블과 연동하는 프로그램을 작성하려고 한다.
# 아래의 출력 예와 같이 키보드로 직급을 입력받아 해당 직급의 직원을 출력하는 코드를 작성하시오.
# 출력 대상은 직원번호, 직원명, 직급, 부서번호 이다.

# 조건 : 테이블은 MariaDB의 jikwon을 사용하기로 한다. (배점:10)

import MySQLdb
import pickle

with open(r'mydb.dat', mode='rb') as obj:
    config = pickle.load(obj)

def chulbal():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()

        jikwon_jik = input('직급 입력: ')

        sql = """
            select jikwon_no, jikwon_name, jikwon_jik, buser_num 
            from jikwon 
            where jikwon_jik = '{0}'
         """.format(jikwon_jik)

        cursor.execute(sql)
        datas = cursor.fetchall()

        if len(datas) == 0:
            print('직급을 확인하세요')
            return

        for r in datas:
            print(r[0], "\t", r[1], "\t", r[2], "\t", r[3])

    except Exception as e:
        print("err : ", e)
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    chulbal()
