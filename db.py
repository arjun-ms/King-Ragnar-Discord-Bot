# import mysql.connector
from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String
from os import environ
from dotenv import load_dotenv

load_dotenv()

# sql3463755 = mysql.connector.connect(
#     host = environ["BOT_HOST"], 
#     user = environ["BOT_USER"],
#     password = environ["BOT_PASS"],
#     port = environ["BOT_PORT"]
# )

# if(sql3463755):
#     print("Starting....")

host = environ["BOT_HOST"], 
user = environ["BOT_USER"],
password = environ["BOT_PASS"],
port = environ["BOT_PORT"],
database = environ["BOT_DB"]

url = f"mysql://{user}:{password}@{host}:{port}/{database}"
