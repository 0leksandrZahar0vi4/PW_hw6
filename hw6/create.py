import logging
from psycopg2 import DatabaseError

from connect import create_connection


def create_table(conn, sql_expression: str):
    """ create a table from the create_table_sql statement
    :param sql_expression:
    :param conn: Connection object
    :return:
    """
    c = conn.cursor()
    try:
        c.execute(sql_expression)
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()


if __name__ == '__main__':
    sql_create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(120),
    email VARCHAR(120),
    age smallint CHECK(age > 18 AND age < 60) 
    );
    """
    sql_create_users_groups = """
    CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    users_id INTEGER REFERENCES users(id)
    on delete cascade
    );"""

    sql_create_users_subjects = """
    CREATE TABLE subjects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(175) NOT NULL,
    teacher_id INTEGER  REFERENCES teachers(id)
    on delete cascade
    );"""
    
    sql_create_users_teachers = """
    CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(150) NOT NULL
    );"""
    
    sql_create_users_grades = """
    CREATE TABLE grades (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES users(id) on delete cascade,
    subject_id INTEGER REFERENCES subjects(id) on delete cascade,
    grade INTEGER CHECK (grade >= 60 AND grade <= 100),
    grade_date DATE NOT NULL
    );"""
    
    try:
        with create_connection() as conn:
            if conn is not None:
                create_table(conn, sql_create_users_table)
                create_table(conn, sql_create_users_groups)
                create_table(conn, sql_create_users_subjects)
                create_table(conn, sql_create_users_teachers)
                create_table(conn, sql_create_users_grades)
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)