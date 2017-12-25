import json
import os
from os import listdir
from os.path import isfile, join
import logging
from classes.config import Configuration_Handler

class DataFile():

    def __init__(self,folderpath):
        if  folderpath and os.path.exists(folderpath):
            self.folder_files = [f for f in listdir(folderpath) if isfile(join(folderpath, f))]
            self.folderpath = folderpath
        else:
            self.folder_files = []

        logger_cls = '%s.%s'%(Configuration_Handler.get('Logging', 'logger_instance_name'),self.__class__.__name__)
        self.logger = logging.getLogger(logger_cls)


    def read(self,file_name):
        try:
            file_path = '%s/%s'%(self.folderpath,file_name)
            data = json.load(open(file_path))
            logger_string = 'File [%s] read successfully '%(file_name)
            self.logger.info(logger_string)
            return data
        except Exception as e:
            logger_string = 'File [%s] Error : %s'%(file_name,e.message)
            self.logger.info(logger_string)
            raise Exception(e.message)


    def directory_files_list(self):
        if self.folder_files >0:
            return self.folder_files
        else:
            self.logger.info('Folder has no valid files!')
            raise Exception('Folder has no valid files!')