import Model.DataClass as DataClass
import json
import os
import typing

def openFile(json_path : str) -> str:
    contents : str = str()
    try:
        with open(json_path, 'rb') as f:
            contents = f.read()
    except Exception as err:
        print("Failed to open {0}: {1}".format(json_path, err))
    return contents

def parseHeaderConfig(json_contents : str) -> DataClass.HeaderConfig:
    json_data = json.loads(json_contents)
    header_config = DataClass.HeaderConfig(json_data["path"], json_data["header"], json_data["footer"])
    return header_config

def parseConfigData(json_contents : str) -> typing.List[DataClass.ConfigData]:
    json_data = json.loads(json_contents)
    config_data : typing.List[DataClass.ConfigData] = list()
    for config in json_data["configs"]:
        parsed_config : DataClass.ConfigData = DataClass.ConfigData(config["symbol"], config["description"], config["detail"], config["enable"])
        config_data.append(parsed_config)
    return config_data
