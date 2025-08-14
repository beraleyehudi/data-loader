from fastapi import FastAPI
from sql_dal import SQLDAL

app = FastAPI()

@app.get("/")
def read_root():
    return "this is data loader service."

@app.get("/get data")
def get_data():
    dal = SQLDAL()
    data = dal.dal_get("my table", "*")
    show_data = {k: v for k, v in data.items()} 
    return show_data
