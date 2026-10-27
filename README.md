# Book Catalog Search API

A small Python application that provides an HTTP endpoint for searching a local SQLite catalog.

## Files

- `app.py`: HTTP request handling and catalog search
- `database.py`: SQLite initialization and connection
- `.gitignore`: local generated files excluded from version control

## Requirements

Python 3.10 or later. No third-party Python packages are required.

## Local use

From the project directory:

```bash
python app.py
```

Then, from another terminal:

```bash
curl 'http://127.0.0.1:8766/books?q=Python'
```

The application binds to `127.0.0.1:8766` and creates `books.sqlite3` at startup. The database file is excluded from version control.

This repository is intended for local development and testing; do not expose the application as an internet-facing service.
