# JSON 문서 읽기 : 서울시 제공 도서관 정보 5개 읽기(XML을 점점 대체하는 중)
# JSON은 beautifulsoup 아님
import json
import urllib.request as req

url = "https://raw.githubusercontent.com/pykwon/python/master/seoullibtime5.json"
plainText = req.urlopen(url).read()

jsonData = json.loads(plainText)  # json decoding(dumps : encoding)  string을 객체로 바꿈
print(jsonData)
print(type(jsonData))  # <class 'dict'>  loads(json decoding)를 사용했기 때문에 dict

libData = jsonData.get('SeoulLibraryTime').get('row')
print(libData)
name = libData[0].get('LBRRY_NAME')
print(name)  # 잘 나옴

print('\n도서관명\t\t\t\t전화\t\t\t\t주소')
datas = []  # dataframe에 넣기
for ele in libData:
    name = ele.get('LBRRY_NAME')
    tel = ele.get('TEL_NO')
    addr = ele.get('ADRES')
    print(name + '\t' + tel + '\t' + addr)
    imsi = [name, tel, addr]  # list를 만든 후
    datas.append(imsi)  # imsi를 추가

print()
import pandas as pd
df = pd.DataFrame(datas, columns = ['이름', '전화', '주소'])
print(df)
