import Model.DataClass
from typing import List

def generateHeader(header_config : Model.DataClass.HeaderConfig, configs : List[Model.DataClass.ConfigData]) -> str:
    contents : str = str()
    contents += header_config.header
    contents += "\r\n"
    for config in configs:
        if not config.enable : continue
        contents += "#define\t"
        contents += config.symbol
        contents += "\t/* "
        contents += config.description
        contents += "*/\r\n"
    contents += header_config.footer
    return contents