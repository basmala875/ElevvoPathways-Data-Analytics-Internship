import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\basma\Downloads\titanic.csv")

#UCOMMENT TO RUN

#print(df.describe(include='all'))
#print(df['Survived'].value_counts(normalize= True))


#print('Survival Rate by Gender:')
#print(df.groupby('Sex')['Survived'].mean())

#print('Survval Rate by Class:')
#print(df.groupby('Pclass')['Survived'].mean())

#print('Survval Rate by Gender and Class:')
#print(df.groupby(['Sex','Pclass'])['Survived'].mean())


