import pandas as pd
data={
    "s.no":[1,2,3,4,5,6,7,8,9,10],
    "name":["kalai","kesavan","kayal","vicky","nithish","saravanan","rajesh","suresh","raman","pradeep"],
    "age": [20,22,25,23,28,26,24,29,23,27],
    "dept": ["hr","sales","purchase","it_support","sales","purchase","helpdesk","helpdesk","hr","purchase"],
    "working days":[30,29,27,28,26,24,30,23,28,26],
    "basic_salary":[25000,30000,27000,28000,24000,30000,36000,28000,29000,25000]
}
df=pd.DataFrame(data)
print(df)
df["bonus"]=1000
df["total_salary"] =df["basic_salary"]+df["bonus"]
print(df)
df["bonus"]=df["bonus"]+500
df["total_salary"]=df["bonus"]+df["basic_salary"]
print(df)
print(df[df["total_salary"]>30000])
print(df.drop("bonus",axis=1))
