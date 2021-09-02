import sqlite3
import datetime

class manager:

    def __init__(self):
        connection = sqlite3.connect("bookmarks.db") 

        with connection:
            db_cursor = connection.cursor()
            db_cursor.execute("""CREATE TABLE IF NOT EXISTS bookmarks (url TEXT UNIQUE, date TEXT)""")

    def update(self, url):
        connection = sqlite3.connect("bookmarks.db") 

        with connection:
            db_cursor = connection.cursor()

            try:
                date = datetime.date.today().strftime("%Y-%m-%d") # YYYY-MM-DD
                db_cursor.execute("""INSERT INTO bookmarks VALUES (?, ?)""", (url, date))

            except:
                pass

    def search(self, year, month=None, day=None, count=5):
        connection = sqlite3.connect("bookmarks.db") 

        with connection:
            db_cursor = connection.cursor()
            date = f"{year}-{month or '__'}-{day or '__'}"

            print(date)

            try:
                db_cursor.execute("""SELECT url FROM bookmarks WHERE date LIKE ? ORDER BY rowid DESC LIMIT ?""", (date, count))
            except:
                pass

        return db_cursor.fetchall()
                    
if __name__ == "__main__":

    mymanager = manager()

    mymanager.update(url="https://github.com/er-knight/mybookmarks")

    bookmarks = mymanager.search(
        year=datetime.date.today().strftime("%Y"), 
        month=datetime.date.today().strftime("%m")
    )

    for url in bookmarks:
        print(url)