import sqlite3

class BoardDB:
    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS board (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT)''')
        self.conn.commit()

    def get_all_boards(self):
        self.c.execute("SELECT * FROM board")
        rows = self.c.fetchall()
        return rows

    def get_board_by_id(self, board_id):
        self.c.execute("SELECT * FROM board WHERE id=?", (board_id,))
        row = self.c.fetchone()
        return row

    def insert_board(self, title, content):
        self.c.execute("INSERT INTO board (title, content) VALUES (?, ?)", (title, content))
        self.conn.commit()
        return self.c.lastrowid

    def close(self):
        self.conn.close()