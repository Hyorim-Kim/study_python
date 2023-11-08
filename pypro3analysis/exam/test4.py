from pandas import DataFrame
frame = DataFrame({'bun':[1,2,3,4], 'irum':['aa','bb','cc','dd']},
                  index=['a','b', 'c','d'])

print(frame.T)
frame2 = frame.drop('d', axis=0)    # 인덱스가 'd'인 행 삭제
print(frame2)
