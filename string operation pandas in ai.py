import pandas as pd
data={
    "name": ["KALAI","naveen","  Chandru  ","KARHIKA","akshitha"],
    "age": [26,25,24,29,26],
    "dept": ["IT","Sales","HR","it","SALES"],
    "city": ["Chennai","madurai","TRICHY","chennai","Madurai"]
}
df=pd.DataFrame(data)
print(df)
df["name"]=df["name"].str.lower()
print(df)
df["name"]=df["name"].str.strip()
print(df)
df["dept"]=df["dept"].str.upper()
print(df)
df["city"]=df["city"].str.title()
print(df)
print(df[df["city"].str.contains("chennai",case=False)])

import pandas as pd
data={
    "name": ["KALAI","naveen","  Chandru  ","KARHIKA","akshitha"],
    "age": [26,25,24,29,26],
    "dept": ["IT","Sales","HR","it","SALES"],
    "city": ["Chennai","madurai","TRICHY","chennai","Madurai"],
    "joining_date":["25-06-26","28-06-26","01-07-26","03-07-26","09-07-26",]
    
}
df=pd.DataFrame(data)
print(df)
print(df.dtypes)
df["joining_date"]=pd.to_datetime(df["joining_date"])
print(df)
df["year"]=df["joining_date"].dt.year
print(df)
df["month"]=df["joining_date"].dt.month
print(df)
df["day"]=df["joining_date"].dt.day
print(df)
df["days_worked"]=pd.Timestamp.today()-df["joining_date"]
print(df)
