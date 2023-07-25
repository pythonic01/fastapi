from fastapi import  FastAPI , Response , status ,HTTPException , Depends , APIRouter
from .. import models,schema , utils , auth2
from sqlalchemy.orm import Session 
from sqlalchemy import func
from ..database import   get_db
from typing import List, Optional

router = APIRouter(
    prefix="/posts",
    tags=['posts']
)


# # Get the whole post
@router.get("/", response_model=List[schema.Post_Like])
# @router.get("/")
# to pass quary premiters all you need to do is to add it to the function argument as limit in this case
def get_posts(db: Session = Depends(get_db) , current_user: dict =  Depends(auth2.get_current_user),
              limit:int = 10 , skip:int = 0 , search:Optional[str] = ""):
    # posts = cursor.execute(""" SELECT * FROM  post""")
    # posts = cursor.fetchall()
    
    
    result = db.query(models.Post, func.count(models.Like.post_id).label("Num_Like")
                      ).join(models.Like , models.Like.post_id == models.Post.id , isouter=True
        ).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    return  result





# Create a post
@router.post("/" , status_code=status.HTTP_201_CREATED , response_model=schema.PostRsponse)
def create_post(post : schema.CreatePost , db: Session = Depends(get_db) ,current_user: dict =  Depends(auth2.get_current_user)): # the current_user Depandes will force the user to have cridantial before post or do anything requier cridantal
    # cursor.execute("""INSERT INTO post (Post_title , Post_content  , Post_published) VALUES  (%s,%s,%s) """ , (post.title,post.content , post.published))
    # cursor.fetchone()
    # cursor.execute("""SELECT * FROM post""")
    # new_post = cursor.fetchall()
    # connection.commit()    
    print(current_user.email) # give you the user information
    new_post = models.Post(woner_id = current_user.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post




#Get a single post
@router.get("/{id}", response_model=schema.Post_Like )
def get_post(id:int , db: Session = Depends(get_db),current_user: dict =  Depends(auth2.get_current_user)):# ! the id here is an string so you need to convert whaterver you get to the type you awnt unless it's string brcause it's string by defalut
    # cursor.execute("""SELECT * FROM post WHERE Post_id = %s""" , (str(id),))#! note the comma 
    # post = cursor.fetchone()
    
    # post = db.query(models.Post).filter(models.Post.id == id).first()
    post = db.query(models.Post, func.count(models.Like.post_id).label("Num_Like")
                      ).join(models.Like , models.Like.post_id == models.Post.id , isouter=True
        ).group_by(models.Post.id).filter(models.Post.id == id).first()
    
    if not post :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"ID does not exist : {id}")# the best way to handel exaptions
    # if post.woner_id != current_user.id: # to allow user to get his post only
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="not athurise to preform this action")
    
    return post




#delete post
@router.delete("/{id}" , status_code=status.HTTP_204_NO_CONTENT) 
def delete_post(id:int, db: Session = Depends(get_db) ,current_user: dict =  Depends(auth2.get_current_user)):

    post_quary = db.query(models.Post).filter(models.Post.id == id)
    if  post_quary.first() == None: # this means that if no row was deleted means does not exist
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="The Id not found")
    
    if post_quary.first().woner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="not athurise to preform this action")
    
    post_quary.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)#! when we try to make response for delete HTTP method FastApi says that we can't do that sence we deleting 




#update post
@router.put("/{id}", response_model=schema.PostRsponse)
def update_post(id: int,  post:schema.CreatePost,db: Session = Depends(get_db) ,current_user: dict =  Depends(auth2.get_current_user)):
    # cursor.execute("""UPDATE post SET Post_title = %s, Post_content = %s, post_published = %s WHERE Post_id = %s""",
    #                (post.title, post.content, post.published, id))
    # cursor.execute("""SELECT * FROM post WHERE Post_id = %s""", (id,))
    # updated_post = cursor.fetchone()
    quary = db.query(models.Post).filter(models.Post.id == id)
    updated_post = quary.first()

    
    if  updated_post == None: # ! this is monditory if you says if not index this will not work
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The ID not found")
    if updated_post.woner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="not athurise to preform this action")
    quary.update(post.dict(), synchronize_session=False)
    db.commit()
    return quary.first()