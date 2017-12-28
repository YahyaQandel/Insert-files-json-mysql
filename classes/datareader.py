import json
import os
from os import listdir
from os.path import isfile, join
import logging
from classes.config import Configuration_Handler
from bson import json_util
class DataFile():

    def __init__(self,folderpath):
        logger_cls = '%s.%s'%(Configuration_Handler.get('Logging', 'logger_instance_name'),self.__class__.__name__)
        self.__cp_law_files_directory = Configuration_Handler.get('DATA_FILES', 'copied_files_directory_name')
        self.__logger = logging.getLogger(logger_cls)
        self.__file_ext = Configuration_Handler.get('DATA_FILES', 'default_file_ext')
        self.__file_path = None
        self.__file_name = None
        self.__folder_files = None
        self.__folderpath = folderpath
    def read(self,file_name):
        if file_name:
            try:
                file_path = '%s/%s'%(self.__folderpath,file_name)
                data = json.load(open(file_path))
                logger_string = 'File [%s] read successfully '%(file_name)
                self.__logger.info(logger_string)
                self.__file_path = file_path
                self.__file_name = file_name
                return data
            except Exception as e:
                raise Exception(e.message)


    def directory_files_list(self):
        if  self.__folderpath and os.path.exists(self.__folderpath):
            self.__folder_files = [f for f in listdir(self.__folderpath) if isfile(join(self.__folderpath, f)) and f.endswith(self.__file_ext)]
            if len(self.__folder_files) == 0:
                logger_string = 'There are no .txt files to be processed !'
                self.__logger.info(logger_string)
                return []
            else:
                return self.__folder_files
        else:
            self.__folder_files = []
            self.__logger.info('Folder [%s] not exists !'%(self.__folderpath))


    def rename(self,new_file_ext):
        file_name_without_ext = self.__file_name.split('.')[0];
        new_file_name = '%s/%s%s'%(self.__folderpath,file_name_without_ext,new_file_ext)
        os.rename(self.__file_path,new_file_name)
        logger_string = 'File[%s] status swtiched to PROCESSED !'%(self.__file_name)
        self.__logger.info(logger_string)


    def cp_modified_law_files(self,filename,json_law_data):
        # try:
        if not self.__cp_law_files_directory or not os.path.exists(self.__cp_law_files_directory):
            os.makedirs(self.__cp_law_files_directory)
        cp_file_path = '%s/%s'%(self.__cp_law_files_directory,filename)
        print cp_file_path
        cp_file = open(cp_file_path,"w")
        cp_file.write(json.dumps(json_law_data,default=str))
        return True
        # except Exception as e:
        #     self.__logger.info(str(e))
        #     return False


