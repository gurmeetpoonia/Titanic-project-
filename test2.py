import pandas as pd
data={
    "Name":["gurmeet","rahul","deepak"],
    "marks":[56,60,45]
}
df=pd.DataFrame(data)
print(df)
df = pd.read_csv("students.csv")

#print(df)
#print(df.head())
#print(df.head(10))
#print(df.tail())
#print(df.columns)
#print(df.info())
print(df.describe())
print(df["age"])
print(df[["age", "G2"]])
print(df.loc[0])
print(df[df["age"] > 18])
df["age+5"] = df["age"] + 5
print(df["age+5"])
#print(df.drop("age", axis=1))
print(df.isnull())
print(df.isnull().sum())
print(df.sort_values("age"))
print(df.sort_values("age", ascending=False))
(df.to_csv("output.csv"))
print(df["sex"].unique())

print(df["sex"].value_counts())
print(df.loc[67])
print(df.iloc[0,30])