import requests
import json
from models.law import Laws
from models.lawTxtFile import law_txt_files
import ast
from classes.config import Configuration_Handler
from classes.db import DBConnection
import enum 
import logging
from datetime import date
# encoding=utf8  
import sys  
class Law():
    def __init__(self, args=None):
        if args:
            self.__args = args
        self.__session = DBConnection().session
        self.__months_format = Configuration_Handler.get('LAW_ATTRIBUTES_SETTINGS', 'months')
        self.__months__alternatives_format = Configuration_Handler.get('LAW_ATTRIBUTES_SETTINGS', 'months_alternatives')
        logger_cls = '%s.%s'%(Configuration_Handler.get('Logging', 'logger_instance_name'),self.__class__.__name__)
        self.__logger = logging.getLogger(logger_cls)

    def set_attributes(self,args,filename):
        self.__args = args
        self.__args['id'] = filename.split('.')[0]
        self.__args['issueDate'] = self.__reformat_date(self.__args['issueDate']);
        self.__args['startDate'] = self.__reformat_date(self.__args['startDate']);
        self.__args['endDate'] = self.__reformat_date(self.__args['endDate']);

    def save(self):
        try:
            self.__args = self.__encode_parameters(self.__args)
            new_law = Laws(id=self.__args['id'],
                        url=self.__args['url'],
                        header=self.__args['header'],
                        lawType=self.__args['lawType'],
                        number=self.__args['number'],
                        title=self.__args['title'],
                        year=self.__args['year'],
                        legalStatus=self.__args['legalStatus'],
                        noPages=self.__args['noPages'],
                        journal=self.__args['journal'],
                        journalNo=self.__args['journalNo'],
                        issueType=self.__args['issueType'],
                        issueDate=self.__args['issueDate'],
                        startDate=self.__args['startDate'],
                        endDate=self.__args['endDate']
                    )
            self.__session.add(new_law)
            self.__session.commit()
            self.__session.flush()
            self.__session.close()
            law_obj = self.__session.query(Laws).filter_by(number=self.__args['number']).first()
            if law_obj:
                logger_string = 'law number [%s] fetched successfully '%(self.__args['number'])
                self.__logger.info(logger_string)
                return True
            return True

        except Exception as e:
            self.__logger.info(str(e))
            print str(e)

    def __encode_parameters(self,args):
        reload(sys)  
        sys.setdefaultencoding('utf8')
        for key,value in args.items():
            if isinstance(value,basestring):
                args[key] = value.encode('utf-8')

        return args

    def check_law_file_already_inserted(self,filename):
        query_rows_count = self.__session.query(law_txt_files).filter_by(filename=filename).count()
        return True if query_rows_count>0 else False


    def get_attributes(self):
        return self.__args

    def save_law_file(self,filename):
        new_law_file = law_txt_files(filename=filename,status=LAW_FILE_STATUS.PROCESSED.value)
        self.__session.add(new_law_file)
        self.__session.commit()
        self.__session.flush()
        self.__session.close()



    def __reformat_date(self,old_date):
        if old_date:
            months = ast.literal_eval(self.__months_format)
            current_array_splitted = old_date.split(' ')
            return date(int(current_array_splitted[2]),
                        (self.__getIndexFromList(months,current_array_splitted[1])),
                        int(current_array_splitted[0]))
        else:
            return None

    def __getIndexFromList(self,gv_list,item):
        try:
            item = item.encode('utf-8')
            vl = [index for index in range(len(gv_list)) if gv_list[index] == item]
            if len(vl) == 0:
                # use the alternatives names for months
                months_al_list = ast.literal_eval(json.loads(json.dumps(self.__months__alternatives_format)))
                for alt in months_al_list:
                    for value in alt:
                       if value == item:
                        return int(alt[value])
            return vl[0]+1
        except Exception as ex:
            print self.__logger.info(ex.message)
            return None

class LAW_FILE_STATUS(enum.Enum):
    PROCESSED = 1
    UNPROCESSED = 0