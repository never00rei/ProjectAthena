#coding: UTF-8

"""
Project Athena database adapter...
"""

from sqlalchemy  import create_engine
from sqlalchemy.orm import relationship, scoped_session, sessionmaker

from ..db_adapter.db_setup import setup

db_url = setup()

databaseEngine = create_engine(db_url, echo=True,
                               convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=databaseEngine))
