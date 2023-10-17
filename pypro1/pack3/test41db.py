# 원격 database(MariaDB)와 연동
# sangdata 자료 출력

import MySQLdb
'''
conn = MySQLdb.connect(host = '127.0.0.1', user = 'root', password='seoho123', database='test')  # connect는 dict로 받음
print(conn)
conn.close()
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

try:
    conn = MySQLdb.connect(**config)  # dict 받을 때는 **를 작성, 원격 DB 연결 객체가 생성됨
    #print(conn)
    cursor = conn.cursor()  # sql문 실행 및 select의 결과를 기억
    
    # 자료 추가
    # sql = "insert into sangdata values(6, '마이쮸', 50, '1000')"
    # cursor.execute(sql)  # sql문 실행

    # commit 자료 추가
    '''
    sql = "insert into sangdata values(%s, %s, %s, %s)"  # 문자열
    # sql_data = (6, '마이쮸', 50, '1000')
    sql_data = 6, '마이쮸', 50, '1000'  # tuple은 괄호를 두르지 않아도 ok
    cursor.execute(sql, sql_data)
    # result = cursor.execute(sql, sql_data)  # 성공하면 1, 실패하면 0, 값을 보고 확인 가능
    conn.commit()  # 자동커밋 아니기 때문에
    '''
    # 자료 수정
    '''
    sql = "update sangdata set sang=%s,su=%s,dan=%s where code=%s"
    sql_data = ('에너지바', 12, 1500, 5)
    result = cursor.execute(sql, sql_data)
    print(result)
    conn.commit()
    '''
    # 자료 삭제
    code = '6'  # 문자열로 만들어야 함
    # sql = "delete from sangdata where code=" + code  # 문자열 더하기 비권장 : secure coding 가이드라인에 위배
    
    # sql = "delete from sangdata where code=%s"
    # count = cursor.execute(sql, code)
    
    sql = "delete from sangdata where code='{0}'".format(code)
    count = cursor.execute(sql)
    if count != 0:
        print('삭제 성공')
        conn.commit()
    else:
        print('삭제 실패')
    
    # 자료 읽기
    sql = "select code,sang,su,dan from sangdata"
    cursor.execute(sql)  # sql문 실행, select문의 결과를 cursor가 갖고 있음
    
    # 출력1
    for data in cursor.fetchall():
        #print(data)  # tuple 형식으로 출력
        print('%s %s %s %s'%data)
        
    print()
    # 출력2
    for r in cursor:
        #print(r)  # tuple 형식으로 출력
        print(r[0], r[1], r[2], r[3])
        
    print()
    # 출력3
    for (code,sang,su,dan) in cursor:
        print(code,sang,su,dan)
    
    print()
    # 출력3-1  # cursor가 가지고 있는 레코드 값 순서대로 출력되기 때문에 변수명은 상관없음
    for a, kbs, su, 단가 in cursor:
        print(a, kbs, su, 단가)
    
except Exception as err:
    print('에러 : ', err)
    conn.rollback()
finally:
    cursor.close()
    conn.close()
