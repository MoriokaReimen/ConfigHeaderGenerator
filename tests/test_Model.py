import pytest
import app.JSONParser

def test_parseHeaderConfig():
    json_contents = """
    {
        "path":"./hoge",
        "header":"header",
        "footer":"footer"
    }
    """
    header_config = app.JSONParser.parseHeaderConfig(json_contents)
    assert header_config.path == "./hoge"
    assert header_config.header == "header"
    assert header_config.footer == "footer"

def test_parseConfigData():
    json_contents = """
    {
       "configs" : [
            {"symbol":"DEBUG", "description":"My Config", "detail":"my first config", "enable":true},
            {"symbol":"DEBUG2", "description":"My Config2", "detail":"my second config", "enable":false}
        ]
    }
    """
    configs = app.JSONParser.parseConfigData(json_contents)
    assert configs[0].symbol == "DEBUG"
    assert configs[0].description == "My Config"
    assert configs[0].detail == "my first config"
    assert configs[0].enable == True

    assert configs[1].symbol == "DEBUG2"
    assert configs[1].description == "My Config2"
    assert configs[1].detail == "my second config"
    assert configs[1].enable == False

