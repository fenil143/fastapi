from fastapi import FastAPI;

app = FastAPI();

@app.get('/')
def index():
    return {"name":{"firstName":"fenil", "lastName":"mod"}}

@app.get('/blog/{id}')
def show(id : int):
    return {"data":id}

#below function is never going to be executed if you want it to be executed it should be above second function
@app.get('/blog/unpublished')
def show():
    return {"blogs":"unpublished blogs"}


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data':{'1','2'}}