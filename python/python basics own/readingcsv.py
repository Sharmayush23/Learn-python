import pandas as pd

df=pd.read_csv("dataset.csv")
#print(df)

df=pd.read_csv('dataset.csv',nrows=6)
#print(df)

df=pd.read_csv('dataset.csv',usecols=['gender','parental level of education','test preparation course',	'math score',	'reading score','writing score'],nrows=6)

print(df)
df=pd.read_csv('dataset.csv',usecols=['gender','parental level of education','test preparation course',	'math score',	'reading score','writing score'],nrows=6,index_col=0).to_csv('test3.csv')