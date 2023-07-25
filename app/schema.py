from datetime import datetime
from typing import Optional
from pydantic import BaseModel , EmailStr, conint


    
class UserCreateResponse(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime
    
    class Config:
        from_attributes= True
        
class PostBase(BaseModel):
    title:str
    content : str
    published : bool = True # optinal
    # raiting : Optional[int] = None # complitile optinal
    
class CreatePost(PostBase):
    
    pass
class Like(BaseModel):
    post_id: int
    like_dir : conint(ge=0, le=1) # this to ensure that the input is less or equal to 1
    

class PostRsponse(PostBase):
    created_at:datetime # for check the validation for the date
    id:int
    woner_id : int
    woner : UserCreateResponse # we can use pydantic model as a data type 
 
    
    class Config:
        from_attributes= True

class Post_Like(BaseModel):
    Post:PostRsponse
    Num_Like : int
    class Config:
        from_attributes= True

        
        
class CreateUser(BaseModel):
    email: EmailStr
    password: str

        
class UserLogin(BaseModel):
    email : EmailStr
    password:str
    
class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id:Optional[str] = None
    
