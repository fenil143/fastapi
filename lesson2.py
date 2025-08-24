from fastapi import FastAPI;

app = FastAPI();

@app.get('/')
def index():
    return {"name":{"firstName":"fenil", "lastName":"mod"}}

@app.get('/blog/{id}')
def show(id):
    return {"data":id}


