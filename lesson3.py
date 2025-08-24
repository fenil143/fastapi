#query parameters

from fastapi import FastAPI;
from typing import Optional;

app = FastAPI();

#to make request below 
#http://127.0.0.1:8000/blog?limit=10&published=true
#you can also give default values
# Optional is used to provide optional values...

@app.get('/blog')
def index(limit : Optional[int], published : bool):
    if published:
        return {'data':f'{limit} published blogs from the db.'}
    else :
        return {'data':f'{limit} blogs from the db'}

#you can also provide query parameter with path parameter
@app.get('/blog/{id}/comments')
def comments(id,limit = 10):
    return {"id":id,"limit":limit}