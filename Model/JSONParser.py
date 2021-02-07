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

def parseValConfigData(json_contents : str) -> typing.List[DataClass.ValConfigData]:
    json_data = json.loads(json_contents)
    val_config_data : typing.List[DataClass.ValConfigData] = list()
    for val_config in json_data["val_configs"]:
        parsed_config : DataClass.ValConfigData = DataClass.ValConfigData(val_config["symbol"], val_config["description"], val_config["detail"], val_config["value"], val_config["enable"])
        val_config_data.append(parsed_config)
    return val_config_data