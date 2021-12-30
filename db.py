import mysql.connector
from os import environ
from dotenv import load_dotenv

load_dotenv()

mydb = mysql.connector.connect(
    host = environ["BOT_HOST"], 
    user = environ["BOT_USER"],
    password = environ["BOT_PASS"],
)

if(mydb):
    print("Starting....")