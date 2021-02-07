import Model.DataClass
from typing import List
import re
import datetime
import os

def generateHeader(header_config: Model.DataClass.HeaderConfig, configs: List[Model.DataClass.ConfigData], val_configs: List[Model.DataClass.ValConfigData]) -> str:
    contents: str = str()

    header = header_config.header
    date_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
    header = re.sub("\$\{DATE_TIME\}", date_time, header)

    file_name = os.path.basename(header_config.path)
    header = re.sub("\$\{FILE_NAME\}", file_name, header)

    contents += header
    contents += "\r\n"
    contents += "/* Enable/Disable Configurations ******************************************/\r\n"
    for config in configs:
        if not config.enable:
            continue
        contents += "#define\t"
        contents += config.symbol
        contents += "\t/**< "
        contents += config.description
        contents += " */\r\n"
    contents += "\r\n"

    contents += "/* Value Configurations ***************************************************/\r\n"
    for val_config in val_configs:
        if not val_config.enable:
            continue
        contents += "#define\t"
        contents += val_config.symbol
        contents += "\t( "
        contents += str(val_config.value)
        contents += " )"
        contents += "\t/**< "
        contents += config.description
        contents += " */\r\n"
    
    contents += "\r\n"
    footer = header_config.footer

    date_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
    footer = re.sub("\$\{DATE_TIME\}", date_time, footer)

    file_name = os.path.basename(header_config.path)
    footer = re.sub("\$\{FILE_NAME\}", file_name, footer)

    contents += footer
    return contents
