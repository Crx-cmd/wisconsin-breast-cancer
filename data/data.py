import pandas as pd
import os

print(os.getcwd())

df = pd.read_csv("/Users/heinerploog/Desktop/Github/wisconsin-breast-cancer/data/data.csv")
print(df)

print(df.columns)