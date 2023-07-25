from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from . import config

SQLALCHEMY_DATABASE_URL = f'mysql://{config.setting.DATABASE_USERNAME}:{config.setting.DATABASE_PASSWORD}@{config.setting.DATABASE_HOSTNAME}:{config.setting.DATABASE_PORT}/{config.setting.DATABASE_NAME}'


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
# !to connect to data based without sqlalchemy

# Replace placeholders with your database information
# host = "localhost"  # or your MySQL server IP address
# user = "root"
# password = "Yasser01w"
# database = "fasrapi"
# while True:
# #database connection without sqlalchemy
#     try:
#         connection = mysql.connector.connect(
#         host=host,
#         user=user,
#         password=password,
#         database=database

#     )
#         cursor = connection.cursor(dictionary=True)
#         print("connect sessufly ")
#         break
#     except Exception as error:
#         print("faile to connect : " + str(error))
#         time.sleep(5)
    
    