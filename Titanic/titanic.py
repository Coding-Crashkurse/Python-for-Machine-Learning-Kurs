import numpy as np
import pandas as pd
import seaborn as sns


train = pd.read_csv("C:/Users/User/Desktop/PythonForMachineLearning/Titanic/train.csv")
test = pd.read_csv("C:/Users/User/Desktop/PythonForMachineLearning/Titanic/test.csv")

PassengerIds = test["PassengerId"]

# EDA

train.isnull().sum()
for col in train.columns:
    print(col, str(round(100 * train[col].isnull().sum() / len(train), 2)) + "%")

sns.heatmap(train.isnull())

train["Survived"].value_counts().plot(kind="pie")
train["Survived"].value_counts(normalize=True) * 100
train["Survived"].value_counts().plot(kind="bar")

pd.crosstab(train.Pclass, train.Survived, margins=True)

sns.barplot(data=train, x="Sex", y="Survived")

pd.crosstab(train.SibSp, train.Survived, margins=True)
sns.barplot(data=train, x="SibSp", y="Survived", hue="Pclass")


sns.barplot(data=train, x="Sex", y="Survived", hue="Pclass")

sns.barplot(data=train, x="Embarked", y="Survived")
sns.catplot(data=train, y="Embarked", hue="Pclass", kind="count")
sns.factorplot("Pclass", "Survived", hue="Sex", col="Embarked", data=train)

sns.barplot(data=train, y="Survived", x="Embarked", hue="Pclass")
sns.barplot(data=train, y="Survived", x="Embarked", hue="Sex")


train.groupby(["Sex", "Survived"], as_index=False).size()

sns.violinplot("Sex", "Age", hue="Survived", data=train)
sns.violinplot("Sex", "Age", hue="Survived", data=train, split=True)

# Fare
train["Fare"].hist()

sns.heatmap(train.corr(), annot=True)

# Title aus Namen holen
# Categories dummy_codieren

df = pd.concat([train, test])

df["title"] = df["Name"].apply(lambda x: x.split(",")[1].split(".")[0].strip())
df["title"] = df["title"].astype("str")

df["title"].head()
df["title"] == "Mr"

df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)
df["Fare"].fillna(df["Fare"].median(), inplace=True)

def family(x):
    if x == 1:
        return "Single"
    elif x == 2:
        return "Couple"
    else:
        return "Family"


df["Family"] = df["SibSp"] + df["Parch"] + 1
df["Family"] = df["Family"].apply(lambda x: family(x))
df["Family"].fillna(df["Family"])


df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)
df["Age"].fillna(df["Age"].median(), inplace=True)

df["title"].value_counts()
replacements = {"Mme": "Mrs", "Mme": "Mrs", "Ms": "Miss", "Sir": "Mr", "Dona": "Mrs", "Don": "Mr"}

for item in replacements.items():
    df["title"] = df["title"].str.replace(item[0], item[1])

df["title"] = df["title"].apply(lambda x: "Other" if x not in ["Mr", "Miss", "Mrs", "Master"] else x)
df.drop(["Ticket", "Cabin", "Name", "PassengerId", "SibSp", "Parch"], axis=1, inplace=True, errors="ignore")

df = pd.get_dummies(df, columns=["Family", "title", "Sex", "Embarked"], prefix="", prefix_sep="", drop_first=True)
df = pd.get_dummies(df, columns=["Pclass"], prefix="Pclass_", prefix_sep="", drop_first=True)

from sklearn.preprocessing import MinMaxScaler   

scaler = MinMaxScaler()

df[["Age", "Fare"]] = scaler.fit_transform(df[["Age", "Fare"]])

### Train models
from sklearn.model_selection import train_test_split
#from sklearn.metrics import confusion_matrix

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier

from sklearn.model_selection import cross_val_score

random_state = 0
classifiers = []
classifiers.append(LogisticRegression())
classifiers.append(KNeighborsClassifier())
classifiers.append(DecisionTreeClassifier())
classifiers.append(RandomForestClassifier())
classifiers.append(AdaBoostClassifier(DecisionTreeClassifier(), learning_rate=0.1))
classifiers.append(GradientBoostingClassifier())

train = df.iloc[0:len(train),:]
test = df.iloc[len(train): len(df),:]
test.drop("Survived", axis=1, inplace=True)
test.isnull().sum().sum()

X = train.drop("Survived", axis=1)
y = train["Survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


#cms = []
#for clf in classifiers:
#    clf.fit(X_train, y_train)
#    y_pred = clf.predict(X_test)
#    cm = confusion_matrix(y_test, y_pred)
#    cms.append(cm.diagonal().sum() / cm.sum())

cms = []
for clf in classifiers:
    cms.append(cross_val_score(clf, X_train, y_train, cv=10))

### Testset gesamt wieder als test definieren

clf = GradientBoostingClassifier()

parameters = {
    "n_estimators":[5,50,250,500],
    "max_depth":[1,3,5,7,9],
    "learning_rate":[0.01,0.1,1,10,100]
}

from sklearn.model_selection import GridSearchCV
cv = GridSearchCV(clf,parameters,cv=5)

cv.fit(X_train, y_train)
cv.best_params_

y_pred = cv.predict(test)

test_Survived = pd.Series(y_pred, name="Survived").astype("int")
test_Survived

results = pd.concat([PassengerIds,test_Survived],axis=1)
results.tail()

results.to_csv("C:/Users/User/Desktop/PythonForMachineLearning/Titanic/submission.csv", index=False)

