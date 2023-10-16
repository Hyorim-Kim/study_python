# jikwon 테이블을 대상으로 사번과 이름을 입력 ( 로그인 ) 해 해당자료가 있다면,
# 해당 직원이 근무하는 부서 직원을 직급별 오름차순으로 모두 출력, 직급이 같으면 이름별 오름차순
# ( 사번, 이름, 부서명, 직급, 성별 )
#   5   홍길동 총무부  대리   남
# 인원수: *명
# 다음으로 해당 직원이 관리하는 고객자료 출력
# 출력 형태 : 고객 번호 고객명 고객전화 나이
#            3   신기해  111-1111 23
#       관리 고객수: *명


# 키보드로 부서번호를 입력받아, 해당 부서의 자료 출력 + 인원수도 출력
import MySQLdb
import pickle
with open(r'mydb.dat', mode='rb') as obj:
    config = pickle.load(obj)
def chulbal():
    try:
        conn = MySQLdb.connect(**config)
        print(conn)
        cursor = conn.cursor()

        jikwon_no = input('사번 입력 : ')
        jikwon_name=input('이름 입력 : ')

        sql = """
            select buser_num from jikwon 
            where jikwon_no ={0} and jikwon_name='{1}'
         """.format(jikwon_no, jikwon_name)
        cursor.execute(sql)
        datas = cursor.fetchall()
        if len(datas) == 0:
            print('사번 또는 이름을 확인하세요')
            return
        buser_num = datas[0][0]
        sql = """
            select jikwon_no, jikwon_name, buser_name, jikwon_jik, jikwon_gen
             from jikwon inner join buser on buser_num = buser_no where buser_num={0} order by jikwon_jik, jikwon_name
        """.format(buser_num)
        cursor.execute(sql)
        datas = cursor.fetchall()
        print('사번' + '\t 이름' + '\t 부서명'+ '\t 직급'+ '\t성별')
        for r in cursor:
            print(r[0],"\t",r[1],"\t",r[2],"\t",r[3],"\t",r[4])
        print('인원수 : '+ str(len(datas)) + '명\n\n')

        sql ="""
            select gogek_no, gogek_name, gogek_tel,CAST(substr(DATE_FORMAT(CURDATE(), '%Y'),1,4)-(substr(gogek_jumin, 1,2)+1900) AS signed integer)
            from gogek inner join jikwon on jikwon_no = gogek_damsano where jikwon_no = {0}
        """.format(jikwon_no)
        cursor.execute(sql)
        datas = cursor.fetchall()
        if len(datas) == 0:
            print('담당 고객이 없습니다')
            return
        print('고객번호' + '\t고객명' + '\t\t고객전화'+ '\t\t나이')
        for r in cursor:
            print(r[0],"\t\t",r[1],"\t",r[2],"\t",r[3])
        print('관리 고객수 : '+ str(len(datas)) + '명')
    except Exception as e:
        print("err : ", e)
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    chulbal()
