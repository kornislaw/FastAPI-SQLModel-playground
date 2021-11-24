from sqlmodel import SQLModel
from models import Book
from database import engine

print("Creating the database...")

SQLModel.metadata.create_all(engine)

