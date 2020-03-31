from pathlib import Path
THIS_DIR = Path(__file__).absolute.parent

SQLITE_PATH = THIS_DIR.parent.parent / 'db/data' / 'web_app.db'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(SQLITE_PATH)