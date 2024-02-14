from sqlalchemy.orm import Session
from . import models, schemas

def get_user(db:Session, user_id: int):
    return db.query(models.Users).filter(models.Users.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Users).offset(skip).limit(limit).all()

def get_user_by_email(db:Session, email: str):
    return db.query(models.Users).filter(models.Users.email == email).first()

def create_user(db:Session, user: schemas.UsersCreate):
    fake_hasshed_password = user.password
    db_user = models.Users(email=user.email, username=user.username, hashed_password = fake_hasshed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user