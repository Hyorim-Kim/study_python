# JSON 문서 읽기 : 서울시 제공 도서관 정보 5개 읽기(JSON이 XML을 점점 대체하는 중)
# 참고 : JSON은 BeautifulSoup을 이용하지 않음
import json
import urllib.request as req  # 웹 요청을 위한 모듈

url = "https://raw.githubusercontent.com/pykwon/python/master/seoullibtime5.json"
plainText = req.urlopen(url).read()  # 해당 URL로부터 데이터를 읽어와서 plainText로 저장

jsonData = json.loads(plainText)  # json decoding (JSON 형식의 문자열을 Python 객체로 변환하는 함수) / dumps : encoding
print(jsonData)
print(type(jsonData))  # <class 'dict'>  loads(json decoding)했기 때문에 dict

libData = jsonData.get('SeoulLibraryTime').get('row')  # 실제 도서관 정보가 담긴 부분을 가져와서 libData에 저장
print(libData)
name = libData[0].get('LBRRY_NAME')  # 첫 번째 도서관의 이름을 가져와 name에 저장
print(name)  # 잘 나옴

print('\n도서관명\t\t\t\t전화\t\t\t\t주소')
datas = []  # list 생성
for ele in libData:
    name = ele.get('LBRRY_NAME')  # 도서관의 이름
    tel = ele.get('TEL_NO')  # 전화번호
    addr = ele.get('ADRES')  # 주소
    print(name + '\t' + tel + '\t' + addr)  # 출력
    imsi = [name, tel, addr]  # list에 담아
    datas.append(imsi)  # datas에 추가함

print()
import pandas as pd  # pandas 라이브러리를 이용하여
df = pd.DataFrame(datas, columns = ['이름', '전화', '주소'])  # 데이터프레임을 생성하고 출력
print(df)
