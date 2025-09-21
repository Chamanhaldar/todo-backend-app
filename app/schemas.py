from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    
class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    completed: Optional[bool]
    
class TodoInDB(TodoBase):
    id:int
    completed: bool
    created_at: datetime
    
    class Config:
        orm_mode = True
        
class TodoResponse(TodoInDB):
    pass