from fastapi import  FastAPI , Response , status ,HTTPException , Depends , APIRouter
from .. import models,schema , utils
from sqlalchemy.orm import Session 
from ..database import   get_db
from typing import List


router = APIRouter(
    prefix="/users",
    tags=['users']
)

@router.post("/" , status_code=status.HTTP_201_CREATED , response_model=schema.UserCreateResponse )
def Create_User(user : schema.CreateUser , db: Session = Depends(get_db) ):
    #hash the password
    user.password = utils.hash(user.password)
    #----------
    
    
    new_user = models.User(**user.dict()) # unpack the dictionary
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



@router.get('/{id}' , response_model=schema.UserCreateResponse)
def get_user(id:int , db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="user is not found")
    return user
