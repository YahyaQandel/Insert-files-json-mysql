import ConfigParser

class Configuration_Handler():

    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.config.read('classes/cfg/Configuration.cfg')

    
    def get(self,section,key):
        return self.config.get(section, key)
