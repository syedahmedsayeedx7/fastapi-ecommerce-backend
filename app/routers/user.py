from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database.session import SessionLocal
from app.schemas.user import UserCreate, UserResponse
from app.schemas.token import Token
from app.services import user_service
from app.oauth2 import verify_token

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Register
@router.post("/", response_model=UserResponse)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return user_service.create_user(db, user)


# Login
@router.post("/login", response_model=Token)
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = user_service.authenticate_user(
        db,
        user_credentials.username,
        user_credentials.password
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    token = user_service.create_user_token(user)

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# Current User
@router.get("/me", response_model=UserResponse)
def current_user(
    user_id: int = Depends(verify_token),
    db: Session = Depends(get_db)
):

    user = user_service.get_user_by_id(
        db,
        user_id
    )

    return user