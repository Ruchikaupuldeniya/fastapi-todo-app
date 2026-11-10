
from sqlalchemy.orm import Session

from models.user import User
from schemas.user import UserCreate


def create_user_record(db: Session, user: UserCreate):

    new_user = User(
        name=user.name,
        email=str(user.email)
    )

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user

    except Exception:
        db.rollback()
        raise


def get_user_record(db: Session, user_id: int):

    return db.get(User, user_id)
