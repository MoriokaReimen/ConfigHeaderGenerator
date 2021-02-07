import Model.Utility
import Model.DataClass
import Model.JSONParser
import Model.HeaderGenerator

class Control:
    def __init__(self):
        self.loadFile()

    def loadFile(self):
        contents = Model.Utility.openFile("config.json")
        self.header_config = Model.JSONParser.parseHeaderConfig(contents)
        self.configs = Model.JSONParser.parseConfigData(contents)
    
    def generateHeader(self):
        contents = Model.HeaderGenerator.generateHeader(self.header_config, self.configs)
        Model.Utility.writeFile(self.header_config.path, contents)
    
    def getConfigs(self):
        return self.configs
    
    def getHeaderConfig(self):
        return self.header_config