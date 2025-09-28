import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\basma\Downloads\titanic.csv")

sns.barplot(x='Sex', y='Survived', data=df, palette= ['blue', 'red'])
plt.title('Survival Rate by Gender')
plt.show()

sns.barplot(x='Pclass', y='Survived', data=df)
plt.title('Survival Rate by CLass')
plt.show()

sns.catplot(
    x="Sex", 
    y="Survived", 
    col="Pclass", 
    kind="bar", 
    data=df,
    palette={"male": "blue", "female": "red"}
)
plt.title('Survval Rate by Gender and Class')
plt.show()

sns.histplot(data=df, x='Age', hue='Survived', multiple='stack')
plt.title("Age Distribution by Survival")
plt.show()




