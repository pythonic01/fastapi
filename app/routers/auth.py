from fastapi import APIRouter , Depends , Response, status , HTTPException
from sqlalchemy.orm import Session
from .. import database , schema , models , utils , auth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login' ,response_model=schema.Token)
def login(user_auth : OAuth2PasswordRequestForm = Depends(),db:Session = Depends(database.get_db)): # OOAuth2PasswordRequestForm does not provide email just username and it's the same as email just different name
    user = db.query(models.User).filter(models.User.email == user_auth.username ).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail="no user")
    
    if not utils.verify(user_auth.password , user.password): #the password we reseve from the user - the real password
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="invalid input")
    
    #create token
    access_token = auth2.create_access_token(data={"user_id" : user.id}) # here we use the fuction from auth2 to create the token
    #retuen token
    
    return {"access_token" : access_token , "token_type":"Bearer"}
    
    