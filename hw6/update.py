import logging
from random import randint
from main import group_id, users_id, subjects_id, teacher_id
from faker import Faker
from psycopg2 import DatabaseError

from connect import create_connection


fake = Faker('uk-Ua')
COUNT = 100


def update_users(conn, sql_expression: str):
    c = conn.cursor()
    try:
        for i in range(31, 131):
            c.execute(sql_expression, group_id, i + 1)
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()


if __name__ == '__main__':
    sql_expression_update = """
        UPDATE users SET group_id = %s WHERE id = %s;
        """

    try:
        with create_connection() as conn:
            if conn is not None:
                update_users(conn, sql_expression_update)
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)