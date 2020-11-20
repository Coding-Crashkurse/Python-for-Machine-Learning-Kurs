import seaborn as sns
import pandas as pd

df = pd.read_csv("https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")

# Histogram
sns.displot(df["mpg"])
sns.displot(df["mpg"], binwidth=1)
sns.displot(df["mpg"], shrink=0.8)

sns.displot(df, x="mpg", hue="cyl")
sns.displot(df, x="mpg", hue="cyl", multiple="stack")
sns.displot(df, x="mpg", hue="cyl", multiple="dodge")

sns.displot(df, x="mpg", col="cyl", multiple="dodge")

sns.displot(df, x="mpg", kind="kde")

# Barplot
sns.barplot(x="cyl", y="wt", data=df)

grouped = df.groupby("cyl").agg({"wt": "mean"}).reset_index()
grouped

sns.barplot(x="cyl", y="wt", data=grouped)

# Lineplot
sns.lineplot(data=df, x="mpg", y="hp")

# Scatterplot
sns.scatterplot(x="mpg", y="wt", hue="cyl", data=df)
sns.scatterplot(x="mpg", y="wt", hue="cyl", data=df)
sns.scatterplot(x="mpg", y="wt", hue="cyl", data=df, s=300, palette=["green", "blue", "red"])
sns.scatterplot(x="mpg", y="wt", hue="cyl", data=df, s=300, palette=["green", "blue", "red"]).set(title="Weight by mpg", xlabel="mpg", ylabel="wt")

# Violinplot
df.columns

df["cyl"].value_counts().plot(kind="pie", y="cyl")


sns.violinplot(x="mpg", data=df)
sns.violinplot(y="mpg", data=df)
sns.violinplot(x="cyl", y="mpg", data=df)

sns.heatmap(df.isna())

df.drop(columns=["model"], axis=1, inplace=True)

sns.heatmap(df)

