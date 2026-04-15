import pandas as pd
from preprocess import preprocess

#  Loading Dataset
df=pd.read_csv('data.csv')

#  Applying Preprocessing
df['Processed']=df['Question'].apply(preprocess)

# Data Sample
print("*******************Processed Data Sample************************")
print(df[['Question','Processed']].head())