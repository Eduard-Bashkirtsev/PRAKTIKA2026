from app.db.db import Base, engine, SessionLocal
from app.db.models import Category
from app.db.crud import create_category, create_book

# Создание таблиц
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Создание категорий
fiction = create_category(db, "Художественная литература")
programming = create_category(db, "Программирование")

# Добавление книг
create_book(
    db,
    "Война и мир",
    "Роман Л. Н. Толстого",
    1200,
    "",
    fiction
)

create_book(
    db,
    "Преступление и наказание",
    "Роман Ф. М. Достоевского",
    950,
    "",
    fiction
)

create_book(
    db,
    "Изучаем Python",
    "Учебник по Python",
    1800,
    "",
    programming
)

create_book(
    db,
    "SQL для начинающих",
    "Основы SQL",
    1500,
    "",
    programming
)

db.close()

print("База данных успешно заполнена.")
