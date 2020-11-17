import numpy as np
import pandas as pd

arr = np.arange(1,10, 2)
series = pd.Series(arr)
series

test_dict = {"Apfel": 0.99, "Banane": 1.20, "Milch": 1.35}

s = pd.Series(test_dict)
s.index
s.values
np.array([0.99, 1.2, 1.35])

s.dtype
s.sum()
s.min()
s.max()
s.describe()
s.isna()
s.diff()
s.where(s > 1)

#

s.isna().sum()

## Read in data
#https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_r.html

df = pd.read_csv("https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")

df.shape
df.head()
df.index
df.columns

df[df.mpg > 20]
df[df["mpg"] > 20]
df.query("mpg > 20")


df.iloc[1:19,1:3]
df.loc[:, "mpg"]

df.drop("mpg", axis=1)
df.drop(1, axis=0)
df.drop(["mpg", "cyl"], axis=1, inplace=True)
df

df.drop_duplicates(subset=["mpg"], keep="first")
df.sample(10)
df.sample(frac=0.2)
df.sort_values(by=["cyl", "disp"], ascending=False)
df.assign(new = df["mpg"] / 2)

df.describe()
df.groupby("cyl").agg({"mpg": "mean"})
df.groupby("cyl").agg({"cyl": "count"})
df["cyl"].value_counts()

pd.get_dummies(df["cyl"])

df.plot(kind="barh")
