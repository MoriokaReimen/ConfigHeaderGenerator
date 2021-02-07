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
        self.val_configs = Model.JSONParser.parseValConfigData(contents)
    
    def generateHeader(self):
        contents = Model.HeaderGenerator.generateHeader(self.header_config, self.configs, self.val_configs)
        Model.Utility.writeFile(self.header_config.path, contents)
    
    def getConfigs(self):
        return self.configs
    
    def getValConfigs(self):
        return self.val_configs

    def getHeaderConfig(self):
        return self.header_config
