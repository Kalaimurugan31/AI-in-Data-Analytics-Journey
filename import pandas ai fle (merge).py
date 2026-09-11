import pandas as pd
data={
    "name":["auresh","akash","naveen","vignesh","karthick","amudha","vivel","sathish","santhosh"],
    "age":[22,24,23,25,21,20,25,24,28]
}
df1=pd.DataFrame(data)

import pandas as pd
data={
    "name":["auresh","akash","naveen","vignesh","karthick","amudha","vivel","sathish","santhosh"],
    "salary":[25000,50000,15000,26000,10000,23000,24000,26000,24000],
    "age":[22,24,23,25,21,20,25,24,28],
    "dept":["it","sales","purchase","non_voice","sales","purchase","frontend","backend","sales"]
}
df2=pd.DataFrame(data)
print("table1-2columns:")
print(df1)
print("table2-4columns:")
print(df2)
df_merged=pd.merge(df1,df2,on=["name","age"])
print(df_merged)


#csv file read
import pandas as pd
df=pd.read_csv("C:/Users/kalai/OneDrive/Documents/employees.csv")
print(df)
print(df.shape())
print(df.shape())
print(df.describe())