from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.models import Base
from config import DB_HOST, DB_NAME, DB_PASS, DB_USER

DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'
engine = create_engine(DATABASE_URL,future=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
