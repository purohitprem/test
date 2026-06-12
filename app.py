from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class tea(BaseModel):
    id :int 
    name : str
    origin : str 

teas: list[tea]=[]

@app.get("/")
def index():
    return {"messege":"Welcome to Prem Tea House "}

@app.get("/teas")
def get_teas():
    return teas

@app.post("/teas")
def add_teas(tea : tea):
    teas.append(tea)
    return teas

@app.put("/teas/{tea_id}")
def update_tea(tea_id:int, updated_tea :tea):
    for index, tea in enumerate(teas):
        if tea.id==tea_id:
            teas[index] = updated_tea
            return updated_tea
    return {"error": "Tea not found"}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id :int):
    for index, tea in enumerate(teas):
        if tea.id==tea_id:
            delete = teas.pop(index)
            return delete
    return {"error": "Tea not found"}

