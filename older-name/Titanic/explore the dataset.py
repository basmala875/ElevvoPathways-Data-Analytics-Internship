import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\basma\Downloads\titanic.csv")

print(df.head())
print(df.info())