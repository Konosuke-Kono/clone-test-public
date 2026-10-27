"""SQLite storage for the book catalog."""
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name('books.sqlite3')


def connect():
    return sqlite3.connect(DB_PATH)


def initialize():
    with connect() as db:
        db.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT)')
        db.executemany('INSERT OR IGNORE INTO books VALUES (?, ?, ?)', [
            (1, 'Python Basics', 'A. Writer'),
            (2, 'Data Systems', 'B. Writer'),
            (3, 'Web Development', 'C. Writer'),
        ])
