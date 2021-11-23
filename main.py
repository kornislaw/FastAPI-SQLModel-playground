from fastapi import FastAPI
from sqlmodel import SQLModel

app = FastAPI()


class Book(SQLModel):
    pass


@app.get("/books")
async def get_all_books():
    return {"message": "getting all books - placeholder"}


@app.get("/books/{id}")
async def get_books(id: int):
    return {"message": "getting a book - placeholder"}


@app.post("/books")
async def create_book(book: Book):
    return {"message": "creating book - placeholder"}


@app.put("/books/{id}")
async def update_book(id: int, book: Book):
    return {"message": "updating book - placeholder"}


@app.delete("/books/{id}")
async def delete_book(id: int):
    return {"message": "deleting a book - placeholder"}
