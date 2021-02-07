import Model.DataClass
from typing import List

def generateHeader(header_config : Model.DataClass.HeaderConfig, configs : List[Model.DataClass.ConfigData], val_configs : List[Model.DataClass.ValConfigData]) -> str:
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

    for val_config in val_configs:
        if not val_config.enable : continue
        contents += "#define\t"
        contents += val_config.symbol
        contents += "\t( "
        contents += str(val_config.value)
        contents += " )"
        contents += "\t/* "
        contents += config.description
        contents += "*/\r\n"

    contents += header_config.footer
    return contents