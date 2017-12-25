# from peewee import *
import ConfigParser
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import Sequence


Base = declarative_base()
config = ConfigParser.ConfigParser()
config.read('Configuration.cfg')
database_name = config.get('DataDB', 'name')
column_length = config.get('DataDB', 'col_length')

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
	issueDate = Column(String(column_length, convert_unicode=True), nullable=False)
	startDate = Column(String(column_length, convert_unicode=True), nullable=False)
	endDate = Column(String(column_length, convert_unicode=True), nullable=False)

