# 에러의 종류
# syntax : 문법 오류
# logic : 프로그램 실행 중에 발생하는 오류로 프로그램이 비정상적으로 종료되는 오류
# exception : 예외는 코드를 실행하는 중에 발생하는 에러, try ~ except 문 사용

def divide(a, b):  # 함수
    return a / b
'''
print('뭔가를 하다가...')
c = divide(5, 0)
print(c)
'''
try:  # 일반 영역
    c = divide(5, 2)
    #c = divide(5, 0)
    
    aa = [1, 2]
    print(aa[0])
    #print(aa[2])
    
    f = open(r'c:/work/abc/txt')  # 없는 파일 열기
    print('계속')
    
except ZeroDivisionError:  # 에러 발생
    print('두 번째 숫자는 0을 주지 마시오')
except IndexError as e:
    print('참조 범위 오류 : ', e)
except Exception as err:  # 이외의 나머지 에러는 에러의 super class인 Exception을 이용
    print('에러 발생 :' , err)
finally:  # 에러와 상관없이 실행
    print('에러 유무에 상관없이 반드시 수행됨')

print('프로그램 종료')
