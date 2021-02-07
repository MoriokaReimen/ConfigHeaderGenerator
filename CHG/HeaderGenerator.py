import DataClass
from typing import List

def generateHeader(header_config : DataClass.HeaderConfig, configs : List[DataClass.ConfigData]) -> str:
    contents : str = str()
    contents += header_config.header
    contents += "\r\n"
    for config in configs:
        contents += "#define\t"
        contents += config.symbol
        contents += "\t/* "
        contents += config.description
        contents += "*/\r\n"
    return contents