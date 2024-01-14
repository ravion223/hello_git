from sqlalchemy.orm import Session
from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.DBUser).filter(models.DBUser.id == user_id).first()

def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.DBUser).offset(skip).limit(limit).all()

def create_user(db: Session, username, email):
    db_user = models.DBUser(username = username, email = email)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user