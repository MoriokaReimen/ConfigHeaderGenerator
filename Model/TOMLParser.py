import Model.DataClass as DataClass
import toml
import os
import typing

def parseHeaderConfig(toml_contents : str) -> DataClass.HeaderConfig:
    toml_data = toml.loads(toml_contents)
    header_config = DataClass.HeaderConfig(toml_data["path"], toml_data["header"], toml_data["footer"])
    return header_config

def parseConfigData(toml_contents : str) -> typing.List[DataClass.ConfigData]:
    toml_data = toml.loads(toml_contents)
    config_data : typing.List[DataClass.ConfigData] = list()
    for config in toml_data["configs"]:
        parsed_config : DataClass.ConfigData = DataClass.ConfigData(config["symbol"], config["description"], config["detail"], config["enable"])
        config_data.append(parsed_config)
    return config_data

def parseValConfigData(toml_contents : str) -> typing.List[DataClass.ValConfigData]:
    toml_data = toml.loads(toml_contents)
    val_config_data : typing.List[DataClass.ValConfigData] = list()
    for val_config in toml_data["val_configs"]:
        parsed_config : DataClass.ValConfigData = DataClass.ValConfigData(val_config["symbol"], val_config["description"], val_config["detail"], val_config["value"], val_config["enable"])
        val_config_data.append(parsed_config)
    return val_config_data