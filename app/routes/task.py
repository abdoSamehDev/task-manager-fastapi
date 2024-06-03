from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas
from ..crud import task as crud
from ..database import get_db
from ..auth import get_current_user

router = APIRouter()


@router.post("/", response_model=schemas.Task)
async def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    task = crud.create_task(db=db, user_id=current_user.id, task=task)
    return task


@router.get("/", response_model=List[schemas.Task])
async def read_tasks(
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
    skip: int = 0,
    limit: int = 10,
):
    tasks = crud.get_tasks(db=db, skip=skip, limit=limit)
    return tasks


@router.get("/{task_id}", response_model=schemas.Task)
async def read_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    db_task = crud.get_task(db=db, task_id=task_id)
    if db_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    return db_task


@router.put("/{task_id}", response_model=schemas.Task)
async def update_task(
    task_id: int,
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    db_task = crud.update_task(db=db, task_id=task_id, task=task)
    if db_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    return db_task


@router.delete("/{task_id}", response_model=schemas.Task)
async def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
):
    db_task = crud.delete_task(db=db, task_id=task_id)
    if db_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    return db_task
