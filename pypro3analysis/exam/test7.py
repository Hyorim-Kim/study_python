from pandas import DataFrame

data = {"a": [80, 90, 70, 30], "b": [90, 70, 60, 40], "c": [90, 60, 80, 70]}
df = DataFrame(data)

# 컬럼(열) 이름 변경
df.columns = ["국어", "영어", "수학"]

# 1) 모든 학생의 수학 점수 출력
print(df['수학'])

# 2) 모든 학생의 수학 점수의 표준편차 출력
print(df['수학'].std())

# 3) 모든 학생의 국어와 영어 점수를 DataFrame으로 출력
print(df[['국어', '영어']])
