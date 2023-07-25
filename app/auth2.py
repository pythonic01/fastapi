#handel JWT file (return to fastapi doc for more information(Oauth2))
from jose import JWTError , jwt
from datetime import datetime , timedelta
from sqlalchemy.orm import Session
from app import models
from . import schema , database
from fastapi import Depends , status , HTTPException
from fastapi.security import OAuth2PasswordBearer
from . import config

oauth2_schema = OAuth2PasswordBearer(tokenUrl='login')

#! REQUIERMENT
#SECRETE_KEY
SECRET_KEY = config.setting.SECRET_KEY

#ALGORITH
ALGORITHM = config.setting.ALGORITHM

#EXPIRE_TIME
ACCESS_TOKEN_EXPIRE_MINUTES = config.setting.ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp" : expire})
    #       payload(data), Secrete key, algorithm     
    encode_jwt = jwt.encode(to_encode , SECRET_KEY , algorithm=ALGORITHM)
    return encode_jwt
    

def verify_access_token(token:str , exaptions):
    try:
        payload = jwt.decode(token , SECRET_KEY , algorithms=[ALGORITHM])
        
        id :str = payload.get('user_id')
        
        if id is None:
            raise exaptions
        token_data = schema.TokenData(id = str(id))
    except JWTError:
        raise exaptions
    return token_data # user ID
    
def get_current_user(token:str = Depends(oauth2_schema) ,db:Session = Depends(database.get_db) ):
    cre_exaption = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="could not validate the credinatial" , 
                                 headers={"WWW-Authenticate": "Bearer"})
    
    token = verify_access_token(token , cre_exaption)
    
    user = db.query(models.User).filter(models.User.id == token.id).first()
    return user
    
    
    