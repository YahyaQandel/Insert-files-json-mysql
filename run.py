# #!/usr/bin/env python
from classes.law import Law
from classes.config import Configuration_Handler
from classes.datareader import DataFile
import json
import logging
import datetime

logname = datetime.datetime.now().strftime("%Y-%m-%d")
logname = 'logs/%s'%(logname)
logging.basicConfig(filename=logname,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)



cnfHndl = Configuration_Handler()
logger_cls = Configuration_Handler.get('Logging', 'logger_instance_name')
folder_path = Configuration_Handler.get('DATA_FILES', 'folder_path')



datar = DataFile(folder_path)
files =  datar.directory_files_list()

law = Law()
logger = logging.getLogger(logger_cls)
for law_file_name in files:
	try:
		law_file_json = datar.read(law_file_name)
		law.set_attributes(law_file_json)
		new_law_obj = law.save()
	except Exception as e:
		logger_string = 'Invalid Json File[%s]'%(law_file_name)
		logger.info(logger_string)



