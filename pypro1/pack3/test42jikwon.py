# 키보드로 부서번호를 입력받아 해당 부서의 자료 출력, 인원수도 출력
import MySQLdb
'''
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'seoho123',
    'database':'test',
    'port':3307,
    'charset':'utf8',
    'use_unicode':True
}
'''

import pickle
with open(r'mydb.dat', mode='rb') as obj:
    config = pickle.load(obj)  # pickle로 저장했으므로
    
def start():
    try:
        conn = MySQLdb.connect(**config)
        # print(conn)
        cursor = conn.cursor()
        
        #buser_no = '10'
        buser_no = input('부서번호 입력 : ')
        sql = """
             select jikwon_no, jikwon_name, buser_num, jikwon_pay, jikwon_jik
             from jikwon
             where buser_num={0}
        """.format(buser_no)  # 문자열
        # print(sql)
        cursor.execute(sql)
        datas = cursor.fetchall()
        print(datas)
        print(len(datas))  # 7명
        
        if len(datas) == 0:
            print(buser_no + '번 부서는 없어요')
            return  # sys.exit()도 가능
        
        for jikwon_no, jikwon_name, buser_num, jikwon_pay, jikwon_jik in datas:
            print(jikwon_no, jikwon_name, buser_num, jikwon_pay, jikwon_jik)
            
        print('인원수 : ' + str(len(datas)))
            
    except Exception as e:
        print('err : ', e)
    finally:
        cursor.close()
        conn.close()
    
if __name__ == '__main__':
    start()
