from datetime import datetime

from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from database import engine
from sqlmodel import Session, select
from models import Book
from typing import Optional, List


app = FastAPI()
session = Session(bind=engine)


@app.get("/books", response_model=List[Book], status_code=status.HTTP_200_OK)
async def get_all_books():
    statement = select(Book)
    results = session.exec(statement).all()
    return results


@app.get("/books/{id}")
async def get_books(id: int):
    statement = select(Book).where(Book.id==id)
    results = session.exec(statement).first()
    if results is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No book for ID=={id}")
    return results


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    new_book = Book(title=book.title, description=book.description, price=book.price, created_at=datetime.utcnow())
    session.add(new_book)
    session.commit()
    return new_book


@app.put("/books/{id}", response_model=Book, status_code=status.HTTP_200_OK)
async def update_book(id: int, book: Book):
    statement = select(Book).where(Book.id==id)
    updated_book = session.exec(statement).first()
    if updated_book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    updated_book.title = book.title
    updated_book.description = book.description
    updated_book.price = book.price

    session.commit()
    return updated_book


@app.delete("/books/{id}")
async def delete_book(id: int):
    statement = select(Book).where(Book.id==id)
    deleted_book = session.exec(statement).first()
    if deleted_book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID={id} not found")

    session.delete(deleted_book)

    return None
