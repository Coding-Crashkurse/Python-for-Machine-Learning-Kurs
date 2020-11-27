import numpy as np
import pandas as pd
import seaborn as sns


train = pd.read_csv("C:/Users/User/Desktop/PythonForMachineLearning/Titanic/train.csv")
train.head()

# EDA

train.isnull().sum()
sns.heatmap(train.isnull())

train["Survived"].value_counts().plot(kind="pie")


train["Survived"].value_counts(normalize = True) * 100
train["Survived"].value_counts().plot(kind="bar")


train.groupby(['Sex','Survived'])['Survived'].count()