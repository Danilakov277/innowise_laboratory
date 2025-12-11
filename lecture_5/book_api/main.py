from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
import crud
from database import engine
from dependencies import get_db

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book Collection API")

# Add book
@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

# List all books
@app.get("/books/", response_model=list[schemas.Book])
def get_books(db: Session = Depends(get_db)):
    return crud.get_books(db)

# Delete book
@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    result = crud.delete_book(db, book_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Deleted"}

# Update book
@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    updated = crud.update_book(db, book_id, book)
    if updated is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated

# Search
@app.get("/books/search/", response_model=list[schemas.Book])
def search_books(query: str, db: Session = Depends(get_db)):
    return crud.search_books(db, query)
