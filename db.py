import mysql.connector
from os import environ
from dotenv import load_dotenv

load_dotenv()

sql6462175 = mysql.connector.connect(
    host = environ["BOT_HOST"], 
    user = environ["BOT_USER"],
    password = environ["BOT_PASS"],
    port = environ["BOT_PORT"]
)

if(	sql6462175):
    print("Starting....")