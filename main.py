from fastapi import FastAPI;

app = FastAPI();

@app.get('/')
def index():
    return {"name":{"firstName":"fenil", "lastName":"mod"}}

@app.get('/about')
def about():
    return {"data":["fenil","raj","himu"]}