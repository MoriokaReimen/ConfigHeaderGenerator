import Model.DataClass as DataClass
import json
import os
import typing

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
