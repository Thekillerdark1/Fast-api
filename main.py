from pydantic import BaseModel
from typing import List

from fastapi import FastAPI

import mysql.connector

class people(BaseModel):
    id : int
    first_name : str
    email : str

db_config = {
    "host" : "localhost",
    "user" : "nuevo_usuario",
    "password": "1234@Halo",
    "database": "personas_db"
}

def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection


app = FastAPI()


@app.get("/", response_model=list[people])
def get_users():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("select id, first_name, email from people")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return users

