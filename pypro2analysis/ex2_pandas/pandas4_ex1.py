import numpy as np
import pandas as pd
titanic = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/titanic_data.csv')
print(titanic.head(3))
print(titanic.columns)
print(titanic['Age'])

bins = [1, 20, 35, 60, 150]
labels = ["소년", "청년", "장년", "노년"]

titanic.Age = pd.cut(titanic['Age'], bins=bins, labels=labels)
# group_survived = titanic.groupby(Age_cut)['Survived'].sum()
# print(group_survived)


print()
print((titanic.pivot_table(values='Survived', index=['Sex'], columns=['Pclass'], aggfunc=np.mean)*100).round(2))

print()
print(titanic.pivot_table(values='Survived', index=['Sex', 'Age'], fill_value=0, columns=['Pclass'], aggfunc=np.mean)*100)

df2 = titanic.pivot_table(values='Survived', index=['Sex', 'Age'], fill_value=0, columns=['Pclass'], aggfunc=np.mean)*100
print(round(df2,2))
