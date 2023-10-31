import pandas as pd

# 1. human.csv 파일을 읽어오기
df = pd.read_csv('../testdata/human.csv')
print(df)

# 데이터프레임의 칼럼명에 있는 공백 제거
df.columns = df.columns.str.strip()

# NA 공백 제거
df = df[df['Group'].str.strip() != 'NA']

# 2. Group이 NA인 행 삭제
df = df.dropna(subset=['Group'])
print(df)

# 3. Career, Score 칼럼 추출하여 데이터프레임 작성
df = df[['Career', 'Score']]
print(df.head(3))

# 4. Career, Score 칼럼의 평균 계산
avg_career = df['Career'].mean()
avg_score = df['Score'].mean()

# 결과 출력
print(df)
print(f'평균 Career: {avg_career}')
print(f'평균 Score: {avg_score}')
print(df.mean())

print()
# 1. tips.csv 파일을 읽어오기
df2 = pd.read_csv('../testdata/tips.csv')

# 2. 파일 정보 확인
print("파일 정보:")
print(df2.info())

# 3. 앞에서 3개의 행만 출력
print("\n앞에서 3개의 행 출력:")
print(df2.head(3))

# 4. 요약 통계량 보기
print("\n요약 통계량:")
print(df2.describe())

# 5. 흡연자, 비흡연자 수 계산
smoker_counts = df2['smoker'].value_counts()
print("\n흡연자, 비흡연자 수:")
print(smoker_counts)

# 6. 요일을 가진 칼럼의 유일한 값 출력
unique_days = df2['day'].unique()   # pd.unique(df2['day']), 파이썬의 set에 넣었다 빼도됨
print("\n요일의 유일한 값:")
print(unique_days)
