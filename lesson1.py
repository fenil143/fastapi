from fastapi import FastAPI; # type: ignore

hi = FastAPI();

@hi.get('/')
def index():
    return {"name":{"firstName":"fenil", "lastName":"mod"}}

@hi.get('/about')
def about():
    return {"data":["fenil","raj","himu"]}


'''
to run this file you have to write below command
uvicorn lesson1:hi --reload
here lesson1 is file name 
hi is instance for fastapi
and --reload is used to track any changes
'''