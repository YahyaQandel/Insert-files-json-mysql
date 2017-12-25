import ConfigParser
import logging

class Configuration_Handler:

	__config = None
	__logger_cls = None
	__logger = None
	@staticmethod
	def get(section,key):

		if Configuration_Handler.__config == None:
			Configuration_Handler()
		return Configuration_Handler.__config.get(section, key)


	def __init__(self):
		if Configuration_Handler.__config != None:
			Configuration_Handler.__logger.info('Instance already initialized before')
		else:
			Configuration_Handler.__config = ConfigParser.ConfigParser()
			Configuration_Handler.__config.read('classes/cfg/Configuration.cfg')
			Configuration_Handler.__logger_cls = '%s.%s'%(Configuration_Handler.get('Logging', 'logger_instance_name'),self.__class__.__name__)
			Configuration_Handler.__logger = logging.getLogger(Configuration_Handler.__logger_cls)