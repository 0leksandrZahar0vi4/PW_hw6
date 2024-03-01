import logging
from random import randint

from faker import Faker
from psycopg2 import DatabaseError

from connect import create_connection


fake = Faker('uk_UA')
COUNT = 100

def insert_users(conn, sql_expression: str):
    c = conn.cursor()
    try:
        for _ in range(COUNT):
            c.execute(sql_expression, (fake.name(), fake.email(), randint(19, 61)))
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()

def insert_groups(conn, sql_expression: str):
    c = conn.cursor()
    try:
        for _ in range(3):
            c.execute(sql_expression, (fake.word(),))
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()

def insert_subjects(conn, sql_expression: str):
    c = conn.cursor()
    try:
        for _ in range(8):
            c.execute(sql_expression, (fake.word(),))
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()
        
def insert_teachers(conn, sql_expression: str):
    c = conn.cursor()
    try:
        for _ in range(5):
            c.execute(sql_expression, (fake.name(),))
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()
        
def insert_grades(conn, sql_expression: str):
    c = conn.cursor()
    try:
        for _ in range(800):
            c.execute(sql_expression, (randint(60,101), fake.date()))
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()
        
if __name__ == '__main__':
    sql_insert_users = """
        INSERT INTO users (name, email, age) VALUES (%s, %s, %s);
        """
    sql_insert_groups = """
        INSERT INTO groups (name) VALUES (%s);
        """
    sql_insert_subjects = """
        INSERT INTO subjects (name) VALUES (%s);
        """
    sql_insert_teachers = """
        INSERT INTO teachers (fullname) VALUES (%s);
        """
    sql_insert_grades = """
        INSERT INTO grades (grade, grade_date) VALUES (%s, %s);
        """

    try:
        with create_connection() as conn:
            if conn is not None:
                insert_users(conn, sql_insert_users)
                insert_groups(conn, sql_insert_groups)
                insert_subjects(conn, sql_insert_subjects)
                insert_teachers(conn, sql_insert_teachers)
                insert_grades(conn, sql_insert_grades)
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)