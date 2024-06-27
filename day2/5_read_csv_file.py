
import pandas as pd 
import json 

df = pd.read_csv("file.csv")
n= 0 
for api in df["name"]:
    name = api
    roll = df["roll"][n]
    json_data = {
        "name":name,
        "roll":roll
    }
    print(json_data)
    n = n +1