import pandas as pd
import scipy.stats

# 귀무 : 등급에 따라 생존율이 차이가 없다.
# 대립 : 등급에 따라 생존율이 차이가 있다.

titanic = pd.read_csv('../testdata/titanic_data.csv')
print(titanic.head(3))

# 교차 테이블 생성
cross_table = pd.crosstab(titanic['Pclass'], titanic['Survived'])

# 이원카이제곱 검정 수행
chi2, pvalue, _, _ = scipy.stats.chi2_contingency(cross_table)

# 결과 출력
print('chi2:{}, pvalue:{}'.format(chi2, pvalue))

# 해석
# pvalue:4.549251711298793e-23 < 0.05 이므로 귀무가설 기각, 등급에 따라 생존율이 차이가 있다.
