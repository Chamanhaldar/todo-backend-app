from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud, models
from ..database import get_db

# Instead of making all routes in main.py, we create a separate router for todo-related endpoints

router = APIRouter(prefix="/todos", tags=["todos"])


@router.post("/", response_model=schemas.TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo)


@router.get("/", response_model=List[schemas.TodoResponse])
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_todos(db, skip=skip, limit=limit)


@router.get("/{todo_id}", response_model=schemas.TodoResponse)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_todo(db, todo_id)
    if not db_obj:
       raise HTTPException(status_code=404, detail="Todo not found")
    return db_obj


@router.put("/{todo_id}", response_model=schemas.TodoResponse)
def update_todo(todo_id: int, updates: schemas.TodoUpdate, db: Session = Depends(get_db)):
    db_obj = crud.get_todo(db, todo_id)
    if not db_obj:
      raise HTTPException(status_code=404, detail="Todo not found")
    return crud.update_todo(db, db_obj, updates)


@router.delete("/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_todo(db, todo_id)
    if not db_obj:
      raise HTTPException(status_code=404, detail="Todo not found")
    crud.delete_todo(db, db_obj)
    return {"ok": True}