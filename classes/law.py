import requests
import ConfigParser
from models.law import Laws
from sqlalchemy.orm import sessionmaker
import ConfigParser
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import Sequence
# encoding=utf8  
import sys  
class Law():
    def __init__(self, args=None):
        if args:
            self.args = args
        Base = declarative_base()
        config = ConfigParser.ConfigParser()
        config.read('Configuration.cfg')
        database_name = config.get('DataDB', 'name')
        column_length = config.get('DataDB', 'col_length')
        dbconnectionstring = 'mysql+pymysql://root:xwwx11@localhost/%s?charset=utf8'%(database_name)
        engine = create_engine(dbconnectionstring)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()


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
            return self.session.query(Laws).filter_by(number=self.args['number']).first()
        except Exception as e:
            return str(e)


    def encode_parameters(self,args):
        reload(sys)  
        sys.setdefaultencoding('utf8')
        for key,value in args.items():
            print key
            if isinstance(value,basestring):
                args[key] = value.encode('utf-8')
                print len(args[key])
                print "%s,%s"%(key,args[key])

        return args
