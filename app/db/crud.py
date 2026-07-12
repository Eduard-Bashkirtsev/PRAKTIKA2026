from app.db.models import Category, Book

# Categories
def create_category(db, title):
    category = Category(title=title)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def get_categories(db):
    return db.query(Category).all()

# Books
def create_book(db, title, description, price, url, category):
    book = Book(
        title=title,
        description=description,
        price=price,
        url=url,
        category=category
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_books(db):
    return db.query(Book).all()

def update_book_price(db, book_id, new_price):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        book.price = new_price
        db.commit()

def delete_book(db, book_id):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
