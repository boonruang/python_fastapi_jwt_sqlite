from fastapi import APIRouter
from passlib.context import CryptContext
from ..import models, schemas
from fastapi.params import Depends
from sqlalchemy.orm import Session
from ..database import get_db


router = APIRouter(
    tags=['Seller']
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post('/seller', response_model=schemas.DisplaySeller)
def create_seller(request: schemas.Seller, db: Session = Depends(get_db)):
    hashedpassword = pwd_context.hash(request.password)
    new_seller = models.Seller(
        username=request.username, email=request.email, password=hashedpassword
    )
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller
