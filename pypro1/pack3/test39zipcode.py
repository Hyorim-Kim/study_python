# 우편번호 자료 읽기
# 키보드로 '동 이름'을 입력해, 해당 동 자료들만 모두 읽기

try:
    dongName = input('동 이름을 입력: ')
    #print(dongName)
    
    with open(r'zipcode.txt', mode='r', encoding='utf-8') as obj:
        line = obj.readline()
        #print(line)
        
        while line:  # 파일을 끝까지 읽을 때까지 반복
            lines = line.split(' ')
            # print(lines)  # ['135-806', '서울', '강남구', '개포1동', '경남아파트', 'NULL\n']
            
            # str.startswith(str or tuple) 형식으로 사용하면 되고, 반환 값으로는 True, False를 반환
            if lines[3].startswith(dongName):
                #print(lines)
                print('[' + lines[0] + ']' + lines[1] + ' ' + lines[2] + ' ' + lines[3] + ' ' + lines[4])
            
            line = obj.readline()
except Exception as e:
    print('err : ', e)
