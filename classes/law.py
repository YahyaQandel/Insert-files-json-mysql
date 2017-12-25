import requests
from models.law import Laws
from models.lawTxtFile import law_txt_files

from classes.config import Configuration_Handler
from classes.db import DBConnection
import enum 
import logging

# encoding=utf8  
import sys  
class Law():
    def __init__(self, args=None):
        if args:
            self.args = args
        self.session = DBConnection().session
        logger_cls = '%s.%s'%(Configuration_Handler.get('Logging', 'logger_instance_name'),self.__class__.__name__)
        self.logger = logging.getLogger(logger_cls)

    def set_attributes(self,args):
        self.args = args

    def save(self):
        try:
            self.args = self.encode_parameters(self.args)
            new_law = Laws(url=self.args['url'],
                        header=self.args['header'],
                        lawType=self.args['lawType'],
                        number=self.args['number'],
                        title=self.args['title'],
                        year=self.args['year'],
                        legalStatus=self.args['legalStatus'],
                        noPages=self.args['noPages'],
                        journal=self.args['journal'],
                        journalNo=self.args['journalNo'],
                        issueType=self.args['issueType'],
                        issueDate=self.args['issueDate'],
                        startDate=self.args['startDate'],
                        endDate=self.args['endDate']
                    )
            self.session.add(new_law)
            self.session.commit()
            self.session.flush()
            self.session.close()
            law_obj = self.session.query(Laws).filter_by(number=self.args['number']).first()
            if law_obj:
                logger_string = 'law number [%s] fetched successfully '%(self.args['number'])
                self.logger.info(logger_string)
                return True

        except Exception as e:
            self.logger.info(str(e))

    def encode_parameters(self,args):
        reload(sys)  
        sys.setdefaultencoding('utf8')
        for key,value in args.items():
            if isinstance(value,basestring):
                args[key] = value.encode('utf-8')

        return args

    def check_law_file_already_inserted(self,filename):
        query_rows_count = self.session.query(law_txt_files).filter_by(filename=filename).count()
        return True if query_rows_count>0 else False



    def save_law_file(self,filename):
        new_law_file = law_txt_files(filename=filename,status=LAW_FILE_STATUS.PROCESSED.value)
        self.session.add(new_law_file)
        self.session.commit()
        self.session.flush()
        self.session.close()


class LAW_FILE_STATUS(enum.Enum):
    PROCESSED = 1
    UNPROCESSED = 0