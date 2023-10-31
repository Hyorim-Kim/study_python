# pandas로 파일 읽기
import pandas as pd

# df = pd.read_csv('../testdata/ex1.csv')
df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/ex1.csv")  # web 통해 읽기
print(df, type(df))  # <class 'pandas.core.frame.DataFrame'>
print(df.info())
print()
df = pd.read_table('../testdata/ex1.csv', sep=',')  # read_table은 구분자를 줘야함
print(df)
print(df.info())
print()
df = pd.read_csv('../testdata/ex2.csv', header=None)
print(df)
df = pd.read_csv('../testdata/ex2.csv', header=None, names=['col1', 'col2'])  # column명 부여
print(df)
print()
df = pd.read_csv('../testdata/ex2.csv', header=None, names=['a', 'b', 'c', 'd', 'msg'], index_col='msg')
print(df)
print()
# df = pd.read_csv('../testdata/ex3.txt')  # 하나의 문자열
df = pd.read_table('../testdata/ex3.txt', sep='\s')  # sep=' '   sep='정규표현식', read_csv 해도됨
# \s : space를 표현하며 공백 문자를 의미한다.
# \S : non space를 표현하며 공백 문자가 아닌 것을 의미한다.
print(df)
print(df.info())
print(df.describe())
print()
df = pd.read_table('../testdata/ex3.txt', sep='\s+', skiprows=(1,3))  # 특정 행 제외
print(df)

print()
df = pd.read_fwf('../testdata/data_fwt.txt', widths=(10, 3, 5), \
                 header=None, names=('date', 'name', 'price'), encoding='utf-8')
print(df)

print()
# 대용량의 자료를 chunk(묶음) 단위로 할당해서 처리 가능***
test = pd.read_csv('../testdata/data_csv2.csv', header=None, chunksize=3)
print(test)  # TextFileReader object (텍스트 파서 객체), 메모리 관리에 효율적

for p in test:
    #print(p)
    print(p.sort_values(by=2, ascending=True))

print('\n\nDataFrame 저장')
items = {'apple':{'count':10, 'price':1500}, 'orange':{'count':5, 'price':1000}}
df = pd.DataFrame(items)
print(df)
# print(df.to_html())  # html로 만들어줌
# print(df.to_json())
# print(df.to_clipboard())
# print(df.to_csv())
df.to_csv('test1.csv', sep=',')
df.to_csv('test2.csv', sep=',', index=False)
df.to_csv('test3.csv', sep=',', index=False, header=False)
