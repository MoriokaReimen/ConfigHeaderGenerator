import DataClass
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

if __name__ == '__main__':
    json_contents = """
    {
        "path" : "./hoge.json",
        "header" : "hogehogheo",
        "footer" : "fugafuga",
        "configs" : [
            {"symbol":"DEBUG", "description":"My Config", "detail":"my first config", "enable":true},
            {"symbol":"DEBUG2", "description":"My Config2", "detail":"my first config2", "enable":false}
        ]
    }
    """
    header_config = parseHeaderConfig(json_contents)
    print(header_config)
    configs = parseConfigData(json_contents)
    print(configs)
