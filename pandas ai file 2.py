import pandas as pd
data={
    "name":["auresh","akash","naveen","vignesh","karthick","amudha","vivel","sathish","santhosh"],
    "age":[22,24,23,25,21,20,25,24,28],
    "working_days":[25,30,26,28,21,20,29,30,29],
    "one_day_salary":[1000,1500,600,700,800,1000,1200,1000,1250],
    "dept":["it","sales","sales","tech support","data migration","it","data migration","tech support","sales"],
    "city":["chennai","madurai","trichy","coimbatore","chennai","madurai","trichy","chennai","coimbatore"]


}
df=pd.DataFrame(data)

#calculate_total_salary
df["basic_salary"]=df["working_days"]*df["one_day_salary"]
print(df)
print(df.sort_values("basic_salary",ascending=True))
print(df.sort_values("age",ascending=True))
print(df.groupby("age")["basic_salary"].mean())
print(df.groupby("age")["basic_salary"].sum())
print(df["dept"].value_counts())
print(df["city"].value_counts())
print(df["dept"].unique())
print(df["dept"].nunique())





