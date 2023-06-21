from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from configs import db_user, db_password, db_host, db_name
from models.base import Base


engine = create_engine(f"mysql://{db_user}:{db_password}@{db_host}/{db_name}")
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models
    Base.metadata.create_all(bind=engine)
