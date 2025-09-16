import psycopg2


class DataBase:
    def __init__(self):
        self.DATABASE_URL = "postgresql://magazinedata_user:vNqcYD74Yh1HcepJcgQMnBMFLiZ0R5d9@dpg-d2o7m06uk2gs73ajlft0-a/magazinedata"

    def execute(self, query, params=None, fetch=False, commit=False):
        with psycopg2.connect(self.DATABASE_URL, sslmode="require") as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                if commit:
                    conn.commit()
                if fetch:
                    return cur.fetchall()
