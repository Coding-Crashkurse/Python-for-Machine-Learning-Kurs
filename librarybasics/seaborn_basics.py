import seaborn as sns
import pandas as pd

df = pd.read_csv(
    "https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv"
)

sns.displot(df["mpg"], binwidth=1)
sns.displot(df["mpg"], shrink=0.8)

sns.displot(df, x="mpg", hue="cyl")
sns.displot(df, x="mpg", hue="cyl", multiple="stack")
sns.displot(df, x="mpg", hue="cyl", multiple="dodge")

sns.displot(df, x="mpg", col="cyl", multiple="dodge")

sns.displot(df, x="mpg", kind="kde")


# Scatterplot
sns.scatterplot(x="mpg", y="disp", hue="cyl", data=df)
sns.scatterplot(x="mpg", y="disp", hue="cyl", data=df)
sns.scatterplot(
    x="mpg", y="disp", hue="cyl", data=df, s=300, palette=["green", "blue", "red"]
)
sns.scatterplot(
    x="mpg", y="disp", hue="cyl", data=df, s=300, palette=["green", "blue", "red"]
).set(title="bla", xlabel="bla", ylabel="muh")

# Violinplot
df.columns

sns.violinplot(x="mpg", data=df)
sns.violinplot(y="mpg", data=df)
sns.violinplot(x="cyl", y="mpg", data=df)

df["cyl"].value_counts().plot(kind="pie", y="cyl")


sns.heatmap(df.isna())

df.drop(columns=["model"], axis=1, inplace=True)

sns.heatmap(df)


sns.lineplot(data=df, x="mpg", y="hp")
