from fastapi import  FastAPI 
from . import models
from .database import  engine 
from app.routers.user import router as user_router
from app.routers.post import router as post_router
from app.routers.auth import router as login_router
from app.routers.like import router as like_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://www.google.com",
    "https://www.youtube.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}








# models.Base.metadata.create_all(bind=engine)


    
    
# this how you break the project into sprate files or routs
app.include_router(user_router)
app.include_router(post_router)
app.include_router(login_router)
app.include_router(like_router)


# ! to turn the server on use the command uvicorn <mainfileName>:app --reaload
# !if it was in folder all you need to add is  uvicorn folderName.<mainfileName>:app --reaload
#the root function
@app.get("/" )
def root():
    return {"message": "Yasser's api"} 





