from sqlalchemy import *
from sqlalchemy.sql.expression import null
from sqlalchemy.orm import relationship
from .database import Base

class Post(Base):
    __tablename__ = "post"
    
    id =  Column(Integer ,primary_key=True ,nullable=False )
    title = Column(String(100) , nullable=False)
    content = Column(String(100) , nullable=False)
    published = Column(Boolean  , nullable=False , default=True) 
    created_at = Column(TIMESTAMP(timezone=True) , nullable=False , default=text('now()'))
    woner_id = Column(Integer , ForeignKey("users.id" , ondelete="CASCADE") , nullable=False)
    
    woner = relationship("User")# this relationship allows us to retrive an information from another class and also edit the structure from schema.py
    

    
class User(Base):
    __tablename__ = "users"
    
    id =  Column(Integer ,primary_key=True ,nullable=False )
    email = Column(String(250) , nullable=False , unique=True)
    password = Column(String(100) , nullable=True )
    created_at = Column(TIMESTAMP(timezone=True) , nullable=False , default=text('now()'))

    
class Like(Base):
    __tablename__ = "likes"
    user_id = Column(Integer , ForeignKey("users.id" , ondelete="CASCADE") , primary_key=True)
    post_id = Column(Integer , ForeignKey("post.id" , ondelete="CASCADE") ,primary_key=True)