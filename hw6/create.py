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
    CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    group_id INTEGER REFERENCES groups(id) on delete cascade
    );
    """
    sql_create_groups = """
    CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
    );"""

    sql_create_subjects = """
    CREATE TABLE subjects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(175) NOT NULL,
    teacher_id INTEGER REFERENCES teachers(teacher_id) on delete cascade
    );"""
    
    sql_create_teachers = """
    CREATE TABLE teachers (
    teacher_id SERIAL PRIMARY KEY,
    fullname VARCHAR(150) NOT NULL
    );"""
    
    sql_create_grades = """
    CREATE TABLE grades (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(id) on delete cascade,
    subject_id INTEGER REFERENCES subjects(id) on delete cascade,
    grade INTEGER CHECK (grade >= 60 AND grade <= 100),
    grade_date DATE NOT NULL
    );"""
    
    try:
        with create_connection() as conn:
            if conn is not None:
                create_table(conn, sql_create_users_table)
                create_table(conn, sql_create_groups)
                create_table(conn, sql_create_subjects)
                create_table(conn, sql_create_teachers)
                create_table(conn, sql_create_grades)
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)