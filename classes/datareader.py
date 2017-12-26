import json
import os
from os import listdir
from os.path import isfile, join
import logging
from classes.config import Configuration_Handler

class DataFile():

    def __init__(self,folderpath):
        logger_cls = '%s.%s'%(Configuration_Handler.get('Logging', 'logger_instance_name'),self.__class__.__name__)
        self.logger = logging.getLogger(logger_cls)
        self.file_ext = Configuration_Handler.get('DATA_FILES', 'default_file_ext')
        self.file_path = None
        self.file_name = None
        self.folder_files = None
        self.folderpath = folderpath
    def read(self,file_name):
        if file_name:
            try:
                file_path = '%s/%s'%(self.folderpath,file_name)
                data = json.load(open(file_path))
                logger_string = 'File [%s] read successfully '%(file_name)
                self.logger.info(logger_string)
                self.file_path = file_path
                self.file_name = file_name
                return data
            except Exception as e:
                raise Exception(e.message)


    def directory_files_list(self):
        if  self.folderpath and os.path.exists(self.folderpath):
            self.folder_files = [f for f in listdir(self.folderpath) if isfile(join(self.folderpath, f)) and f.endswith(self.file_ext)]
            if len(self.folder_files) == 0:
                logger_string = 'There are no .txt files to be processed !'
                self.logger.info(logger_string)
                return []
            else:
                return self.folder_files
        else:
            self.folder_files = []
            self.logger.info('Folder [%s] not exists !'%(folderpath))


    def rename(self,new_file_ext):
        file_name_without_ext = self.file_name.split('.')[0];
        new_file_name = '%s/%s%s'%(self.folderpath,file_name_without_ext,new_file_ext)
        os.rename(self.file_path,new_file_name)
        logger_string = 'File[%s] status swtiched to PROCESSED !'%(self.file_name)
        self.logger.info(logger_string)


