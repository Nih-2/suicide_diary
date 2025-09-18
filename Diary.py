# import sqlite3
from datetime import datetime, timedelta
# from DataBase import DataBase
from zoneinfo import ZoneInfo


class Diary:
    def __init__(self, db):
        self.db = db
        
        self.notes_list = []
        self.day_rating = 0
        self.week_rating = 0
        self.month_rating = 0

        self.first()
        self.auto_run()
        self.count_rating()

        # self.add_note(react=+1, note='пишеться')


    def first(self):
        self.db.execute("""CREATE TABLE IF NOT EXISTS notes (    
                id SERIAL PRIMARY KEY,
                date TEXT NOT NULL,
                react INTEGER NOT NULL,
                note TEXT
                )""",
                commit=True
        )

        
        # with sqlite3.connect("diary_data.db") as data_base:
            # data_base.execute("PRAGMA foreign_keys = ON")
          #  cursor = data_base.cursor()

           # cursor.execute("""
            #    CREATE TABLE IF NOT EXISTS notes (
             #   id INTEGER PRIMARY KEY AUTOINCREMENT,
              #  date TEXT NOT NULL,
               # react INTEGER NOT NULL,
                #note TEXT
                #)"""
            #)
            #data_base.commit()


    def auto_run(self):
        #with sqlite3.connect("diary_data.db") as data_base:
            #cursor = data_base.cursor()

            # cursor.execute("SELECT * FROM notes")
        notes = self.db.execute("SELECT * FROM notes", fetch=True)
            
            # cursor.fetchall()
        for note in notes:
            id = note[0]
            date = datetime.strptime(note[1], "%d.%m.%Y %H:%M")
            react = note[2]
            note = note[3]

            self.notes_list.append([id, date, react, note])


    def add_note(self, react, note):
        date = datetime.now(ZoneInfo("Europe/Kyiv"))

        #with sqlite3.connect("diary_data.db") as data_base:
            #cursor = data_base.cursor()

            #self.db.execute("INSERT INTO notes (date, react, note) VALUES(%s, %s, %s)",
            #    (date.strftime("%d.%m.%Y %H:%M"), react, note), commit=True
            #)
            # data_base.commit()

        # ID вставленого рядка
        result  = self.db.execute("""
            INSERT INTO notes (date, react, note)
            VALUES (%s, %s, %s)
            RETURNING id
        """, (date.strftime("%d.%m.%Y %H:%M"), react, note), commit=True, fetch=True)

        id = result[0][0]  # self.db.fetchone()[0]
        
        
            # id = cursor.lastrowid

        self.notes_list.append([id, date, react, note])


    def delete_note(self, id):
        #with sqlite3.connect("diary_data.db") as data_base:
        #    cursor = data_base.cursor()

        self.db.execute("DELETE FROM notes WHERE id = %s", (id,), commit=True,)
            # data_base.commit()


    def count_rating(self):
        self.day_rating = 0
        self.week_rating = 0
        self.month_rating = 0

        today = datetime.now()

        for note in self.notes_list:
            if note[1].day == today.day:
                self.day_rating += note[2]

        for note in self.notes_list:
            week_start = today - timedelta(days=today.weekday())  # понеділок поточного тижня
            week_end = week_start + timedelta(days=6)

            if week_start.date() <= note[1].date() <= week_end.date():
                self.week_rating += note[2]

        #for note in self.notes_list:
            #if note[1] <= (today + timedelta(days=7)) and note[1].weekday() <= today.weekday():
                #self.week_rating += note[2]

        for note in self.notes_list:
            if note[1].month == today.month:

                self.month_rating += note[2]

