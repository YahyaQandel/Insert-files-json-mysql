# #!/usr/bin/env python
from classes.law import Law
from classes.config import Configuration_Handler
from classes.datareader import DataFile
import json
import logging
import datetime
import os

class JSONScript:

	def __init__(self):
		# class attributes
		self.__folder_path = Configuration_Handler.get('DATA_FILES', 'folder_path')
		self.__logger = None
		self.__datareaderObj = DataFile(self.__folder_path)
		self.__lawObj =Law()


	def run(self):
		self.__initiateLogger()
		self.__fetchDataFolder()


	def __fetchDataFolder(self):
		# Data files configuration
		processed_file_ext = Configuration_Handler.get('DATA_FILES', 'processed_file_ext')
		files =  self.__datareaderObj.directory_files_list()
		for law_file_name in files:
			try:
				law_file_json = self.__datareaderObj.read(law_file_name)
				if self.__saveFileJson(law_file_name,law_file_json):
					self.__datareaderObj.rename(processed_file_ext)
					self.__datareaderObj.cp_modified_law_files(law_file_name,self.__lawObj.get_attributes())
			except Exception as e:
				logger_string = 'File [%s] Error :[%s]'%(law_file_name,str(e))
				self.__logger.info(logger_string)


	def __saveFileJson(self,filename,json):
		self.__lawObj.set_attributes(json,filename)
		if self.__lawObj.check_law_file_already_inserted(filename):
			logger_string = 'File[%s] already inserted before !'%(filename)
			self.__logger.info(logger_string)
			return False
		else:
			self.__lawObj.save()
			self.__lawObj.save_law_file(filename)
			return True


	def __initiateLogger(self):

		# Logging configuration
		logger_cls = Configuration_Handler.get('Logging', 'logger_instance_name')
		log_folder = Configuration_Handler.get('Logging', 'log_folder')


		logname = datetime.datetime.now().strftime("%Y-%m-%d")
		if not os.path.exists(log_folder):
		    os.makedirs(log_folder)
		logname = '%s/%s'%(log_folder,logname)
		logging.basicConfig(filename=logname,
		                            filemode='a',
		                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
		                            datefmt='%H:%M:%S',
		                            level=logging.DEBUG)

		self.__logger = logging.getLogger(logger_cls)