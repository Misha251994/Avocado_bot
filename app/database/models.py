from pydantic import BaseModel
from sqlalchemy import Column, Integer, String


class User(BaseModel):
    __tablaname__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, index=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String)
