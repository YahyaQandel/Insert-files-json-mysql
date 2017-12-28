from classes.config import Configuration_Handler
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import Sequence

Base = declarative_base()
cnfHndl = Configuration_Handler()

database_name = cnfHndl.get('DataDB', 'name')
column_length = cnfHndl.get('DataDB', 'col_length')

class law_txt_files(Base):
	__tablename__ = 'law_txt_files'
	id = Column(Integer, primary_key=True)
	filename = Column(String(column_length, convert_unicode=True), nullable=False)
	status = Column(String(column_length, convert_unicode=True), nullable=False)
	created_at = Column(DateTime, default=datetime.datetime.utcnow)