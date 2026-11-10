
from sqlalchemy.orm import Session
from sqlalchemy import select

from models.task import Task
from schemas.task import TaskCreate, TaskPut


def create_task_record(
    db: Session,
    user_id: int,
    task: TaskCreate
):

    new_task = Task(
        title=task.title,
        description=task.description,
        completed=task.completed,
        user_id=user_id
    )

    try:
        db.add(new_task)  #add  new taskobject to ses
        db.commit()#save datab
        db.refresh(new_task)#update

        return new_task

    except Exception:
        db.rollback()
        raise


def get_all_task_records(db: Session):

    statement = select(Task)

    return db.scalars(statement).all()


def get_user_task_records(
    db: Session,
    user_id: int
):

    statement = select(Task).where(
        Task.user_id == user_id
    )

    return db.scalars(statement).all()


def get_task_record(
    db: Session,
    user_id: int,
    task_id: int
):

    statement = select(Task).where(
        Task.task_id == task_id,
        Task.user_id == user_id
    )

    return db.scalars(statement).first()


def replace_task_record(
    db: Session,
    task: Task,
    updated_task: TaskPut
):

    task.title = updated_task.title
    task.description = updated_task.description
    task.completed = updated_task.completed

    try:
        db.commit()
        db.refresh(task)

        return task

    except Exception:
        db.rollback()
        raise


def patch_task_record(
    db: Session,
    task: Task,
    update_data: dict
):

    for field, value in update_data.items():
        setattr(task, field, value)

    try:
        db.commit()
        db.refresh(task)

        return task

    except Exception:
        db.rollback()
        raise


# DELETE 
def delete_task_record(
    db: Session,
    task: Task
):

    deleted_task = {
        "task_id": task.task_id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed,
        "user_id": task.user_id
    }

    try:
        db.delete(task)
        db.commit()

        return deleted_task

    except Exception:
        db.rollback()
        raise
