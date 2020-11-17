import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import seaborn as sns

df = pd.read_csv("https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")
df

X = df[["mpg", "hp"]]
y = df["cyl"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)

clf = RandomForestClassifier(random_state=0)
clf.fit(X_train, y_train)


clf.predict_proba(X_test)

y_pred = clf.predict(X_test)

from sklearn.metrics import confusion_matrix

accuracy = confusion_matrix(y_test, y_pred).diagonal().sum() / confusion_matrix(y_test, y_pred).sum()

print(f'Accuracy is: {round(accuracy, 4) * 100}% ')


feat_importances = pd.Series(clf.feature_importances_, index=X.columns)
feat_importances.sort_values(inplace=True, ascending=False)
feat_importances.plot(kind="bar")

