from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List

from db import crud, models, schemas
from db.engine import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/create_user", response_model=schemas.User)
def user_create(username: str, email: str, db: Session = Depends(get_db)):
    return crud.create_user(db, username, email)

@app.get("/users/{user_id}")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)

@app.get("/users", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_all_users(db, skip=skip, limit=limit)
    return users