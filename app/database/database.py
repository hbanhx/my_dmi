from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

'''
https://docs.sqlalchemy.org/en/21/orm/quickstart.html

The Engine is a factory that can create new database connections for us, which also holds onto connections inside of a Connection Pool for fast reuse

The sessionmaker factory generates new Session objects when called, creating them given the configurational arguments established here.

https://docs.sqlalchemy.org/en/21/orm/session_api.html#sqlalchemy.orm.sessionmaker
'''

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:1234@localhost:5433/dmi_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
# Declarative_base = sqlalchemy syntax for ORM setup og shared base engine, session, models og schemas
Base = declarative_base()

def get_db():

    try:
        db = SessionLocal() # Create db session
        yield db  # Provide it to the request
    except Exception as e:
        print("Database error:", e)
        raise
    finally:
        db.close() 