#create different differnt kind of requests

from typing import Optional
from fastapi import FastAPI; # type: ignore
from pydantic import BaseModel # type: ignore

app = FastAPI()

class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
    return {'data':f'blog is created with title {request.title}'}
