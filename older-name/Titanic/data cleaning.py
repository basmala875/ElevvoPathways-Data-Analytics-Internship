import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\basma\Downloads\titanic.csv")

#print(df.isnull().sum())

df['Age'].fillna(df['Age'].median(), inplace= True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace= True)
df.drop(columns=['Cabin'], inplace= True)

df['Survived']= df['Survived'].astype('category')
df['Pclass']= df['Pclass'].astype('category')

print(df.isnull().sum())
