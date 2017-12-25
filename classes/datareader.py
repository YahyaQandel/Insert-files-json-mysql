import json
import os
from os import listdir
from os.path import isfile, join

class DataFile():

    def __init__(self,folderpath):
        if  folderpath and os.path.exists(folderpath):
            self.folder_files = [f for f in listdir(folderpath) if isfile(join(folderpath, f))]
            self.folderpath = folderpath
        else:
            self.folder_files = []
        
        

    def read(self):
        try:
            if len(self.folder_files)>0:
                for txt_file in self.folder_files:
                    file_path = '%s/%s'%(self.folderpath,txt_file)
                    data = json.load(open(file_path))
                    return data
            else:
                raise Exception('Folder has no valid files!')
        except Exception as e:
                raise Exception(e.message)
