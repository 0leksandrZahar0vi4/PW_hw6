import logging

from faker import Faker
import random
import psycopg2
from psycopg2 import DatabaseError

fake = Faker('uk_UA')

# Підключення до бази даних
conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="1")
cur = conn.cursor()

# Додавання груп
for _ in range(3):
    cur.execute("INSERT INTO groups (name) VALUES (%s)", (fake.word(),))

# Додавання викладачів
for _ in range(3):
    cur.execute("INSERT INTO teachers (fullname) VALUES (%s)", (fake.name(),))

# Додавання предметів із вказівкою викладача
for teacher_id in range(1, 4):
    for _ in range(2):
        cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (%s, %s)", (fake.word(), teacher_id))

# Додавання студентів і оцінок
for group_id in range(1, 4):
    for _ in range(10):
        cur.execute("INSERT INTO users (name, email, age, group_id) VALUES (%s, %s, %s, %s) RETURNING id",
                    (fake.name(), fake.email(), random.randint(18, 60), group_id))
users_id = cur.fetchone()[0]
for subjects_id in range(1, 3):
    for _ in range(10):
        cur.execute("INSERT INTO grades (user_id, subjects_id, grade, grade_date) VALUES (%s, %s, %s, %s)",
                    (users_id, subjects_id, random.randint(60, 100), fake.date()))

try:
    # Збереження змін
    conn.commit()
except DatabaseError as e:
    logging.error(e)
    conn.rollback()
finally:
    # Закриття підключення
    cur.close()
    conn.close()