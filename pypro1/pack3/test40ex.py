# test40su.txt 파일을 한 행 씩 읽어 각 행의 숫자의 합을 출력하시오

try:
    with open('test40su.txt', mode='r', encoding='utf-8') as obj:
        line = obj.readline()  # 한 행씩 읽어서 line에 저장
        
        while line:  # 파일을 끝까지 읽을 때까지 반복
            # 각 행을 공백(탭)을 기준으로 나누어 숫자들을 리스트로 저장
            numbers = line.split('\t')
            # numbers = line.split(chr(9))  # ASCII 코드값
            
            # 각 숫자를 float으로 변환하고 합 구하기
            total = sum(float(i) for i in numbers)
            
            # 현재 읽은 행의 원본 내용과 숫자의 합을 출력
            print(f'{line.strip()}의 숫자 합: {total}')
            
            line = obj.readline()  # 다음 행을 읽어옴
except Exception as e:
    print('err : ', e)
