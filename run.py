# #!/usr/bin/env python
import ConfigParser
from classes.law import Law
from classes.datareader import DataFile
import json
import logging

config = ConfigParser.ConfigParser()
config.read('Configuration.cfg')
folder_path = config.get('DATA_FILES', 'folder_path')
logging.basicConfig(filename='logname',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

datar = DataFile(folder_path)
files =  datar.directory_files_list()

law = Law()
module_logger = logging.getLogger('json_script_to_mysql.main')
for law_file_name in files:
	try:
		law_file_json = datar.read(law_file_name)
		law.set_attributes(law_file_json)
		new_law_obj = law.save()
	except Exception as e:
		print 'Invalid Json File[%s]'%(law_file_name)



