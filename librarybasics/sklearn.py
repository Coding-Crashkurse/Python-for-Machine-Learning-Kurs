import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np

df = pd.read_csv("https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")


X = df[["mpg", "hp"]]
y = df["cyl"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)

clf = RandomForestClassifier(random_state=0)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

from sklearn.metrics import confusion_matrix

accuracy = confusion_matrix(y_test, y_pred).diagonal().sum() / confusion_matrix(y_test, y_pred).sum()

print(f'Accuracy is: {round(accuracy, 4) * 100}% ')