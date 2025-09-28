# import psycopg2

#
# class DataBase:
#     def __init__(self):
#         self.DATABASE_URL = "postgresql://magazinedata_user:vNqcYD74Yh1HcepJcgQMnBMFLiZ0R5d9@dpg-d2o7m06uk2gs73ajlft0-a/magazinedata"
#
#     def execute(self, query, params=None, fetch=False, commit=False):
#         with psycopg2.connect(self.DATABASE_URL, sslmode="require") as conn:
#             with conn.cursor() as cur:
#                 cur.execute(query, params)
#                 if commit:
#                     conn.commit()
#                 if fetch:
#                     return cur.fetchall()


import psycopg2
from psycopg2 import OperationalError, sql

class DataBase:
    def __init__(self):
        # ВСТАВ повний URL або параметри з панелі хостингу
        self.db_params = {
            "dbname": "diary_i1k9",
            "user": "diary_i1k9_user",
            "password": "XMnaLQXKeNsSDxph8AuzFpVBbqOQZkMl",
            "host": "dpg-d3cfbsili9vc73dh0kgg-a.oregon-postgres.render.com",  # приклад для Render
            "port": 5432,
            "sslmode": "require"
        }

    def execute(self, query, params=None, fetch=False, commit=False):
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cur:
                    cur.execute(query, params)

                    if commit:
                        conn.commit()

                    if fetch:
                        return cur.fetchall()

        except OperationalError as e:
            print("❌ Помилка підключення до БД:", e)
        except Exception as e:
            print("❌ Помилка виконання запиту:", e)
