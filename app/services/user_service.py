from sqlalchemy.orm import Session

from app.models.user import User
from app.auth import hash_password, verify_password, create_access_token


def create_user(db: Session, user):

    hashed = hash_password(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def authenticate_user(db: Session, username: str, password: str):

    # username field in OAuth2 will contain the user's email
    user = db.query(User).filter(
        User.email == username
    ).first()

    if user is None:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user


def create_user_token(user: User):

    return create_access_token(
        data={"user_id": user.id}
    )


def get_user_by_id(db: Session, user_id: int):

    return db.query(User).filter(
        User.id == user_id
    ).first()