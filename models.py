from sqlalchemy import Column
from sqlalchemy import Integer

from app import db

class Fechas(db.Model):
    __tablename__='fechas'
    id=Column(Integer,primary_key=True)