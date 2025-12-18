from sqlalchemy.orm import Session
import models
import schemas

# Create new book
def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(
        title=book.title,
        author=book.author,
        year=book.year
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Get all books
def get_books(db: Session):
    return db.query(models.Book).all()

# Delete book
def delete_book(db: Session, book_id: int):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
    return book

# Update book
def update_book(db: Session, book_id: int, book_data: schemas.BookUpdate):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        return None
    book.title = book_data.title
    book.author = book_data.author
    book.year = book_data.year
    db.commit()
    db.refresh(book)
    return book

# Search books
def search_books(db: Session, query: str):
    return db.query(models.Book).filter(
        models.Book.title.contains(query) |
        models.Book.author.contains(query)
    ).all()
