from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

db_book = []


# ------------------------------
# 📦 Pydantic моделі
# ------------------------------

class Base(BaseModel):
    name: str
    price: int


class Book(Base):
    id: int


class CreateBook(Base):
    pass


class PatchBook(Base):
    name: Optional[str] = None
    price: Optional[int] = None


# ------------------------------
# 🔧 Утиліта: генерація ID
# ------------------------------

def lenth_db():
    return len(db_book) + 1


# ------------------------------
# 📤 GET — отримати всі книги
# ------------------------------

@app.get("/book", response_model=List[Book])
def get_books():
    return db_book


# ------------------------------
# 📥 POST — створити нову книгу
# ------------------------------

@app.post("/book", response_model=Book)
def create_book(book: CreateBook) -> Book:
    new_book = Book(
        id=lenth_db(),
        name=book.name,
        price=book.price
    )
    db_book.append(new_book)
    return new_book


# ------------------------------
# 🔄 PATCH — часткове оновлення книги
# ------------------------------

@app.patch("/book/{book_id}", response_model=Book)
def patch_book(book_id: int, updated_book: PatchBook) -> Book:
    book = next((b for b in db_book if b.id == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    book.name = updated_book.name or book.name  # Заміна, якщо є нове значення
    book.price = updated_book.price or book.price  # Заміна, якщо є нове значення

    return book


# ------------------------------
# 🛠 PUT — повне оновлення книги
# ------------------------------

@app.put("/book/{book_id}", response_model=Book)
def put_book(book_id: int, updated_book: CreateBook) -> Book:
    book = next((b for b in db_book if b.id == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    book.name = updated_book.name
    book.price = updated_book.price

    return book


# ------------------------------
# ❌ DELETE — видалити книгу
# ------------------------------

@app.delete("/book/{book_id}")
def delete_book(book_id: int):
    book = next((b for b in db_book if b.id == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    db_book.remove(book)  # Тепер правильно видаляємо об'єкт книги

    return {"message": f"Book with id {book_id} has been deleted."}
