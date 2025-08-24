from fastapi import Depends, FastAPI # type: ignore
from sqlalchemy.orm import Session # type: ignore
from . import models, schemas, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog')
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blogs')
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}')
def blog(id, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog