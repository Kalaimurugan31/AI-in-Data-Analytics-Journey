import pandas as pd
import numpy as np
data={
    "name":["kalai","naveen","chandru","karhika","akshitha","naresh","karthi","sathish"],
    "age":[26,25,24,29,26,25,26,24,],
    "basic_salary":[26000,25000,28000,24000,36000,26000,15000,20000]
}
df=pd.DataFrame(data)
print(df)
print(df.shape)
print(df.info())
print(df.head())
print(df.tail())
print(df.describe())
print(df["name"])
print(df[["name","age"]])
print(df[df["age"]>26])
print(df[df["basic_salary"]>=26000])
df["bonus"]=1000  
df["total_salary"]=df["basic_salary"]+df["bonus"]
print(df)
df["bonus"]=df["bonus"]+500
df["total_salary"]=df["basic_salary"]+df["bonus"]
print(df)
print(df[df["total_salary"]>30000])
print(df.drop("bonus",axis=1))
print(df)
df.loc[5,"age"]=np.nan
df.loc[7,"basic_salary"]=np.nan
print(df.isnull())
print(df.isnull().sum())
df["age"]=df["age"].fillna(0)
df["basic_salary"]=df["basic_salary"].fillna(0)
df["basic_salary"]=df["basic_salary"].fillna(df["basic_salary"].mean())
print(df)



