from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models.user import User
from app.core.security import hash_password

router = APIRouter()

User.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_user(email: str, password: str, db: Session = Depends(get_db)):
    user = User(email=email, hashed_password=hash_password(password))
    db.add(user)
    db.commit()
    return {"id": user.id, "email": user.email}
