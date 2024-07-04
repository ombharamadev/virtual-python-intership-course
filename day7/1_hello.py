
from fastapi import FastAPI

import pandas as pd
app = FastAPI()

df = pd.read_csv("student-dataset.csv")

@app.get("/")
def hello():
    return {"text":"Hello world"}

@app.get("/name/{name}")
def print_name(name:str):
    return {f"hello ,{name} ."}

@app.get("/roll/{id}")
def print_roll(id:int):
    student_data = df[df["id"] == id]
    name = str(student_data.name[id])
    country = str(student_data.nationality[id])

    new_js = {
        "roll":str(id),
        "name":name,
        "nationality":country
    }
    return new_js
###git add

