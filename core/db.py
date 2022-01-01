from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
from sqlalchemy import event

SQLALCHEMY_DATABASE_URL = "sqlite:///./app.core.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> SessionLocal:
    """
    Get db to create session
    :return Session:
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# Todo Logging
@event.listens_for(Engine, "before_execute")
def my_before_execute(
        conn, clauseelement, multiparams, params, execution_options
):
    print("before execute!")

@event.listens_for(Engine, "after_execute")
def my_before_execute(
        conn, clauseelement, multiparams, params, execution_options
):
    print("after execute!")

