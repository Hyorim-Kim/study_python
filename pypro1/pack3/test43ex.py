# jikwon 테이블을 대상으로 사번과 이름을 입력(로그인)해 해당 자료가 있다면
# 해당 직원이 근무하는 부서 직원을 직급별 오름차순으로 모두 출력, 직급이 같으면 이름별 오름차순 출력
# 출력 형태 : 사번, 이름, 부서명, 직급, 성별
#                         5   홍길동 총무부  대리    남
#                      인원수 : *명

# 다음으로 해당 직원이 관리하는 고객자료 출력
# 출력 형태 : 고객번호, 고객명, 고객전화, 나이
#                              3        신기해  111-1111  23
#                      관리 고객수 : * 명

import MySQLdb
import pickle

with open(r'mydb.dat', mode='rb') as obj:
    config = pickle.load(obj)

def start():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        
        #jikwon_no, jikwon_name = '1', '홍길동'
        jikwon_no, jikwon_name = input('사번 : '), input('이름 : ')
        sql = """
             select jikwon_no, jikwon_name, buser_num, jikwon_jik, jikwon_gen
             from jikwon
             where jikwon_no={0} and jikwon_name='{1}'
        """.format(jikwon_no, jikwon_name)
        cursor.execute(sql)
        datas = cursor.fetchall()

        if len(datas) == 0:
            print('해당 정보가 없습니다')
            return

        for jikwon_no, jikwon_name, buser_num, jikwon_jik, jikwon_gen in datas:
            print(jikwon_no, jikwon_name, buser_num, jikwon_jik, jikwon_gen)
        

        # 해당 직원이 근무하는 부서 직원 출력
        print('\n부서 직원 목록:')
        sql_department = """
            select jikwon_no, jikwon_name, buser_num, jikwon_jik, jikwon_gen
            from jikwon
            where buser_num={0}
            order by jikwon_jik, jikwon_name
        """.format(buser_num)
        cursor.execute(sql_department)
        department_datas = cursor.fetchall()

        for jikwon_no, jikwon_name, buser_num, jikwon_jik, jikwon_gen in department_datas:
            print(jikwon_no, jikwon_name, buser_num, jikwon_jik, jikwon_gen)

        print('인원수:', len(department_datas))
        
        
        # 해당 직원이 관리하는 고객자료 출력
        print('\n관리 고객 목록:')
        sql_customers = """
            select gogek_no, gogek_name, gogek_tel, 
            timestampdiff(year, substring(gogek_jumin, 1, 6), curdate()) as age
            from gogek
            inner join jikwon on gogek_damsano = jikwon_no
            where jikwon_no={0}
        """.format(jikwon_no)
        # print("Debug: SQL Query for Customers:", sql_customers)  # 디버깅용 출력문 추가
        cursor.execute(sql_customers)
        customers_datas = cursor.fetchall()

        for gogek_no, gogek_name, gogek_tel, age in customers_datas:
            print(gogek_no, gogek_name, gogek_tel, age)

        print('관리 고객수:', len(customers_datas))

    except Exception as e:
        print('에러:', e)
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    start()
