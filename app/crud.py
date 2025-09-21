from sqlalchemy.orm import Session
from . import models, schemas


def get_todo(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()


def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todo).offset(skip).limit(limit).all()


def create_todo(db: Session, todo: schemas.TodoCreate):
    db_obj = models.Todo(**todo.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_todo(db: Session, db_obj: models.Todo, updates: schemas.TodoUpdate):
    for field, value in updates.dict(exclude_unset=True).items():
        setattr(db_obj, field, value)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
    return db_obj


def delete_todo(db: Session, db_obj: models.Todo):
    db.delete(db_obj)
    db.commit()
    return True