from fastapi import  FastAPI , Response , status ,HTTPException , Depends , APIRouter

from app import auth2
from .. import models,schema , utils
from sqlalchemy.orm import Session 
from ..database import   get_db
from typing import List

router = APIRouter(
    prefix="/like"
)


@router.post("/" , status_code=status.HTTP_201_CREATED)
def like( like:schema.Like ,db: Session = Depends(get_db) ,current_user: dict =  Depends(auth2.get_current_user)):
    post_quary = db.query(models.Post).filter(models.Post.id == like.post_id).first()
    if not post_quary:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="The post does not exist")
    vote_quary = db.query(models.Like).filter(models.Like.post_id == like.post_id , models.Like.user_id == current_user.id)
    found_like = vote_quary.first()
    if like.like_dir == 1:
        if found_like:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail=f"the post is already Liked by you ")
        new_like = models.Like(post_id = like.post_id , user_id = current_user.id)
        db.add(new_like)
        db.commit()
        return {"massage " : "you added a Like"}
    else:
        if not found_like:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="vote does not exsit")
        vote_quary.delete(synchronize_session=False)
        db.commit()
        
        return {"massage" : "The vote has deleted"}