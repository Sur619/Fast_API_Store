from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()
books_bd = []


def autogenerate_id():
    return len(books_bd) + 1


# 📦 Базова модель (спільна логіка)
class BookBase(BaseModel):
    title: str
    author: Optional[str] = None
    price: Optional[int] = None


# 📥 Модель для створення (без ID)
class CreateBook(BookBase):
    pass


# 📤 Модель відповіді (з ID)
class Book(BookBase):
    id: int


@app.post("/add", response_model=Book)
def create_book(book: CreateBook):
    new_book = {
        "id": autogenerate_id(),
        "title": book.title,
        "author": book.author,  # ✅ правильно
        "price": book.price
    }
    books_bd.append(new_book)
    return new_book  # FastAPI сам застосує response_model=Book


@app.get("/", response_model=List[Book])
def get_books():
    return books_bd
