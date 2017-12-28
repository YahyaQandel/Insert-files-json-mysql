from classes.config import Configuration_Handler
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import Sequence
from sqlalchemy.sql import func
import datetime
import time

Base = declarative_base()
database_name = Configuration_Handler.get('DataDB', 'name')
column_length = Configuration_Handler.get('DataDB', 'col_length')

class Laws(Base):
	__tablename__ = 'laws'
	id = Column(Integer, primary_key=True)
	url = Column(String(column_length, convert_unicode=True), nullable=False)
	header = Column(String(column_length, convert_unicode=True), nullable=False)
	lawType = Column(String(column_length, convert_unicode=True), nullable=False)
	number = Column(Integer, nullable=False)
	title = Column(String(column_length, convert_unicode=True), nullable=False)
	year = Column(String(column_length, convert_unicode=True), nullable=False)
	legalStatus = Column(String(column_length, convert_unicode=True), nullable=False)
	noPages = Column(Integer, nullable=False)
	journal = Column(String(column_length, convert_unicode=True), nullable=False)
	journalNo = Column(Integer, nullable=False)
	issueType = Column(String(column_length, convert_unicode=True), nullable=False)
	issueDate = Column(DateTime(timezone=True), nullable=False)
	startDate = Column(DateTime(timezone=True), nullable=False)
	endDate = Column(DateTime(timezone=True))

