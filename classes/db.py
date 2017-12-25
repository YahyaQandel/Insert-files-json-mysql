
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import Sequence
from sqlalchemy.orm import sessionmaker
from classes.config import Configuration_Handler

class DBConnection:
    class DBClient:
        def __init__(self):
			Base = declarative_base()
			cnfHndl = Configuration_Handler()
			database_name = cnfHndl.get('DataDB', 'name')
			username = cnfHndl.get('DataDB', 'username')
			password = cnfHndl.get('DataDB', 'password')
			dbconnectionstring = 'mysql+pymysql://%s:%s@localhost/%s?charset=utf8'%(username,password,database_name)
			engine = create_engine(dbconnectionstring)
			Base.metadata.create_all(engine)
			Session = sessionmaker(bind=engine)
			self.session = Session()

    session = None

    def __init__(self):
        if not DBConnection.session:
            DBConnection.session = DBConnection.DBClient().session

