import seaborn as sns
titanic = sns.load_dataset('titanic')
print(titanic.head())
print(titanic.pivot_table('survived', index='sex', columns='class'))
