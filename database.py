import sqlite3

class Database:
    def __init__(self, db_name="mahasiswa.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS mahasiswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nim TEXT NOT NULL,
            nama TEXT NOT NULL,
            prodi TEXT NOT NULL,
            angkatan INTEGER NOT NULL
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetch_all(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
